# ---------- Base libraries -------------------------------------------------------------------------------------------
from typing import cast, Callable
import os
import logging
import subprocess
import platform
from datetime import datetime
import shutil
import pyqtgraph as pg
import time

# ---------- Numerical Visual packages---------------------------------------------------------------------------------
import numpy as np
from numpy.typing import NDArray
from PIL import Image                # instead of  import cv2 as cv
import pandas as pd
import math
from scipy import signal as sig
from scipy.optimize import curve_fit 

# ---------- GUI libraries --------------------------------------------------------------------------------------------
from PySide6.QtWidgets import  QMainWindow, QWidget, QFileSystemModel, QMessageBox, QSpinBox, QApplication
from PySide6.QtGui import QKeySequence, QShortcut, QColor
from PySide6.QtCore import QModelIndex, QDir, Qt, QPersistentModelIndex, QPointF, QObject

# ---------- Custom libs ----------------------------------------------------------------------------------------------
from Custom_UIs.UI_Mainwindow import Ui_MainWindow
from Custom_Libs.Lib_DataDirTree import DataDirTree
from bps_raw_jpeg_processer.src.better_bps_raw_jpeg_processor import quadratic_func, sigmoid_func,  background_new, JpegProcessor, Three_channel_spectra
from bps_raw_jpeg_processer.src.pxlspec_to_pxlweb_formula import pxlspec_to_pxlweb_formula

# ---------- pqgraph config -------------------------------------------------------------------------------------------
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

logger = logging.getLogger(__name__)

def open_file_externally(filepath: str) -> None:
    """Opens given file externally, without hanging current running python script."""
    system_str = platform.system()
    try:
        if system_str == "Windows":  # Windows
            os.startfile(filepath)  # type: ignore
        elif system_str == "Darwin":  # BSDs and macos
            _ = subprocess.Popen(("open ", filepath), stdin=None, stdout=None, stderr=None, close_fds=True)  # shell=True,
        elif system_str == "Linux":  # linux variants
            _ = subprocess.Popen(
                ("xdg-open", os.path.abspath(filepath)),  # shell=True,
                stdin=None,
                stdout=None,
                stderr=None,
                close_fds=True,
            )
        else:
            logger.warning(f"Strange os-platform string id: {system_str}")
            logger.warning(" - Cannot open file")
        return None
    except Exception as e:
        logger.warning(f"error when openning {filepath}:\n{e}")
        return None


class FileSystemModel(QFileSystemModel):
    # read from https://stackoverflow.com/a/40455027/14696853
    def __init__(self, *args: QObject | None, **kwargs: QObject | None) -> None:
        super(FileSystemModel, self).__init__(*args, **kwargs)
        #self.setNameFilters((["*.jpeg", "*.jpg", "*.json"]))
        self.setNameFilters((["*.jpeg"]))
        # self.setNameFilterDisables(False)
        # , "*.tiff", "*.npy", "*.mat", "*.png"]))
        # self.setNameFilterDisables(False)
        # self.setNameFilterDisables(True)
    #@override
    def data(self, index: QModelIndex|QPersistentModelIndex, role:int =Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.ForegroundRole:
            text: str = index.data(Qt.ItemDataRole.DisplayRole)
            if (".jpeg" in text) and (text.count("_") in (3, 4)) and text.replace(".jpeg", "").replace("_", "").isnumeric():
                return QColor("#58cd1c")

            elif text.count("_") == 1 and (len(text) == 15) and text.replace("_", "").isnumeric():
                return QColor("#288d4c")
        return super(FileSystemModel, self).data(index, role)

class TheMainWindow(QMainWindow):
    dir_path: str = QDir.homePath()
    jpeg_path: str = ""
    help_html_path: str = os.path.join(QDir.currentPath(), "docs/help.html") # need change on the binary release?
    ddtree: DataDirTree = DataDirTree()
    jp: JpegProcessor = JpegProcessor()
    wv: NDArray[np.float64] = np.zeros((2464, 3280), dtype=np.float64)
    

    paramLogPath: str = ""
    dfParamHistory: pd.DataFrame = pd.DataFrame()
    paramsChangingFromHistory: bool = False

    def __init__(self, parent: QWidget | None = None) -> None:
        super(TheMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        _ = self.ui.pb_calibrate_calculate.clicked.connect(self.call_calibrate_and_calculate)
        _ = self.ui.pb_export.clicked.connect(self.short_cut_export_raw_jpeg)
        _ = self.ui.pb_dir_goto_parent.clicked.connect(self.short_cut_goto_parent_dir)

        _ = self.ui.clb_0_file2roi_dist.clicked.connect(lambda: self.handle_when_stages_changes(0))
        _ = self.ui.clb_1_dist_to_curve.clicked.connect(lambda: self.handle_when_stages_changes(1))
        _ = self.ui.clb_2_3curves_to_3refl.clicked.connect(lambda: self.handle_when_stages_changes(2))
        _ = self.ui.clb_3_3refl_to_1refl.clicked.connect(lambda: self.handle_when_stages_changes(3))
        # -------------------------------------------------------------------------------------------
        _ = self.ui.sb_3to1_a1.valueChanged.connect(self.handle_when_3to1_sb_changes)
        _ = self.ui.sb_3to1_a2.valueChanged.connect(self.handle_when_3to1_sb_changes)
        _ = self.ui.sb_3to1_a3.valueChanged.connect(self.handle_when_3to1_sb_changes)
        _ = self.ui.sb_3to1_w1.valueChanged.connect(self.handle_when_3to1_sb_changes)
        _ = self.ui.sb_3to1_w2.valueChanged.connect(self.handle_when_3to1_sb_changes)
        _ = self.ui.sb_3to1_w3.valueChanged.connect(self.handle_when_3to1_sb_changes)

        self.graph_3to1_weights = {
            "r" : self.ui.graph_3to1_weight.getPlotItem().plot(pen=pg.mkPen("r", width=2, style=Qt.PenStyle.SolidLine), name="R"),
            "g" : self.ui.graph_3to1_weight.getPlotItem().plot(pen=pg.mkPen("g", width=2, style=Qt.PenStyle.SolidLine), name="G"),
            "b" : self.ui.graph_3to1_weight.getPlotItem().plot(pen=pg.mkPen("b", width=2, style=Qt.PenStyle.SolidLine), name="B"),
            #"759.4nm": self.ui.graph_raw.addItem(pg.InfiniteLine(pos=759.37, movable=False, angle=90, label="x={value:0.2f}nm", labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True})),
        }
        self.graph_3to1_callable: dict[str, Callable[[NDArray[np.float64]], NDArray[np.float64]]] = {
            "r" : lambda wv: wv,
            "g" : lambda wv: wv,
            "b" : lambda wv: wv,
        }

        self.graph_rgb_weighted = {
            "r" : self.ui.graph_refl_curve_weighted.getPlotItem().plot(pen=pg.mkPen("r", width=2, style=Qt.PenStyle.DashLine), name="R"),
            "g" : self.ui.graph_refl_curve_weighted.getPlotItem().plot(pen=pg.mkPen("g", width=2, style=Qt.PenStyle.DashLine), name="G"),
            "b" : self.ui.graph_refl_curve_weighted.getPlotItem().plot(pen=pg.mkPen("b", width=2, style=Qt.PenStyle.DashLine), name="B"),
            "k" : self.ui.graph_refl_curve_weighted.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine), name="B"),
            #"759.4nm": self.ui.graph_raw.addItem(pg.InfiniteLine(pos=759.37, movable=False, angle=90, label="x={value:0.2f}nm", labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True})),
        }

        # -----------------------------------------------------------------------------

        # --------------- initialize the file system ----------------------------------
        self.fsmodel = FileSystemModel()
        _ = self.fsmodel.setRootPath(QDir.homePath())

        self.ui.tv_dir.setModel(self.fsmodel)
        self.ui.tv_dir.setRootIndex(self.fsmodel.setRootPath(QDir.homePath()))
        #self.ui.tv_dir.setRootIndex(self.fsmodel.setRootPath("/home/garid/test_alfa-20230529_091201/20230529_091201_0207367_0000.jpeg")) # TODO change before 
        _ = self.ui.tv_dir.doubleClicked.connect(self.call_tv_onItemDoubleClicked)
        self.short_cut_goto_parent_dir()
        # -----------------------------------------------------------------------------
        _ = self.ui.cb_ft_filter.stateChanged.connect(
            lambda: self.fsmodel.setNameFilters((["*.jpeg"] if self.ui.cb_ft_filter.isChecked() else ["*"]))
        )
        _ = self.ui.cb_calc5_norm.stateChanged.connect(self.handle_cb_calc5_norming)
        _ = self.ui.sb_calc5_norm_zero.valueChanged.connect(self.handle_cb_calc5_norming)
        _ = self.ui.sb_calc5_norm_one.valueChanged.connect(self.handle_cb_calc5_norming)
        _ = self.ui.pb_waveperpixel_reset.clicked.connect(lambda: self.ui.sb_waveperpixel.setValue(1.8385))
        _ = self.ui.pb_system_file_explorer.clicked.connect(self.open_directory_at_point)
        _ = self.ui.le_tv_name_narrower.textChanged.connect(self.dir_searching_based_regex)
        _ = self.ui.cb_parameter_history.currentTextChanged.connect(self.set_calculation_params_from_history_selection)
        _ = self.ui.hs_target_distance.valueChanged.connect(self.update_fov_on_webcam)
        # -----------------------------------------------------------------------------
        self.ui.graph_2dimg.getView().invertY(not self.ui.cb_invert_y_axis_of_rawbayer.isChecked())
        _ = self.ui.cb_invert_y_axis_of_rawbayer.stateChanged.connect(
            lambda: self.ui.graph_2dimg.getView().invertY(not self.ui.cb_invert_y_axis_of_rawbayer.isChecked())
        )
        _ = self.ui.cb_2dimg_key.currentTextChanged.connect(self.update_1_rawbayer_img_data_and_then_plot_below)

        # init_2d_graph_hide_the_original_roi_buttons -----------------------------------------------------------------
        self.selected_ROI_spectrum: dict[str, Three_channel_spectra] = {
            "obje" : Three_channel_spectra(),
            "gray" : Three_channel_spectra(),
            "refl" : Three_channel_spectra(),
        } 
        self.ui.pb_select_gray_roi.clicked.connect(lambda: self.callback_roi_load_to_analysis("gray"))
        self.ui.pb_select_obje_roi.clicked.connect(lambda: self.callback_roi_load_to_analysis("obje"))


        self.roi_label_gray = pg.TextItem(
            html='<div style="text-align: center"><span style="color: #FFF;">Gray-ROI</span></div>',
            anchor=(0, 1),
            border="w",
            fill=(200, 50, 50, 100)
        )

        self.roi_label_obje = pg.TextItem(
            html='<div style="text-align: center"><span style="color: #FFF;">Object-ROI</span></div>',
            anchor=(0, 1),
            border="w",
            fill=(50, 50, 200, 100)
        )

        # init_all_6_roi ----------------------------------------------------------------------------------------------
        self.roi_gray_main = pg.ROI(
            pos=[self.ui.sb_midx_init.value(), self.ui.sb_gray_posy.value()],
            size=pg.Point(700, self.ui.sb_gray_sizy.value()),
            movable=True, scaleSnap=True, snapSize=2, translateSnap=True,
        )

        self.roi_obje_main = pg.ROI(
            pos=[self.ui.sb_midx_init.value(), self.ui.sb_obje_posy.value()],
            size=pg.Point(700, self.ui.sb_obje_sizy.value()),
            movable=True, scaleSnap=True, snapSize=2, translateSnap=True,
        )

        self.roi_wave759nm = pg.ROI(
            pos=[self.ui.sb_roi759_posx.value(), self.ui.sb_roi759_posy.value()],
            size=pg.Point(self.ui.sb_roi759_sizx.value(), self.ui.sb_roi759_sizy.value()),
            movable=True, scaleSnap=True, snapSize=2, translateSnap=True,
        )

        self.roi_bgle = pg.ROI(
            pos=[self.ui.sb_bgle_posx.value(), self.ui.sb_bg___posy.value()],
            size=pg.Point(self.ui.sb_bgle_sizx.value(), self.ui.sb_bg___sizy.value()),
            movable=True, scaleSnap=True, snapSize=2, translateSnap=True,
        )

        self.roi_bgri = pg.ROI(
            pos=[self.ui.sb_bgri_posx.value(), self.ui.sb_bg___posy.value()],
            size=pg.Point(self.ui.sb_bgri_sizx.value(), self.ui.sb_bg___sizy.value()),
            movable=True, scaleSnap=True, snapSize=2, translateSnap=True,
        )

        # end init_all_6_roi ------------------------------------------------------------------------------------------

        _ = self.ui.graph_raw.getPlotItem().addLegend()
        self.graph_raw_lines = {
            "gray_r" : self.ui.graph_raw.getPlotItem().plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine), name="R-gray"),
            "gray_g" : self.ui.graph_raw.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="G-gray"),
            "gray_G" : self.ui.graph_raw.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="G-gray"),
            "gray_b" : self.ui.graph_raw.getPlotItem().plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine), name="B-gray"),
            "obje_r" : self.ui.graph_raw.getPlotItem().plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DashLine),  name="R-object"),
            "obje_g" : self.ui.graph_raw.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine),  name="G-object"),
            "obje_G" : self.ui.graph_raw.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine),  name="G-object"),
            "obje_b" : self.ui.graph_raw.getPlotItem().plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DashLine),  name="B-object"),
            "759.4nm": self.ui.graph_raw.addItem(pg.InfiniteLine(pos=759.37, movable=False, angle=90, label="x={value:0.2f}nm", labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True})),
        }
        # ----------------------------------------------------
        self.graph_2dimg_wave_curves: dict[str, tuple[NDArray[np.float64], pg.PlotCurveItem]] = { #np.ndarray[tuple[int, int, int], np.dtype[np.float64]]
            "400":    (np.array([0, 0, 0], dtype=np.float64), pg.PlotCurveItem(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine))),
            "500":    (np.array([0, 0, 0], dtype=np.float64), pg.PlotCurveItem(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine))),
            #"550":    (np.array([0, 0, 0], dtype=np.float64), pg.PlotCurveItem()),
            "600":    (np.array([0, 0, 0], dtype=np.float64), pg.PlotCurveItem(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine))),
            #"650":    (np.array([0, 0, 0], dtype=np.float64), pg.PlotCurveItem()),
            "700":    (np.array([0, 0, 0], dtype=np.float64), pg.PlotCurveItem(pen=pg.mkPen("w", width=1, style=Qt.PenStyle.SolidLine))),
            "759.37": (np.array([0, 0, 0], dtype=np.float64), pg.PlotCurveItem(pen=pg.mkPen("w", width=1, style=Qt.PenStyle.SolidLine))),
            "800":    (np.array([0, 0, 0], dtype=np.float64), pg.PlotCurveItem(pen=pg.mkPen("w", width=1, style=Qt.PenStyle.SolidLine))),
            #"850":    (np.array([0, 0, 0], dtype=np.float64), pg.PlotCurveItem()),
        }
        self.graph_distributive_dn: dict[str, pg.PlotDataItem] = {
            "red_obje" : self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=None, symbol='o', symbolPen=None, symbolSize=3, symbolBrush=(255, 40, 40)),
            "grn_obje" : self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=None, symbol='o', symbolPen=None, symbolSize=3, symbolBrush=(40, 255, 40)),
            "blu_obje" : self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=None, symbol='o', symbolPen=None, symbolSize=3, symbolBrush=(40, 40, 255)),
            "red_gray" : self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=None, symbol='x', symbolPen=None, symbolSize=3, symbolBrush=(255, 40, 40)),
            "grn_gray" : self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=None, symbol='x', symbolPen=None, symbolSize=3, symbolBrush=(40, 255, 40)),
            "blu_gray" : self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=None, symbol='x', symbolPen=None, symbolSize=3, symbolBrush=(40, 40, 255)),
            "R_gray_savgol_ith" :  self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=4, style=Qt.PenStyle.SolidLine)),
            "G_gray_savgol_ith" :  self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=4, style=Qt.PenStyle.SolidLine)),
            "B_gray_savgol_ith" :  self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=4, style=Qt.PenStyle.SolidLine)),
            "R_obje_savgol_ith" :  self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=4, style=Qt.PenStyle.SolidLine)),
            "G_obje_savgol_ith" :  self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=4, style=Qt.PenStyle.SolidLine)),
            "B_obje_savgol_ith" :  self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=4, style=Qt.PenStyle.SolidLine)),
            "R_gray_savgol_curve" :  self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine)),
            "G_gray_savgol_curve" :  self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine)),
            "B_gray_savgol_curve" :  self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine)),
            "R_obje_savgol_curve" :  self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine)),
            "G_obje_savgol_curve" :  self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine)),
            "B_obje_savgol_curve" :  self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine)),
        }

        self.graph_curves: dict[str, pg.PlotDataItem] = {
            "gray_R_dn_sub_bg": self.ui.graph_gray_curve_rgb.getPlotItem().plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine)),
            "gray_G_dn_sub_bg": self.ui.graph_gray_curve_rgb.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine)),
            "gray_B_dn_sub_bg": self.ui.graph_gray_curve_rgb.getPlotItem().plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine)),

            "obje_R_dn_sub_bg": self.ui.graph_obje_curve_rgb.getPlotItem().plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine)),
            "obje_G_dn_sub_bg": self.ui.graph_obje_curve_rgb.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine)),
            "obje_B_dn_sub_bg": self.ui.graph_obje_curve_rgb.getPlotItem().plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine)),

            "refl_R_dn_sub_bg": self.ui.graph_refl_curve_rgb.getPlotItem().plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine)),
            "refl_G_dn_sub_bg": self.ui.graph_refl_curve_rgb.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine)),
            "refl_B_dn_sub_bg": self.ui.graph_refl_curve_rgb.getPlotItem().plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine)),

            #"red_obje" : self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=None, symbol='o', symbolPen=None, symbolSize=3, symbolBrush=(255, 40, 40)),
            #"grn_obje" : self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=None, symbol='o', symbolPen=None, symbolSize=3, symbolBrush=(40, 255, 40)),
            #"blu_obje" : self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=None, symbol='o', symbolPen=None, symbolSize=3, symbolBrush=(40, 40, 255)),
            #"red_gray" : self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=None, symbol='x', symbolPen=None, symbolSize=3, symbolBrush=(255, 40, 40)),
            #"grn_gray" : self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=None, symbol='x', symbolPen=None, symbolSize=3, symbolBrush=(40, 255, 40)),
            #"blu_gray" : self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=None, symbol='x', symbolPen=None, symbolSize=3, symbolBrush=(40, 40, 255)),
            #"R_gray_savgol_ith" :  self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=4, style=Qt.PenStyle.SolidLine)),
            #"G_gray_savgol_ith" :  self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=4, style=Qt.PenStyle.SolidLine)),
            #"B_gray_savgol_ith" :  self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=4, style=Qt.PenStyle.SolidLine)),
            #"R_obje_savgol_ith" :  self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=4, style=Qt.PenStyle.SolidLine)),
            #"G_obje_savgol_ith" :  self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=4, style=Qt.PenStyle.SolidLine)),
            #"B_obje_savgol_ith" :  self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=4, style=Qt.PenStyle.SolidLine)),
            #"R_gray_savgol_curve" :  self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine)),
            #"G_gray_savgol_curve" :  self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine)),
            #"B_gray_savgol_curve" :  self.ui.graph_gray_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine)),
            #"R_obje_savgol_curve" :  self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine)),
            #"G_obje_savgol_curve" :  self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine)),
            #"B_obje_savgol_curve" :  self.ui.graph_obje_roi_spectra.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine)),
        }

        # ----------------------------------------------------
        # self.iso = pg.IsocurveItem(level=0.8, pen='g')
        # self.iso.setParentItem(self.ui.graph_2dimg.getImageItem())
        # self.iso.setZValue(5)
        # self.ui.sp_wv_shower.valueChanged.connect(
        #    lambda: self.iso.setLevel(self.ui.sp_wv_shower.value())
        # )

        # self.ui.graph_calc4_refl_rgb.getPlotItem().setLabels() # left="axis 1"
        # == 2025-05-03 self.p2 = pg.ViewBox()
        # == 2025-05-03 self.ui.graph_calc4_refl_rgb.getPlotItem().showAxis("right")
        # == 2025-05-03 self.ui.graph_calc4_refl_rgb.getPlotItem().scene().addItem(self.p2)
        # == 2025-05-03 self.ui.graph_calc4_refl_rgb.getPlotItem().getAxis("right").linkToView(self.p2)
        # == 2025-05-03 self.p2.setXLink(self.ui.graph_calc4_refl_rgb.getPlotItem().getViewBox())
        # == 2025-05-03 self.ui.graph_calc4_refl_rgb.getPlotItem().getAxis("right").setLabel("Weight of combination", color="#3f3f3f")


        # == 2025-05-03 def updateViews():
        # == 2025-05-03     #_ = self.ui.graph_calc4_refl_rgb.getPlotItem().addLegend()
        # == 2025-05-03     self.p2.setGeometry(self.ui.graph_calc4_refl_rgb.getPlotItem().getViewBox().sceneBoundingRect())
        # == 2025-05-03     self.p2.linkedViewChanged(self.ui.graph_calc4_refl_rgb.getPlotItem().getViewBox(), self.p2.XAxis)

        # == 2025-05-03 self.ui.graph_calc4_refl_rgb.getPlotItem().vb.sigResized.connect(updateViews)

        # == 2025-05-03 self.p2_weight_r = pg.PlotDataItem(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DashLine), name="R-weight")
        # == 2025-05-03 self.p2_weight_g = pg.PlotDataItem(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine), name="G-weight")
        # == 2025-05-03 self.p2_weight_b = pg.PlotDataItem(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DashLine), name="B-weight")

        # == 2025-05-03 self.p2.addItem(self.p2_weight_r)
        # == 2025-05-03 self.p2.addItem(self.p2_weight_g)
        # == 2025-05-03 self.p2.addItem(self.p2_weight_b)

        # == 2025-05-03 tmp_x = self.jp.gray.itp_hor_nm_array

        # == 2025-05-03 self.p2_weight_r.setData(tmp_x[:-100] / 10**9, self.jp.weight_r[:-100])
        # == 2025-05-03 self.p2_weight_g.setData(tmp_x[:-100] / 10**9, self.jp.weight_g[:-100])
        # == 2025-05-03 self.p2_weight_b.setData(tmp_x[:-100] / 10**9, self.jp.weight_b[:-100])

        # == 2025-05-03 updateViews()
        #   -----------------------------------------------------------------------------------------------------------
        # self.graph_759nm_line_for_2dimg = pg.InfiniteLine(
        #     pos=192*2 + self.ui.sb_midx_init.value(), movable=False, angle=90, label="759.3nm",
        #     #labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True}
        # )
        #self.ui.graph_2dimg.getView().addItem(self.graph_759nm_line_for_2dimg)

        #   -----------------------------------------------------------------------------------------------------------
        self.ui.pb_savgol_calc.clicked.connect(self.callback_savgol)
        self.ui.sb_savgol_wv_num.valueChanged.connect(
            lambda: self.ui.sb_savgol_wv_step.setValue((self.ui.sb_savgol_wv1.value() - self.ui.sb_savgol_wv0.value())//(self.ui.sb_savgol_wv_num.value()-1))
        )

        #self.ui.sb_savgol_wv_step.valueChanged.connect(
        #    lambda: self.ui.sb_savgol_wv_num.setValue((self.ui.sb_savgol_wv1.value() - self.ui.sb_savgol_wv0.value())//self.ui.sb_savgol_wv_step.value()+1)
        #)

        #   -----------------------------------------------------------------------------------------------------------
        # def init_1_webfov_roi(self) -> None:
        self.roi_webcam_fov = pg.ROI(
            pos=[100, 100],        # x, y
            size=pg.Point(30, 40 ),
            movable=True, scaleSnap=True, snapSize=2, translateSnap=True,
        )
        self.roi_webcam_fov.setZValue(10)
        self.ui.graph_webcam.getView().addItem(self.roi_webcam_fov)

        self.ui.graph_webcam.ui.roiBtn.hide()
        self.ui.graph_webcam.ui.menuBtn.hide()
        self.ui.graph_759_roi.ui.roiBtn.hide()
        self.ui.graph_759_roi.ui.menuBtn.hide()
        self.ui.graph_759_roi.ui.histogram.hide()

        # -------------------------------------------------------------------------------------------------------------
        self.graph5_curve_relf = self.ui.graph_calc5_refl_final.getPlotItem().plot(
            pen=pg.mkPen(
                "k",
                width=1, style=Qt.PenStyle.SolidLine
            ), name="Reflection")
        self.graph5_norm_zero_line = pg.InfiniteLine(
                pos=self.ui.sb_calc5_norm_zero.value() / 10**9,
                movable=False, angle=90,
                label="x={value:0.2f}nm",
                labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True})
        self.graph5_norm_one_line = pg.InfiniteLine(
                pos=self.ui.sb_calc5_norm_one.value() / 10**9,
                movable=False, angle=90,
                label="x={value:0.2f}nm",
                labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True})
        #   -----------------------------------------------------------------------------------------------------------

        self.graph_physical_spectrometer_shape = pg.GraphItem()
        self.graph_physical_spectrometer_shape_vertex = np.array(
            [ [0.0,   0.0 - 2.5],  # 0
              [0.0,   5.0 - 2.5],  # 1
              [-9.6,  5.0 - 2.5],  # 2
              [-9.6,  8.0 - 2.5],  # 3
              [-10.3, 8.6 - 2.5],  # 4
              [-10.3, 9.0 - 2.5],  # 5
              [-14.7, 9.0 - 2.5],  # 6
              [-14.7, 0.0 - 2.5],  # 7
            ]
        )
        self.graph_physical_spectrometer_shape_edges = np.array([ [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]])
        self.graph_physical_spectrometer_shape_edges_colors = np.array(
            [
                (255, 0, 0, 255, 1), (255, 0, 0, 255, 1), (255, 0, 0, 255, 1), (255, 0, 0, 255, 1),
                (255, 0, 0, 255, 1), (255, 0, 0, 255, 1), (255, 0, 0, 255, 1), (255, 0, 0, 255, 1),
            ],
            dtype=[
                ("red", np.ubyte),
                ("green", np.ubyte),
                ("blue", np.ubyte),
                ("alpha", np.ubyte),
                ("width", float),
            ],
        )
        # ------------------------------------------------------------------------------------------------------------
        self.graph_physical_vfov_ground_projection_shape = pg.GraphItem()
        self.graph_physical_vfov_ground_proj_vertex = np.array(
            [ [0.0,   0.0],  # 0
              [0,   -self.ui.hs_physical_height.value()],  # 1
              [self.ui.hs_physical_height.value()* math.tan(math.pi/2 + math.radians(self.ui.hs_physical_elv.value() -1.85)),   -self.ui.hs_physical_height.value()],  # 2
              [self.ui.hs_physical_height.value()* math.tan(math.pi/2 + math.radians(self.ui.hs_physical_elv.value()      )),   -self.ui.hs_physical_height.value()],  # 3
              [self.ui.hs_physical_height.value()* math.tan(math.pi/2 + math.radians(self.ui.hs_physical_elv.value() +5.61)),   -self.ui.hs_physical_height.value()],  # 4
            ]
        )
        self.graph_physical_vfov_ground_proj_edges = np.array(
            [ [0, 1], [0,2], [0,3], [0,4], [1, 4]]
        )

        self.graph_physical_vfov_ground_proj_edges_colors = np.array(
            [
                (255, 0, 0, 255, 1), (255, 0, 0, 255, 1), (255, 0, 0, 255, 1), (255, 0, 0, 255, 1), (255, 0, 0, 255, 1), #(255, 0, 0, 255, 1), (255, 0, 0, 255, 1), (255, 0, 0, 255, 1),
            ],
            dtype=[
                ("red", np.ubyte),
                ("green", np.ubyte),
                ("blue", np.ubyte),
                ("alpha", np.ubyte),
                ("width", float),
            ],
        )

        # -------- init the others ------------------------------
        self.init_2d_graph_hide_the_original_roi_buttons()
        self.init_all_6_roi()
        self.init_sb_signals_for_ROI_controls()
        self.init_all_pyqtgraph()
        self.init_keyboard_bindings()
        self.init_actions()

        # self.update_physical_graph()

        self.init_physical_repr_graph()
        _ = self.ui.hs_physical_elv.valueChanged.connect(self.update_physical_graph)
        _ = self.ui.hs_physical_height.valueChanged.connect(self.update_physical_graph)

        _ = self.ui.tw_midcol.currentChanged.connect(self.handle_when_tw_midcol_changed)
        _ = self.ui.cb_shows_calibrated_wl.checkStateChanged.connect(self.handle_when_to_show_calibrated_wavelenghts)

        self.handle_when_tw_midcol_changed() # just so it starts correctly
        self.handle_when_3to1_sb_changes() # just setting


    def handle_when_3to1_sb_changes(self) -> None:
        w1, a1 = self.ui.sb_3to1_w1.value(), self.ui.sb_3to1_a1.value()
        w2, a2 = self.ui.sb_3to1_w2.value(), self.ui.sb_3to1_a2.value()
        w3, a3 = self.ui.sb_3to1_w3.value(), self.ui.sb_3to1_a3.value()
        self.graph_3to1_callable["b"] = lambda wv:                            sigmoid_func(wv, w1, -a1)     + sigmoid_func(wv, w3, a3)/ 3
        self.graph_3to1_callable["g"] = lambda wv: sigmoid_func(wv, w1, a1) + sigmoid_func(wv, w2, -a2) - 1 + sigmoid_func(wv, w3, a3)/ 3 
        self.graph_3to1_callable["r"] = lambda wv: sigmoid_func(wv, w2, a2) + sigmoid_func(wv, w3, -a3) - 1 + sigmoid_func(wv, w3, a3)/ 3

        tmpx = np.arange(400, 900, 0.1, dtype=np.float64)
        self.graph_3to1_weights["r"].setData(tmpx, self.graph_3to1_callable["r"](tmpx))
        self.graph_3to1_weights["g"].setData(tmpx, self.graph_3to1_callable["g"](tmpx))
        self.graph_3to1_weights["b"].setData(tmpx, self.graph_3to1_callable["b"](tmpx))

        _ = self.ui.graph_3to1_weight.getPlotItem().addLegend()
        out_refl = np.zeros_like(self.selected_ROI_spectrum["refl"].channel["R"].savgol_out_curve)
        for rgb_key in ("R", "G", "B"):
            wv = self.selected_ROI_spectrum["refl"].channel[rgb_key].fullwave
            tmp = self.graph_3to1_callable[rgb_key.lower()](self.selected_ROI_spectrum["refl"].channel[rgb_key].fullwave) * self.selected_ROI_spectrum["refl"].channel[rgb_key].savgol_out_curve
            self.graph_rgb_weighted[rgb_key.lower()].setData(wv,tmp)
            out_refl[:] = out_refl[:] + tmp[:]

        self.graph_rgb_weighted["k"].setData(wv, out_refl) # TODO cahnge wv

    def callback_roi_load_to_analysis(self, key: str) -> None:

        assert key in self.selected_ROI_spectrum.keys(), f"bad {key=} must be in { self.selected_ROI_spectrum.keys()}"

        if key == "gray":
            roi_geometry = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_gray_main.getState())
        else: # key == "obje":
            roi_geometry  = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_obje_main.getState())

        self.selected_ROI_spectrum[key].channel["R"].set_data(
            dn = self.jp.get_array("Raw bayer (Noise Filter)", "Mask red",   roi_geometry),
            bg = self.jp.get_array("Background Est.", "Mask red",            roi_geometry),
            wv = self.jp.get_array("Wavelength", "Mask red",                 roi_geometry),
        )

        self.selected_ROI_spectrum[key].channel["G"].set_data(
            dn = self.jp.get_array("Raw bayer (Noise Filter)", "Mask green",   roi_geometry),
            bg = self.jp.get_array("Background Est.", "Mask green",            roi_geometry),
            wv = self.jp.get_array("Wavelength", "Mask green",                 roi_geometry),
        )

        self.selected_ROI_spectrum[key].channel["B"].set_data(
            dn = self.jp.get_array("Raw bayer (Noise Filter)", "Mask blue",   roi_geometry),
            bg = self.jp.get_array("Background Est.", "Mask blue",            roi_geometry),
            wv = self.jp.get_array("Wavelength", "Mask blue",                 roi_geometry),
        )

        self.graph_distributive_dn["red_gray"].setData(self.selected_ROI_spectrum["gray"].channel["R"].spectra["wavelength"], self.selected_ROI_spectrum["gray"].channel["R"].spectra["raw-dn-val"]) 
        self.graph_distributive_dn["red_obje"].setData(self.selected_ROI_spectrum["obje"].channel["R"].spectra["wavelength"], self.selected_ROI_spectrum["obje"].channel["R"].spectra["raw-dn-val"]) 

        self.graph_distributive_dn["grn_gray"].setData(self.selected_ROI_spectrum["gray"].channel["G"].spectra["wavelength"], self.selected_ROI_spectrum["gray"].channel["G"].spectra["raw-dn-val"]) 
        self.graph_distributive_dn["grn_obje"].setData(self.selected_ROI_spectrum["obje"].channel["G"].spectra["wavelength"], self.selected_ROI_spectrum["obje"].channel["G"].spectra["raw-dn-val"]) 

        self.graph_distributive_dn["blu_gray"].setData(self.selected_ROI_spectrum["gray"].channel["B"].spectra["wavelength"], self.selected_ROI_spectrum["gray"].channel["B"].spectra["raw-dn-val"]) 
        self.graph_distributive_dn["blu_obje"].setData(self.selected_ROI_spectrum["obje"].channel["B"].spectra["wavelength"], self.selected_ROI_spectrum["obje"].channel["B"].spectra["raw-dn-val"]) 




    def handle_when_tw_midcol_changed(self) -> None:
        # remove all items 
        for x in [self.roi_obje_main, self.roi_gray_main, self.roi_wave759nm, self.roi_label_obje, self.roi_label_gray, self.roi_bgle, self.roi_bgri]:
            if x in self.ui.graph_2dimg.getView().addedItems:
                _ = self.ui.graph_2dimg.getView().removeItem(x)

        # add items based on which is on 
        if self.ui.tw_midcol.currentIndex() == 0:
            _ = self.ui.graph_2dimg.getView().addItem(self.roi_wave759nm)
        elif self.ui.tw_midcol.currentIndex() == 1:
            _ = self.ui.graph_2dimg.getView().addItem(self.roi_bgle)
            _ = self.ui.graph_2dimg.getView().addItem(self.roi_bgri)

        elif self.ui.tw_midcol.currentIndex() == 2:
            _ = self.ui.graph_2dimg.getView().addItem(self.roi_obje_main)
            _ = self.ui.graph_2dimg.getView().addItem(self.roi_gray_main)
            _ = self.ui.graph_2dimg.getView().addItem(self.roi_label_obje)
            _ = self.ui.graph_2dimg.getView().addItem(self.roi_label_gray)

    def handle_when_to_show_calibrated_wavelenghts(self) -> None:
        for prms, x in self.graph_2dimg_wave_curves.values():
            if self.ui.cb_shows_calibrated_wl.isChecked():
                if x not in self.ui.graph_2dimg.getView().addedItems:
                    _ = self.ui.graph_2dimg.getView().addItem(x)
                x.setData(
                    quadratic_func(np.arange(0, 2464, 1), *prms),
                    np.arange(0, 2464, 1),
                )
            else:
                if x in self.ui.graph_2dimg.getView().addedItems:
                    _ = self.ui.graph_2dimg.getView().removeItem(x)

    def handle_when_stages_changes(self, stages: int=0) -> None:
        print(stages)
        tmp0 = (
            (3, 1, 3, 1, 3, 0, 0, 0, 0),
            (0, 0, 0, 0, 3, 1, 3, 0, 0),
            (0, 0, 0, 0, 0, 0, 3, 1, 3), # TODO
            (0, 0, 0, 0, 0, 0, 3, 1, 3),
        )

        x = (self.ui.gb_panel_00_file, self.ui.gp_panel_05_jpeg_load,
             self.ui.gp_panel_10_rawbayer, self.ui.gp_panel_15_roiselect,
             self.ui.gp_panel_20_3roi_dist, self.ui.gp_panel_25_savgol,
             self.ui.gp_panel_30_rgb_curves, self.ui.gp_panel_35_refl_calculate,
             self.ui.gp_panel_40_3refl_to_1refl)

        for ith, gb in enumerate(x):
            if tmp0[stages][ith] != 0:
                gb.show()
            else:
                gb.hide()


    def dir_searching_based_regex(self) -> None:
        current_search_prompt = self.ui.le_tv_name_narrower.text()
        if current_search_prompt == "":
            self.fsmodel.setFilter(QDir.Filter.Files |  QDir.Filter.AllDirs|  QDir.Filter.NoDotAndDotDot)
            self.fsmodel.setNameFilters((["*.jpeg"]))
            self.fsmodel.setNameFilterDisables(True)
        else:
            self.fsmodel.setFilter(QDir.Filter.Files |  QDir.Filter.Dirs|  QDir.Filter.NoDotAndDotDot)
            self.fsmodel.setNameFilters((["*" + current_search_prompt.replace(" ", "*") + "*"]))
            self.fsmodel.setNameFilterDisables(False)

    def init_2d_graph_hide_the_original_roi_buttons(self) -> None:
        """Hides the ROI/Menu buttons from the 3 images"""
        self.ui.graph_2dimg.ui.roiBtn.hide()
        self.ui.graph_2dimg.ui.menuBtn.hide()

    def init_all_6_roi(self) -> None:
        _ = self.roi_obje_main.addScaleHandle([0.5, 1], [0.5, 0])
        _ = self.roi_gray_main.addScaleHandle([0.5, 1], [0.5, 0])
        _ = self.roi_wave759nm.addScaleHandle([0.5, 1], [0.5, 0])
        _ = self.roi_wave759nm.addScaleHandle([1, 0.5], [0, 0.5])

        self.roi_bgle.addScaleHandle([0.5, 1], [0.5, 0])
        self.roi_bgle.addScaleHandle([0.5, 0], [0.5, 1])
        self.roi_bgle.addScaleHandle([1, 0.5], [0, 0.5])
        self.roi_bgle.addScaleHandle([0, 0.5], [1, 0.5])

        self.roi_bgri.addScaleHandle([0.5, 1], [0.5, 0])
        self.roi_bgri.addScaleHandle([0.5, 0], [0.5, 1])
        self.roi_bgri.addScaleHandle([1, 0.5], [0, 0.5])
        self.roi_bgri.addScaleHandle([0, 0.5], [1, 0.5])

        self.roi_obje_main.setZValue(10)
        self.roi_gray_main.setZValue(10)
        self.roi_wave759nm.setZValue(10)

    def init_sb_signals_for_ROI_controls(self) -> None:
        _ = self.ui.sb_gray_posy.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_gray_sizy.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_obje_posy.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_obje_sizy.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_midx_init.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_midx_size.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_roi759_posx.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_roi759_posy.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_roi759_sizx.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_roi759_sizy.valueChanged.connect(self.update_raw_from_sb)

        _ = self.ui.sb_bgle_posx.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_bg___posy.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_bgle_sizx.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_bg___sizy.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_bgri_posx.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_bgri_sizx.valueChanged.connect(self.update_raw_from_sb)

        _ = self.ui.sb_waveperpixel.valueChanged.connect(self.update_raw_roi_plot_when_sb_or_roi_moved)

        _ = self.roi_gray_main.sigRegionChanged.connect(lambda: self.handle_roi_change("gray"))
        _ = self.roi_obje_main.sigRegionChanged.connect(lambda: self.handle_roi_change("obje"))
        _ = self.roi_wave759nm.sigRegionChanged.connect(lambda: self.handle_roi_change("wave-759"))
        _ = self.ui.cb_759_channel.currentIndexChanged.connect(lambda: self.handle_roi_change("wave-759"))
        _ = self.roi_bgle.sigRegionChanged.connect(lambda: self.handle_roi_change("bg-left"))
        _ = self.roi_bgri.sigRegionChanged.connect(lambda: self.handle_roi_change("bg-right"))

        _ = self.ui.pb_wave_calib.clicked.connect(self.callback_wavelength_calibration)
        _ = self.ui.pb_bg_calc.clicked.connect(self.callback_bg_estimation)


    def init_all_pyqtgraph(self) -> None:
        # --------graph 4:  rgb refl  ---------------------------------------------------------------------
        _ = self.ui.graph_calc4_refl_rgb.getPlotItem().addLegend()
        self.ui.graph_calc4_refl_rgb.getPlotItem().addItem(
            pg.InfiniteLine(
                pos=759.37 / 10**9,
                movable=False, angle=90,
                label="x={value:0.2f}nm",
                labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True}))

        self.ui.graph_calc4_refl_rgb.getPlotItem().setLabel("left",   "Reflection")
        self.ui.graph_calc4_refl_rgb.getPlotItem().setLabel("bottom", "Wavelength", units="m")
        self.ui.graph_calc4_refl_rgb.getPlotItem().setTitle("Reflection RGB 3 channels")

        # --
        self.ui.graph_gray2white.getPlotItem().setLabel("left", "Ratio")
        self.ui.graph_gray2white.getPlotItem().setLabel("bottom", "Wavelength", units="m")
        self.ui.graph_gray2white.getPlotItem().setTitle("White / Gray")
        _ = self.ui.graph_gray2white.getPlotItem().addLegend()

        # --------graph 5:  rgb     ---------------------------------------------------------------------
        self.ui.graph_calc5_refl_final.getPlotItem().setLabel("left", "Reflection")
        self.ui.graph_calc5_refl_final.getPlotItem().setLabel("bottom", "Wavelength", units="m")
        self.ui.graph_calc5_refl_final.getPlotItem().setTitle("Reflection")

        self.ui.graph_calc5_refl_final.getPlotItem().addItem(self.graph5_norm_one_line)
        self.ui.graph_calc5_refl_final.getPlotItem().addItem(self.graph5_norm_zero_line)
        _ = self.ui.graph_calc5_refl_final.getPlotItem().addLegend()

    def spinbox_setvalue_without_emitting_signal(self, sb: QSpinBox, value: int) -> None:
        """Sets QSpinBox widgets value without signal emitting"""
        _ = sb.blockSignals(True)
        sb.setValue(value)
        _ = sb.blockSignals(False)

    def handle_roi_change(self, roi_label: str) -> None:
        if roi_label == "gray":
            gray_posx, gray_posy, gray_sizx, gray_sizy = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_gray_main.getState())
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_midx_init, gray_posx)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_midx_size, gray_sizx)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_gray_posy, gray_posy)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_gray_sizy, gray_sizy)

        elif roi_label == "obje":
            obje_posx, obje_posy, obje_sizx, obje_sizy = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_obje_main.getState())
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_midx_init, obje_posx)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_midx_size, obje_sizx)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_obje_posy, obje_posy)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_obje_sizy, obje_sizy)

        elif roi_label == "wave-759":
            w759_posx, w759_posy, w759_sizx, w759_sizy = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_wave759nm.getState())
            # changing the spinbox
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_roi759_posx, w759_posx)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_roi759_posy, w759_posy)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_roi759_sizx, w759_sizx)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_roi759_sizy, w759_sizy)

            #self.jp.wavelength_array_2464x3280(self.graph_2dimg_wave_curves["759.37"][0], self.ui.sb_waveperpixel.value()) #this ?

        elif roi_label == "bg-left":
            bgle_posx, bgle_posy, bgle_sizx, bgle_sizy = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_bgle.getState())
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_bgle_posx, bgle_posx)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_bgle_sizx, bgle_sizx)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_bg___posy, bgle_posy)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_bg___sizy, bgle_sizy)

        elif roi_label == "bg-right":
            bgri_posx, bgri_posy, bgri_sizx, bgri_sizy = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_bgri.getState())
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_bgri_posx, bgri_posx)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_bgri_sizx, bgri_sizx)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_bg___posy, bgri_posy)
            self.spinbox_setvalue_without_emitting_signal(self.ui.sb_bg___sizy, bgri_sizy)

        self.update_raw_from_sb()

    def get_posx_posy_sizex_sizy_cleaner_carefuler_way(self, tmp_roi_state: dict[str, pg.Point|float]) -> tuple[int, int, int, int]:
        assert ("pos" in tmp_roi_state) and ("size" in tmp_roi_state), "Err while returning roi"
        tmp_roi_pos = tmp_roi_state["pos"]
        tmp_roi_size = tmp_roi_state["size"]
        assert isinstance(tmp_roi_pos, QPointF) and isinstance(tmp_roi_size, QPointF), "Err while returning self.roi_gray_main.getState()"

        return int(tmp_roi_pos.x()), int(tmp_roi_pos.y()), int(tmp_roi_size.x()), int(tmp_roi_size.y())


    def update_raw_from_sb(self) -> None:
        _ = self.roi_gray_main.blockSignals(True)
        _ = self.roi_obje_main.blockSignals(True)
        _ = self.roi_wave759nm.blockSignals(True)
        _ = self.roi_bgle.blockSignals(True)
        _ = self.roi_bgri.blockSignals(True)

        self.roi_gray_main.setPos(self.ui.sb_midx_init.value(), self.ui.sb_gray_posy.value())
        self.roi_gray_main.setSize((self.ui.sb_midx_size.value(), self.ui.sb_gray_sizy.value()))

        self.roi_obje_main.setPos(self.ui.sb_midx_init.value(), self.ui.sb_obje_posy.value())
        self.roi_obje_main.setSize((self.ui.sb_midx_size.value(), self.ui.sb_obje_sizy.value()))

        self.roi_wave759nm.setPos(self.ui.sb_roi759_posx.value(), self.ui.sb_roi759_posy.value())
        self.roi_wave759nm.setSize((self.ui.sb_roi759_sizx.value(), self.ui.sb_roi759_sizy.value()))

        self.roi_bgle.setPos(self.ui.sb_bgle_posx.value(), self.ui.sb_bg___posy.value())
        self.roi_bgle.setSize((self.ui.sb_bgle_sizx.value(), self.ui.sb_bg___sizy.value()))

        self.roi_bgri.setPos(self.ui.sb_bgri_posx.value(), self.ui.sb_bg___posy.value())
        self.roi_bgri.setSize((self.ui.sb_bgri_sizx.value(), self.ui.sb_bg___sizy.value()))

        _ = self.roi_gray_main.blockSignals(False)
        _ = self.roi_obje_main.blockSignals(False)
        _ = self.roi_wave759nm.blockSignals(False)
        _ = self.roi_bgle.blockSignals(False)
        _ = self.roi_bgri.blockSignals(False)

        # change the label position
        self.roi_label_gray.setPos(self.ui.sb_midx_init.value(), self.ui.sb_gray_posy.value())
        self.roi_label_obje.setPos(self.ui.sb_midx_init.value(), self.ui.sb_obje_posy.value())

        self.update_raw_roi_plot_when_sb_or_roi_moved()
        self.update_759roi_when_sb_or_roi_moved()


        if not self.paramsChangingFromHistory:
            self.ui.cb_parameter_history.setCurrentIndex(0) # when change happens make it current


        self.update_fov_on_webcam()

    def update_fov_on_webcam(self) -> None:
        self.ui.l_target_distance.setText(f"Distance: {self.ui.hs_target_distance.value()}cm")
        fov_pw1 = pxlspec_to_pxlweb_formula(self.ui.hs_target_distance.value(), self.ui.sb_obje_posy.value())
        fov_pw2 = pxlspec_to_pxlweb_formula(self.ui.hs_target_distance.value(), self.ui.sb_obje_posy.value() + self.ui.sb_obje_sizy.value())
        self.roi_webcam_fov.setPos((310, fov_pw1))
        self.roi_webcam_fov.setSize((20, fov_pw2-fov_pw1))


    def update_raw_roi_plot_when_sb_or_roi_moved(self) -> None:
        gray_roi_pxl = (self.ui.sb_midx_init.value(), self.ui.sb_gray_posy.value(), self.ui.sb_midx_size.value(), self.ui.sb_gray_sizy.value())
        obje_roi_pxl = (self.ui.sb_midx_init.value(), self.ui.sb_obje_posy.value(), self.ui.sb_midx_size.value(), self.ui.sb_obje_sizy.value())

        self.graph_raw_lines["gray_r"].setData(self.jp.get_array("Wavelength", "Mask red",   gray_roi_pxl), self.jp.get_array("Raw bayer", "Mask red",   gray_roi_pxl)) 
        self.graph_raw_lines["gray_g"].setData(self.jp.get_array("Wavelength", "Mask green", gray_roi_pxl), self.jp.get_array("Raw bayer", "Mask green", gray_roi_pxl)) 
        self.graph_raw_lines["gray_b"].setData(self.jp.get_array("Wavelength", "Mask blue",  gray_roi_pxl), self.jp.get_array("Raw bayer", "Mask blue",  gray_roi_pxl)) 

        self.graph_raw_lines["obje_r"].setData(self.jp.get_array("Wavelength", "Mask red",   obje_roi_pxl), self.jp.get_array("Raw bayer", "Mask red",   obje_roi_pxl)) 
        self.graph_raw_lines["obje_g"].setData(self.jp.get_array("Wavelength", "Mask green", obje_roi_pxl), self.jp.get_array("Raw bayer", "Mask green", obje_roi_pxl)) 
        self.graph_raw_lines["obje_b"].setData(self.jp.get_array("Wavelength", "Mask blue",  obje_roi_pxl), self.jp.get_array("Raw bayer", "Mask blue",  obje_roi_pxl)) 


    def update_759roi_when_sb_or_roi_moved(self) -> None:
        w759_posx, w759_posy, w759_sizx, w759_sizy = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_wave759nm.getState())
        # changing the image
        init_ax0, init_ax1 = 1, 1
        if self.ui.cb_759_channel.currentText() == "red":
            init_ax0, init_ax1 = 1, 1
            self.ui.graph_759_roi.setColorMap(pg.colormap.get("CET-L13"))
        elif self.ui.cb_759_channel.currentText() == "green":
            init_ax0, init_ax1 = 0, 1
            self.ui.graph_759_roi.setColorMap(pg.colormap.get("CET-L14"))
        elif self.ui.cb_759_channel.currentText() == "green2":
            init_ax0, init_ax1 = 1, 0
            self.ui.graph_759_roi.setColorMap(pg.colormap.get("CET-L14"))
        elif self.ui.cb_759_channel.currentText() == "blue":
            init_ax0, init_ax1 = 0, 0
            self.ui.graph_759_roi.setColorMap(pg.colormap.get("CET-L15"))

        self.arr_759_roi: NDArray[np.uint16] = self.jp.arr["Raw bayer (Noise Filter)"][ # TODO use the get_array function later
            w759_posy + init_ax0 : w759_posy + w759_sizy+ init_ax0 : 2,
            w759_posx + init_ax1 : w759_posx + w759_sizx+ init_ax1 : 2,
        ].astype(np.uint16)
        self.arr_759_roi = cast(np.ndarray[tuple[int, int], np.dtype[np.uint16]], self.arr_759_roi)
        # self.arr_759_roi = sig.medfilt(self.arr_759_roi, kernel_size=(1, 3))
        self.ui.graph_759_roi.setImage(self.arr_759_roi, axes={"x":1, "y":0}, levelMode = "mono")
        self.ui.graph_759_plot.clear()
        self.ui.graph_759_plot_fit.clear()

        for k in self.graph_2dimg_wave_curves:
            self.graph_2dimg_wave_curves[k][0][0] = w759_posx + (float(k) - 759.37) / (self.ui.sb_waveperpixel.value() / 2)
            self.graph_2dimg_wave_curves[k][0][1] = 0
            self.graph_2dimg_wave_curves[k][0][2] = 0


    def callback_wavelength_calibration(self) -> None:
        # assume the self.arr_759_roi has already prepped (and median filtered)
        cm = pg.colormap.get("turbo")
        clrs = cm.map(np.linspace(0, 1, self.arr_759_roi.shape[0]))
        print(clrs, type(clrs))

        tmp_near_pix = np.argmin(self.arr_759_roi, axis=1)
        tmp_near_pix_subpix = np.zeros_like(tmp_near_pix, dtype=np.float64)

        #np.save(f"/tmp/near.npy", self.arr_759_roi)
        self.ui.graph_759_plot.getPlotItem().clear()
        self.ui.pbar_759_rows.setMaximum(self.arr_759_roi.shape[0])

        tmpx = np.arange(self.ui.sb_roi759_posx.value(), self.ui.sb_roi759_posx.value() + self.ui.sb_roi759_sizx.value(), 2) # TODO depend on the channel
        tmpy = np.arange(self.ui.sb_roi759_posy.value(), self.ui.sb_roi759_posy.value() + self.ui.sb_roi759_sizy.value(), 2) # TODO depend on the channel
 
        for i in range(self.arr_759_roi.shape[0]):
            self.ui.pbar_759_rows.setValue(i)
            #self.ui.pbar_759_rows.setPalette(QColor(clrs[i,0], clrs[i,1], clrs[i,2], clrs[i,3]))

            z759 = np.polyfit(tmpx, self.arr_759_roi[i, :], 8)
            p759 = np.poly1d(z759)

            tmp_x_759_near_on_index = np.linspace(
                self.ui.sb_roi759_posx.value(),
                self.ui.sb_roi759_posx.value() + self.ui.sb_roi759_sizx.value(),
                1000,
                dtype=np.float64
            )
            tmp_fitted_curve_aroudnd_759 = p759(tmp_x_759_near_on_index)

            _ = self.ui.graph_759_plot.getPlotItem().plot(
                tmp_x_759_near_on_index,
                tmp_fitted_curve_aroudnd_759,
                pen=pg.mkPen(clrs[i], width=1, style=Qt.PenStyle.SolidLine)
            )

            tmp_local_min = tmp_x_759_near_on_index[sig.argrelextrema(tmp_fitted_curve_aroudnd_759, np.less_equal)]
            print(i, tmp_local_min)
            #nearest_for = np.argmin(np.abs(tmp_local_min - tmp_near_pix[i]))
            nearest_for = np.argmin(np.abs(tmp_local_min - (tmp_near_pix[i]*2 + self.ui.sb_roi759_posx.value())))
            print(i, tmp_local_min, nearest_for)
            tmp_local_min = tmp_local_min[nearest_for]
            tmp_near_pix_subpix[i] = tmp_local_min

            _ = self.ui.graph_759_plot.getPlotItem().addItem(
                pg.InfiniteLine(
                    pos=tmp_near_pix_subpix[i],
                    movable=False, angle=90,
                    pen=pg.mkPen(clrs[i], width=1, style=Qt.PenStyle.SolidLine))
            )
            QApplication.processEvents() # update the each


        self.ui.graph_759_plot_fit.getPlotItem().clear()

        _ = self.ui.graph_759_plot_fit.getPlotItem().plot(
            tmp_near_pix_subpix,
            tmpy,
            symbol="o",
            symbolSize=9,
            symbolBrush=clrs,
            pen=None,
            name="R-obje-left"
        )
        self.params_fit759, _ = curve_fit(
            quadratic_func,
            xdata=tmpy.astype(np.float64), 
            ydata=tmp_near_pix_subpix,
        )
        print(self.params_fit759)

        _ = self.ui.graph_759_plot_fit.getPlotItem().plot(
            quadratic_func(np.arange(0, 2464, 1, dtype=np.float64), *self.params_fit759),
            np.arange(0, 2464, 1),
        )


        for k in self.graph_2dimg_wave_curves:
            self.graph_2dimg_wave_curves[k][0][0] = self.params_fit759[0] + (float(k) - 759.37) / ( self.ui.sb_waveperpixel.value() / 2 )
            self.graph_2dimg_wave_curves[k][0][1] = self.params_fit759[1]
            self.graph_2dimg_wave_curves[k][0][2] = self.params_fit759[2]

        #self.wv[:, :] = wavelength_array_2464x3280(self.params_fit759, self.ui.sb_waveperpixel.value())

        self.jp.wavelength_array_2464x3280(self.params_fit759, self.ui.sb_waveperpixel.value())
        #self.iso.setData(self.wv)
        #np.save("/tmp/wv.npy", self.wv)

    def callback_bg_estimation(self) -> None:
        cm = pg.colormap.get("turbo")
        clrs = cm.map(np.linspace(0, 1, self.ui.sb_bg___sizy.value()))

        self.ui.graph_bg_r.getPlotItem().clear()
        self.ui.graph_bg_g.getPlotItem().clear()
        self.ui.graph_bg_b.getPlotItem().clear()

        self.ui.pbar_bg_on_row.setMaximum(self.ui.sb_bg___sizy.value()//2)
        
        bgle_roi_pxl = (self.ui.sb_bgle_posx.value(), self.ui.sb_bg___posy.value(), self.ui.sb_bgle_sizx.value(), self.ui.sb_bg___sizy.value())
        bgri_roi_pxl = (self.ui.sb_bgri_posx.value(), self.ui.sb_bg___posy.value(), self.ui.sb_bgri_sizx.value(), self.ui.sb_bg___sizy.value())
        
        _ = self.ui.graph_bg_r.getPlotItem().plot(self.jp.get_array("x_pxl", "Mask red",   bgle_roi_pxl), self.jp.get_array("Raw bayer", "Mask red",   bgle_roi_pxl), pen=None, symbol='o', symbolPen=None, symbolSize=3)
        _ = self.ui.graph_bg_g.getPlotItem().plot(self.jp.get_array("x_pxl", "Mask green", bgle_roi_pxl), self.jp.get_array("Raw bayer", "Mask green", bgle_roi_pxl), pen=None, symbol='o', symbolPen=None, symbolSize=3)
        _ = self.ui.graph_bg_b.getPlotItem().plot(self.jp.get_array("x_pxl", "Mask blue",  bgle_roi_pxl), self.jp.get_array("Raw bayer", "Mask blue",  bgle_roi_pxl), pen=None, symbol='o', symbolPen=None, symbolSize=3)

        _ = self.ui.graph_bg_r.getPlotItem().plot(self.jp.get_array("x_pxl", "Mask red",   bgri_roi_pxl), self.jp.get_array("Raw bayer", "Mask red",   bgri_roi_pxl), pen=None, symbol='x', symbolPen=None, symbolSize=3)
        _ = self.ui.graph_bg_g.getPlotItem().plot(self.jp.get_array("x_pxl", "Mask green", bgri_roi_pxl), self.jp.get_array("Raw bayer", "Mask green", bgri_roi_pxl), pen=None, symbol='x', symbolPen=None, symbolSize=3)
        _ = self.ui.graph_bg_b.getPlotItem().plot(self.jp.get_array("x_pxl", "Mask blue",  bgri_roi_pxl), self.jp.get_array("Raw bayer", "Mask blue",  bgri_roi_pxl), pen=None, symbol='x', symbolPen=None, symbolSize=3)

        self.jp.bg_pre_estimation_prep(bgle_roi_pxl, bgri_roi_pxl)

        tmp_x = np.arange(self.ui.sb_bgle_posx.value(),  self.ui.sb_bgri_posx.value() + self.ui.sb_bgri_sizx.value(), dtype=np.float64)

        for rel_y_pxl in range(self.ui.sb_bg___sizy.value()):
            self.ui.pbar_bg_on_row.setValue(rel_y_pxl)
            py = self.ui.sb_bg___posy.value() + rel_y_pxl
            self.jp.bg_curve_fit_on_any_row_any_channel(py)

            _ = self.ui.graph_bg_r.getPlotItem().plot(tmp_x, background_new(tmp_x, *self.jp.bg_popts["r"][py, :]), pen=pg.mkPen(clrs[rel_y_pxl], width=1, style=Qt.PenStyle.SolidLine))
            _ = self.ui.graph_bg_g.getPlotItem().plot(tmp_x, background_new(tmp_x, *self.jp.bg_popts["g"][py, :]), pen=pg.mkPen(clrs[rel_y_pxl], width=1, style=Qt.PenStyle.SolidLine))
            _ = self.ui.graph_bg_b.getPlotItem().plot(tmp_x, background_new(tmp_x, *self.jp.bg_popts["b"][py, :]), pen=pg.mkPen(clrs[rel_y_pxl], width=1, style=Qt.PenStyle.SolidLine))
            QApplication.processEvents()


    def handle_cb_calc5_norming(self) -> None:
        # print("i was clicked")
        self.ui.sb_calc5_norm_zero.setEnabled(self.ui.cb_calc5_norm.isChecked())
        self.ui.sb_calc5_norm_one.setEnabled(self.ui.cb_calc5_norm.isChecked())
        try:
            pass
            # self.call_calibrate_and_calculate_calc5_refl_n_norm()
            # TODO where I should put Normalization
        except Exception as e:
            print(e)

    def callback_savgol(self) -> None:
        wv0, wv1, wv_num = self.ui.sb_savgol_wv0.value(), self.ui.sb_savgol_wv1.value(), self.ui.sb_savgol_wv_num.value()
        window_width = self.ui.sb_savgol_poly_wv_window.value()
        #fullwave = np.linspace(wv0, wv1, wv_num, dtype=np.float64) # should be the putoutpu wavelength

        self.ui.pbar_savgol_channel.setMaximum(3)
        self.ui.pbar_savgol_iteration.setMaximum(wv_num)

        self.selected_ROI_spectrum["gray"].channel["R"].savgol_init(wv0, wv1, wv_num, window_width, poly_deg =5)
        self.selected_ROI_spectrum["gray"].channel["G"].savgol_init(wv0, wv1, wv_num, window_width, poly_deg =5)
        self.selected_ROI_spectrum["gray"].channel["B"].savgol_init(wv0, wv1, wv_num, window_width, poly_deg =5)
        self.selected_ROI_spectrum["obje"].channel["R"].savgol_init(wv0, wv1, wv_num, window_width, poly_deg =5)
        self.selected_ROI_spectrum["obje"].channel["G"].savgol_init(wv0, wv1, wv_num, window_width, poly_deg =5)
        self.selected_ROI_spectrum["obje"].channel["B"].savgol_init(wv0, wv1, wv_num, window_width, poly_deg =5)
        self.selected_ROI_spectrum["refl"].channel["R"].savgol_init(wv0, wv1, wv_num, window_width, poly_deg =5)
        self.selected_ROI_spectrum["refl"].channel["G"].savgol_init(wv0, wv1, wv_num, window_width, poly_deg =5)
        self.selected_ROI_spectrum["refl"].channel["B"].savgol_init(wv0, wv1, wv_num, window_width, poly_deg =5)

        for j, rgb_key in enumerate(("R", "G", "B")):
            self.ui.pbar_savgol_channel.setValue(j)

            for i in range(wv_num):
                self.ui.pbar_savgol_iteration.setValue(i+1)
                wndw_wv_g, wndw_ft_g = self.selected_ROI_spectrum["gray"].channel[rgb_key].savgol_calc(i)
                wndw_wv_o, wndw_ft_o = self.selected_ROI_spectrum["obje"].channel[rgb_key].savgol_calc(i)
                self.graph_distributive_dn[rgb_key + "_gray_savgol_ith"].setData(wndw_wv_g, wndw_ft_g)
                self.graph_distributive_dn[rgb_key + "_obje_savgol_ith"].setData(wndw_wv_o, wndw_ft_o)

                self.graph_distributive_dn[rgb_key + "_gray_savgol_curve"].setData(self.selected_ROI_spectrum["gray"].channel[rgb_key].fullwave, self.selected_ROI_spectrum["gray"].channel[rgb_key].savgol_out_curve)
                self.graph_distributive_dn[rgb_key + "_obje_savgol_curve"].setData(self.selected_ROI_spectrum["obje"].channel[rgb_key].fullwave, self.selected_ROI_spectrum["obje"].channel[rgb_key].savgol_out_curve)

                self.graph_curves[f"gray_{rgb_key}_dn_sub_bg"].setData(self.selected_ROI_spectrum["gray"].channel[rgb_key].fullwave, self.selected_ROI_spectrum["gray"].channel[rgb_key].savgol_out_curve)
                self.graph_curves[f"obje_{rgb_key}_dn_sub_bg"].setData(self.selected_ROI_spectrum["obje"].channel[rgb_key].fullwave, self.selected_ROI_spectrum["obje"].channel[rgb_key].savgol_out_curve)

                self.selected_ROI_spectrum["refl"].channel[rgb_key].savgol_out_curve = self.selected_ROI_spectrum["obje"].channel[rgb_key].savgol_out_curve / self.selected_ROI_spectrum["gray"].channel[rgb_key].savgol_out_curve

                self.graph_curves[f"refl_{rgb_key}_dn_sub_bg"].setData(self.selected_ROI_spectrum["refl"].channel[rgb_key].fullwave, self.selected_ROI_spectrum["refl"].channel[rgb_key].savgol_out_curve)


                QApplication.processEvents() # update the each
        self.ui.pbar_savgol_channel.setValue(3)
            

    def init_keyboard_bindings(self) -> None:
        _ = QShortcut(QKeySequence("Ctrl+B"),    self).activated.connect(self.short_cut_goto_parent_dir)
        _ = QShortcut(QKeySequence("Backspace"), self).activated.connect(self.short_cut_goto_parent_dir)
        _ = QShortcut(QKeySequence("Return"),    self).activated.connect(self.short_cut_goto_selected_child_dir)
        _ = QShortcut(QKeySequence("Space"),     self).activated.connect(self.short_cut_preview_raw_jpeg)
        _ = QShortcut(QKeySequence("Ctrl+R"),    self).activated.connect(self.call_calibrate_and_calculate)
        _ = QShortcut(QKeySequence("Ctrl+E"),    self).activated.connect(self.short_cut_export_raw_jpeg)
        _ = QShortcut(QKeySequence("Ctrl+O"),    self).activated.connect(self.short_cut_open_at_point)
        _ = QShortcut(QKeySequence("Ctrl+H"),    self).activated.connect(self.open_help_page)
        _ = QShortcut(QKeySequence("Ctrl+F"),    self).activated.connect(self.ui.cb_ft_filter.toggle)
        _ = QShortcut(QKeySequence("Alt+F"),     self).activated.connect(self.ui.le_tv_name_narrower.setFocus)

    def init_actions(self) -> None:
        _ = self.ui.action_help.triggered.connect(self.open_help_page)
        _ = self.ui.action_dir_goto_cur_child.triggered.connect(self.short_cut_goto_selected_child_dir)
        _ = self.ui.action_dir_goto_parent.triggered.connect(self.short_cut_goto_parent_dir)
        _ = self.ui.action_dir_ft_filter_toggle.triggered.connect(self.ui.cb_ft_filter.toggle)
        _ = self.ui.action_cur_jpeg_export.triggered.connect(self.short_cut_export_raw_jpeg)
        _ = self.ui.action_cur_jpeg_preview.triggered.connect(self.short_cut_preview_raw_jpeg)
        _ = self.ui.action_cur_file_open.triggered.connect(self.short_cut_open_at_point)

    def open_help_page(self) -> None:
        """Opens help page."""
        open_file_externally(self.help_html_path)

    def short_cut_goto_parent_dir(self) -> None:
        """Go to parent directory, Backspace"""
        logger.info("going to parent file")
        cur_root_index = self.ui.tv_dir.rootIndex()  # get .
        parent_of_cur_root_index = self.fsmodel.parent(cur_root_index)  # get ..
        self.ui.tv_dir.setRootIndex(parent_of_cur_root_index)  # set ..
        self.ui.tv_dir.setCurrentIndex(parent_of_cur_root_index)  # idk why this needed
        self.ui.le_tv_name_narrower.setText("") # needed to reset dir filter

    def short_cut_goto_selected_child_dir(self) -> None:
        """Enter: the directory"""
        sel_m_index = self.ui.tv_dir.currentIndex().siblingAtColumn(0)  # get
        if self.fsmodel.hasChildren(sel_m_index):  # enter only if this has children
            self.ui.tv_dir.setRootIndex(sel_m_index) # need if previously other column has selected
        else:
            pass  # need to update jpeg_path here
        self.ui.le_tv_name_narrower.setText("") # needed to reset dir filter

    def short_cut_open_at_point(self) -> None:
        """C-o: opens file externally"""
        sel_m_index = self.ui.tv_dir.currentIndex()
        tmppath = self.fsmodel.filePath(sel_m_index)
        open_file_externally(tmppath)

    def open_directory_at_point(self) -> None:
        """Open current directory"""
        sel_m_index = self.ui.tv_dir.rootIndex()
        tmpdirectory = self.fsmodel.filePath(sel_m_index)
        open_file_externally(tmpdirectory)

    def short_cut_preview_raw_jpeg(self) -> bool:
        """SPC"""
        sel_m_index = self.ui.tv_dir.currentIndex()
        tmppath = self.fsmodel.filePath(sel_m_index)
        basename = os.path.basename(tmppath)
        logger.info("space press "+ tmppath)
        if not os.path.isfile(tmppath):
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Wrong File selected")
            dlg.setText(
                "Selected item is not a file.\n"
                "If this is a folder press ENTER (or double mouseclick)"
                "to enter this folder"
            )
            _ = dlg.exec()
            return False
        if not ((".jpeg" in basename) and (basename.count("_") in (3, 4))):
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Wrong File selected")
            dlg.setText(
                "Selected item is not (JPEG or Directory)\n"
                "Please select JPEG or Directory"
            )
            _ = dlg.exec()
            return False

        self.jpeg_path = tmppath
        self.dir_path = os.path.dirname(self.jpeg_path)
        _ = self.ddtree.set_ddir(self.dir_path)
        self.ui.tb_meta_json.setText(self.ddtree.metajsonText)
        logger.info(f"short_cut_preview_raw_jpeg: {self.ddtree.webcamFP=}")

        webcam: np.ndarray[tuple[int, int, int], np.dtype[np.uint8]] = np.zeros((10, 10, 3), dtype=np.uint8)
        if self.ddtree.webcamFP is not None:
            try:
                tmp = np.asarray(Image.open(self.ddtree.webcamFP), dtype=np.uint8)
                assert tmp.ndim == 3
                webcam = cast(np.ndarray[tuple[int, int, int], np.dtype[np.uint8]], tmp)
                logger.debug(f"short_cut_preview_raw_jpeg: {webcam.dtype=}, {webcam.shape=}")
            except ValueError:
                logger.info(f"PIL-ValueError: while openning {self.ddtree.webcamFP}")
                webcam = np.zeros((10, 10, 3), dtype=np.uint8)
                _ = QMessageBox.warning(self, "file read error", f"{self.ddtree.webcamFP} read Value-error", QMessageBox.StandardButton.Ignore, QMessageBox.StandardButton.Ignore)
            except TypeError:
                logger.info(f"PIL-TypeError: while openning {self.ddtree.webcamFP}")
                webcam = np.zeros((10, 10, 3), dtype=np.uint8)
                _ = QMessageBox.warning(self, "file read error", f"{self.ddtree.webcamFP} read Type-error", QMessageBox.StandardButton.Ignore, QMessageBox.StandardButton.Ignore)
            except Exception as e:
                logger.info(f"PIL-{e}: while openning {self.ddtree.webcamFP}")
                webcam = np.zeros((10, 10, 3), dtype=np.uint8)
                _ = QMessageBox.warning(self, "file read error", f"{self.ddtree.webcamFP} read {e} error", QMessageBox.StandardButton.Ignore, QMessageBox.StandardButton.Ignore)
        else: # webcam image didn't found
            webcam = np.zeros((10, 10, 3), dtype=np.uint8)
            _ = QMessageBox.warning(self, "file not found", "webcam's cam.jpg not found", QMessageBox.StandardButton.Ignore, QMessageBox.StandardButton.Ignore)

        self.ui.graph_webcam.setImage(webcam, axes={"x":1, "y":0, "c":2})

        _ = self.jp.load_jpeg_file(self.jpeg_path)
        self.update_1_rawbayer_img_data_and_then_plot_below()

        # try to reset & repopulate paramHisotry combobox
        self.repopulate_param_history_combobox()
        return True

    def repopulate_param_history_combobox(self) -> None:
        self.paramLogPath = os.path.join(self.ddtree.ddir, "output", "export_log.csv")
        self.dfParamHistory = self.read_param_history_file_and_handle_if_corrupted(self.paramLogPath)
        self.ui.cb_parameter_history.clear()
        self.ui.cb_parameter_history.addItem("Current")
        self.ui.cb_parameter_history.addItems(self.dfParamHistory["date"].astype(str).tolist())

    def call_tv_onItemDoubleClicked(self, v: QModelIndex):
        tmp = self.fsmodel.filePath(v)
        if os.path.isdir(tmp):
            logger.info(f"call_tv_onItemClicked: {tmp}")
            self.short_cut_goto_selected_child_dir()
        else:
            _ = self.short_cut_preview_raw_jpeg()

    def call_calibrate_and_calculate(self) -> None:
        # self.call_calibrate_and_calculate_calc1_desalt()           # TODO
        self.ui.pbar_calc.setValue(0)
        self.ui.tabWidget.setCurrentIndex(0)
        time.sleep(.1)
        # self.call_calibrate_and_calculate_calc2_background()       # TODO
        self.ui.pbar_calc.setValue(25)
        self.ui.tabWidget.setCurrentIndex(1)
        time.sleep(.1)
        #self.call_calibrate_and_calculate_calc3_759_calib()       # TODO
        #self.distribute_pixel_graph()
        self.ui.pbar_calc.setValue(50)
        self.ui.tabWidget.setCurrentIndex(2)
        time.sleep(.1)

        # gray 2 white
        #self.call_calibrate_and_calculate_calc3_759_calib()
        # self.call_calibrate_and_calculate_calc3_5_gray2white() TODO
        self.ui.pbar_calc.setValue(60)
        self.ui.tabWidget.setCurrentIndex(3)
        time.sleep(.1)

        # self.call_calibrate_and_calculate_calc4_rgb_refl() TODO
        self.ui.pbar_calc.setValue(75)
        self.ui.tabWidget.setCurrentIndex(4)
        time.sleep(.1)

        # self.call_calibrate_and_calculate_calc5_refl_n_norm() TODO
        self.ui.pbar_calc.setValue(100)
        self.ui.tabWidget.setCurrentIndex(5)
        time.sleep(.1)

#    def distribute_pixel_graph(self) -> None:
#        gray_roi_pxl = (
#            self.ui.sb_midx_init.value(),
#            self.ui.sb_gray_posy.value(),
#            self.ui.sb_midx_size.value(),
#            self.ui.sb_gray_sizy.value(),
#        )
#
#        obje_roi_pxl = (
#            self.ui.sb_midx_init.value(),
#            self.ui.sb_obje_posy.value(),
#            self.ui.sb_midx_size.value(),
#            self.ui.sb_obje_sizy.value(),
#        )
#        self.graph_distributive_dn["red_gray"].setData(self.jp.get_array("Wavelength", "Mask red",   gray_roi_pxl), self.jp.get_array("Raw bayer", "Mask red",   gray_roi_pxl)) 
#        self.graph_distributive_dn["red_obje"].setData(self.jp.get_array("Wavelength", "Mask red",   obje_roi_pxl), self.jp.get_array("Raw bayer", "Mask red",   obje_roi_pxl)) 
#
#        self.graph_distributive_dn["grn_gray"].setData(self.jp.get_array("Wavelength", "Mask green", gray_roi_pxl), self.jp.get_array("Raw bayer", "Mask green", gray_roi_pxl)) 
#        self.graph_distributive_dn["grn_obje"].setData(self.jp.get_array("Wavelength", "Mask green", obje_roi_pxl), self.jp.get_array("Raw bayer", "Mask green", obje_roi_pxl)) 
#
#        self.graph_distributive_dn["blu_gray"].setData(self.jp.get_array("Wavelength", "Mask blue",  gray_roi_pxl), self.jp.get_array("Raw bayer", "Mask blue",  gray_roi_pxl)) 
#        self.graph_distributive_dn["blu_obje"].setData(self.jp.get_array("Wavelength", "Mask blue",  obje_roi_pxl), self.jp.get_array("Raw bayer", "Mask blue",  obje_roi_pxl)) 



    def update_1_rawbayer_img_data_and_then_plot_below(self) -> None:
        self.ui.graph_2dimg.clear()
        key = self.ui.cb_2dimg_key.currentText()
        assert key in self.jp.arr.keys(), f"bad {key=}"
        self.ui.graph_2dimg.setImage(
            img=self.jp.arr[key].astype(np.float64),
            autoRange=True, #levels=(0, 1024),
            axes={"x":1, "y":0, "c":2} if (self.jp.arr[key].ndim == 3) else {"x":1, "y":0},
            levelMode ="mono", #levelMode ="rgba" if (self.jp.arr[key].ndim == 3) else "mono"
        )
        self.update_raw_from_sb()


    def short_cut_export_raw_jpeg(self) -> None:
        """C-e: export"""
        if not self.short_cut_preview_raw_jpeg():    # checking the selected jpeg
            return

        self.call_calibrate_and_calculate()

        os.makedirs(os.path.join(self.ddtree.ddir, "output"), exist_ok=True)
        #if self.ui.cb_export_bayer_as_npy.isChecked():                          # TODO 2025-05-03
        #    outfname = os.path.join(self.ddtree.ddir, "output", "bayer.npy")
        #    np.save(outfname, self.jp.data)
        self.ui.pbar_export.setValue(25)
        if self.ui.cb_export_bayer_as_mat.isChecked():
            pass
        self.ui.pbar_export.setValue(50)
        #if self.ui.cb_export_ref_CSV_simple.isChecked():                        # TODO 2025-05-03
        #    tmpcsv = np.zeros((1000, 5), dtype=np.float64)
        #    #tmpcsv[:, 0] = self.jp.gray.rchan_759nm_calibrated.index.to_numpy(dtype=np.float64)[-1000:]
        #    tmpcsv[:, 0] = self.jp.gray.itp_hor_nm_array
        #    tmpcsv[:, 1] = self.jp.ref_fancy
        #    tmpcsv[:, 2] = self.jp.ref_fancy_normed if self.ui.cb_calc5_norm.isChecked() else 0
        #    tmpcsv[:, 3] = self.jp.obje_fancy_dn_bg_substracted
        #    tmpcsv[:, 4] = self.jp.gray_fancy_dn_bg_substracted
        #    outfname = os.path.join(os.path.join(self.ddtree.ddir, "output", datetime.now().strftime("refl_output_on_%Y%m%d_%H%M%S.csv")))
        #    logger.debug(f"short_cut_export_raw_jpeg: {outfname=}")
        #    np.savetxt(outfname,
        #               tmpcsv,
        #               ("%3.1f", "%2.5f", "%2.5f", "%3.2f", "%3.2f"),
        #               header=f"wave, refl, refl_norm_{self.ui.sb_calc5_norm_zero.value()}_{self.ui.sb_calc5_norm_one.value()}, DN-obje(bg-substracted), DN-gray(bg-substracted)",
        #               delimiter=",")
        self.ui.pbar_export.setValue(100)

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Exported")
        dlg.setText("Export Finished")
        _ = dlg.exec()

        self.dfParamHistory = pd.concat(
            (
                self.get_current_calculation_parameters_as_pd_df(),
                self.dfParamHistory,
            )
        )
        self.write_export_log_calculation_parameters()
        self.repopulate_param_history_combobox()

        # set to latest history# after exporting finishes
        if (self.dfParamHistory.shape[0] != 0) and (self.ui.cb_parameter_history.count() >= 1):
            # test history isn't empty

            _ = self.ui.cb_parameter_history.blockSignals(True)
            self.ui.cb_parameter_history.setCurrentIndex(1)
            _ = self.ui.cb_parameter_history.blockSignals(False)
            # briefly blocking signal and setting history to last
            # wihtout blokcing singal here, export will
            # self.call_calibrate_and_calculate() twice
            # (once at begining, & then inside of self.ui.cb_parameter_history.setCurrentIndex(1))

    def set_calculation_params_from_history_selection(self) -> None:
        # when cb_parameter_history changes
        selected_hist_date_str = self.ui.cb_parameter_history.currentText()

        logger.debug(f"set_calculation_params_from_history_selection {self.ui.cb_parameter_history.currentText()=}")
        if (selected_hist_date_str == "Current") or (selected_hist_date_str == ""): # it seems when the it's cleared it's running this method
            return

        # in order to not change: self.ui.cb_parameter_history
        self.paramsChangingFromHistory = True

        #tmp = self.dfParamHistory.index[self.dfParamHistory["date"] == selected_hist_date_str]
        selected_row_num = (self.dfParamHistory["date"] == selected_hist_date_str).tolist().index(True)

        self.ui.sb_midx_init.setValue(      self.dfParamHistory["midx_init"].astype(int).iloc[selected_row_num])
        self.ui.sb_midx_size.setValue(      self.dfParamHistory["midx_size"].astype(int).iloc[selected_row_num])
        # self.ui.sb_lefx_init_rel.setValue(  self.dfParamHistory["lefx_init_rel"].astype(int).iloc[selected_row_num])
        # self.ui.sb_lefx_size.setValue(      self.dfParamHistory["lefx_size"].astype(int).iloc[selected_row_num])
        # self.ui.sb_rigx_init_rel.setValue(  self.dfParamHistory["rigx_init_rel"].astype(int).iloc[selected_row_num])
        # self.ui.sb_rigx_size.setValue(      self.dfParamHistory["rigx_size"].astype(int).iloc[selected_row_num])
        self.ui.sb_gray_posy.setValue(    self.dfParamHistory["gray_y_init"].astype(int).iloc[selected_row_num])
        self.ui.sb_gray_sizy.setValue(    self.dfParamHistory["gray_y_size"].astype(int).iloc[selected_row_num])
        self.ui.sb_obje_posy.setValue(    self.dfParamHistory["obje_y_init"].astype(int).iloc[selected_row_num])
        self.ui.sb_obje_sizy.setValue(    self.dfParamHistory["obje_y_size"].astype(int).iloc[selected_row_num])
        _ = self.ui.sb_waveperpixel.blockSignals(True)
        self.ui.sb_waveperpixel.setValue(   self.dfParamHistory["waveperpixel"].astype(int).iloc[selected_row_num])
        _ = self.ui.sb_waveperpixel.blockSignals(False)
        self.ui.cb_calc5_norm.setChecked(   self.dfParamHistory["calc5_norm"].astype(bool).iloc[selected_row_num])
        self.ui.sb_calc5_norm_zero.setValue(self.dfParamHistory["calc5_norm_zero"].astype(int).iloc[selected_row_num])
        self.ui.sb_calc5_norm_one.setValue( self.dfParamHistory["calc5_norm_one"].astype(int).iloc[selected_row_num])

        self.paramsChangingFromHistory = False
        # exporting
        self.call_calibrate_and_calculate()

    def get_current_calculation_parameters_as_pd_df(self) -> pd.DataFrame:
        resultDic = {
            "date"             : [datetime.now().strftime("%Y/%m/%d-%H:%M:%S")],
            "midx_init"        : [self.ui.sb_midx_init.value()],
            "midx_size"        : [700],
            # "lefx_init_rel"    : [self.ui.sb_lefx_init_rel.value()],
            # "lefx_size"        : [self.ui.sb_lefx_size.value()],
            # "rigx_init_rel"    : [self.ui.sb_rigx_init_rel.value()],
            # "rigx_size"        : [self.ui.sb_rigx_size.value()],
            "gray_y_init"      : [self.ui.sb_gray_posy.value()],
            "gray_y_size"      : [self.ui.sb_gray_sizy.value()],
            "obje_y_init"      : [self.ui.sb_obje_posy.value()],
            "obje_y_size"      : [self.ui.sb_obje_sizy.value()],
            "waveperpixel"     : [self.ui.sb_waveperpixel.value()],
            #"calc1_desalt"     : [self.ui.cb_calc1_desalt.isChecked()],
            #"calc2_background" : [self.ui.cb_calc2_background.isChecked()],
            #"calc3_calibrate"  : [self.ui.cb_calc3_calibrate_759.isChecked()],
            "calc5_norm"       : [self.ui.cb_calc5_norm.isChecked()],
            "calc5_norm_zero"  : [self.ui.sb_calc5_norm_zero.value()],
            "calc5_norm_one"   : [self.ui.sb_calc5_norm_one.value()],
        }
        logger.debug(f"get_current_calculation_parameters_as_pd_df: {resultDic=}")
        return pd.DataFrame(resultDic)

    def write_export_log_calculation_parameters(self) -> None:
        os.makedirs(os.path.join(self.ddtree.ddir, "output"), exist_ok=True) # just incase (probably unnecerserly)
        self.dfParamHistory.to_csv(self.paramLogPath, index=False)

    def check_export_log_pandas_has_correct_format(self, df: pd.DataFrame) -> bool:
        if ("date"             not in df.columns or
            "midx_init"        not in df.columns or
            "midx_size"        not in df.columns or
            "lefx_init_rel"    not in df.columns or
            "lefx_size"        not in df.columns or
            "rigx_init_rel"    not in df.columns or
            "rigx_size"        not in df.columns or
            "gray_y_init"      not in df.columns or
            "gray_y_size"      not in df.columns or
            "obje_y_init"      not in df.columns or
            "obje_y_size"      not in df.columns or
            "waveperpixel"     not in df.columns or
            "calc1_desalt"     not in df.columns or
            "calc2_background" not in df.columns or
            "calc3_calibrate"  not in df.columns or
            "calc5_norm"       not in df.columns or
            "calc5_norm_zero"  not in df.columns or
            "calc5_norm_one"   not in df.columns):
            #print("some column missing")
            return False

        if (df["date"].dtype              != np.dtype("O") or
            df["midx_init"].dtype         not in (np.dtype("int64"), np.dtype("int32")) or
            df["midx_size"].dtype         not in (np.dtype("int64"), np.dtype("int32")) or
            df["lefx_init_rel"].dtype     not in (np.dtype("int64"), np.dtype("int32")) or
            df["lefx_size"].dtype         not in (np.dtype("int64"), np.dtype("int32")) or
            df["rigx_init_rel"].dtype     not in (np.dtype("int64"), np.dtype("int32")) or
            df["rigx_size"].dtype         not in (np.dtype("int64"), np.dtype("int32")) or
            df["gray_y_init"].dtype       not in (np.dtype("int64"), np.dtype("int32")) or
            df["gray_y_size"].dtype       not in (np.dtype("int64"), np.dtype("int32")) or
            df["obje_y_init"].dtype       not in (np.dtype("int64"), np.dtype("int32")) or
            df["obje_y_size"].dtype       not in (np.dtype("int64"), np.dtype("int32")) or
            df["waveperpixel"].dtype      not in (np.dtype("float64"), np.dtype("float32")) or
            df["calc1_desalt"].dtype      != np.dtype("bool") or
            df["calc2_background"].dtype  != np.dtype("bool") or
            df["calc3_calibrate"].dtype   != np.dtype("bool") or
            df["calc5_norm"].dtype        != np.dtype("bool") or
            df["calc5_norm_zero"].dtype   not in (np.dtype("float64"), np.dtype("float32")) or
            df["calc5_norm_one"].dtype    not in (np.dtype("float64"), np.dtype("float32"))):
            # print(f"df history bad csv column type: {df.dtypes=}")
            logger.info(f"DF param-history bad csv column type: {df=}")
            return False

        return True

    def read_param_history_file_and_handle_if_corrupted(self, path: str) -> pd.DataFrame:
        # reads csv file @ path and returns corect DF
        # if corrupted saves old file
        if not os.path.isfile(path):
            return self.create_empty_param_history_pd_df()

        # try to read pandas csv
        try:
            result = pd.read_csv(path)
        except Exception:
            # make copy of old corrupted csv file
            _ = shutil.copyfile(path, f"{path}.corrupted_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
            return self.create_empty_param_history_pd_df()

        if self.check_export_log_pandas_has_correct_format(result):
            return result
        else:
            # make copy of old corrupted csv file
            _ = shutil.copyfile(path, f"{path}.corrupted_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
            # returns empty dataframe
            return self.create_empty_param_history_pd_df()

    def create_empty_param_history_pd_df(self) -> pd.DataFrame:
        return pd.DataFrame(
            columns=["date", "midx_init", "midx_size", "lefx_init_rel", "lefx_size", "rigx_init_rel", "rigx_size",
                     "gray_y_init", "gray_y_size", "obje_y_init", "obje_y_size", "waveperpixel", "calc1_desalt", "calc2_background",
                     "calc3_calibrate", "calc5_norm", "calc5_norm_zero", "calc5_norm_one",]
        )


    def init_physical_repr_graph(self) -> None:
        v = self.ui.graph_physical_orientation.ci.addViewBox()
        v.setAspectLocked()
        v.addItem(self.graph_physical_spectrometer_shape)
        v.addItem(self.graph_physical_vfov_ground_projection_shape)
        self.update_physical_graph()

    def update_physical_graph(self) -> None:
        rad_elv:float = np.radians(self.ui.hs_physical_elv.value())
        rot_mat = np.array([
            [np.cos(rad_elv), -np.sin(rad_elv)],
            [np.sin(rad_elv),  np.cos(rad_elv)],
        ])
        d: float = self.ui.hs_physical_height.value() / np.sin(- rad_elv)

        self.graph_physical_spectrometer_shape.setData(
            pos=(rot_mat @ self.graph_physical_spectrometer_shape_vertex.T).T,
            adj=self.graph_physical_spectrometer_shape_edges,
            pen=self.graph_physical_spectrometer_shape_edges_colors,
            size=0,
            pxMode=False,
        )

        self.graph_physical_vfov_ground_proj_vertex = np.array(
            [ [0.0,   0.0],  # 0
              [0,   -self.ui.hs_physical_height.value()],  # 1
              [self.ui.hs_physical_height.value()* math.tan(math.pi/2 + math.radians(self.ui.hs_physical_elv.value() -1.85)),   -self.ui.hs_physical_height.value()],  # 2
              [self.ui.hs_physical_height.value()* math.tan(math.pi/2 + math.radians(self.ui.hs_physical_elv.value()      )),   -self.ui.hs_physical_height.value()],  # 3
              [self.ui.hs_physical_height.value()* math.tan(math.pi/2 + math.radians(self.ui.hs_physical_elv.value() +5.61)),   -self.ui.hs_physical_height.value()],  # 4
            ]
        )

        self.graph_physical_vfov_ground_projection_shape.setData(
            pos=self.graph_physical_vfov_ground_proj_vertex,
            adj=self.graph_physical_vfov_ground_proj_edges,
            pen=self.graph_physical_vfov_ground_proj_edges_colors,
            size=0,
            pxMode=False,
        )

        self.ui.l_physical_elv.setText(f"Pitch: {self.ui.hs_physical_elv.value()}deg")
        self.ui.l_physical_height.setText(f"Height: {self.ui.hs_physical_height.value()}cm")
        self.ui.l_physical_distance.setText(f"Distance: {d:.1f}cm")

        # controll the other tab
        # self.ui.hs_target_distance.setValue(d)
        self.ui.hs_target_distance.setValue(int(d))
