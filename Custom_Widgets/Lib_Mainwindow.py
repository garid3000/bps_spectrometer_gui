# ---------- Base libraries -------------------------------------------------------------------------------------------
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

# ---------- GUI libraries --------------------------------------------------------------------------------------------
from PySide6.QtWidgets import QMainWindow, QWidget, QFileSystemModel, QMessageBox
from PySide6.QtGui import QKeySequence, QShortcut, QColor
from PySide6.QtCore import QModelIndex, QDir, Qt, QPersistentModelIndex, QPointF, QObject

# ---------- Custom libs ----------------------------------------------------------------------------------------------
from Custom_UIs.UI_Mainwindow import Ui_MainWindow
from Custom_Libs.Lib_DataDirTree import DataDirTree
from bps_raw_jpeg_processer.src.bps_raw_jpeg_processer import JpegProcessor, get_wavelength_array, background

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
        #_ = self.ui.cb_rawbayer_visual_demosiac.valueChanged(self.)
        _ = self.ui.cb_rawbayer_visual_demosiac.stateChanged.connect(self.update_1_rawbayer_img_data_and_then_plot_below)


        # --------------- initialize the file system ----------------------------------
        self.fsmodel = FileSystemModel()                     # prev. QFileSystemModel()
        _ = self.fsmodel.setRootPath(QDir.homePath())

        self.ui.tv_dir.setModel(self.fsmodel)
        self.ui.tv_dir.setRootIndex(self.fsmodel.setRootPath(QDir.homePath()))
        self.short_cut_goto_parent_dir()
        _ = self.ui.tv_dir.doubleClicked.connect(self.call_tv_onItemDoubleClicked)
        # self.ui.cb_ft_filter.stateChanged.connect(self.fsmodel.setNameFilterDisables)
        _ = self.ui.cb_ft_filter.stateChanged.connect(self.toggle_filetype_visiblity)
        _ = self.ui.cb_calc5_norm.stateChanged.connect(self.handle_cb_calc5_norming)
        _ = self.ui.sb_calc5_norm_zero.valueChanged.connect(self.handle_cb_calc5_norming)
        _ = self.ui.sb_calc5_norm_one.valueChanged.connect(self.handle_cb_calc5_norming)
        #self.ui.cb_bayer_show_geometry.stateChanged.connect(self.update_visual_1_rawbayer_img_section)
        _ = self.ui.pb_waveperpixel_reset.clicked.connect(lambda: self.ui.sb_waveperpixel.setValue(1.8385))
        _ = self.ui.pb_system_file_explorer.clicked.connect(self.open_directory_at_point)
        _ = self.ui.le_tv_name_narrower.textChanged.connect(self.dir_searching_based_regex)
        _ = self.ui.cb_parameter_history.currentTextChanged.connect(self.set_calculation_params_from_history_selection)

        _ = self.ui.hs_target_distance.valueChanged.connect(self.update_fov_on_webcam)
        # -----------------------------------------------------------------------------
        #self.jp.set_xWaveRng(self.ui.sb_midx_init.value())
        #self.jp.set_yGrayRng((self.ui.sb_gray_y_init.value(), self.ui.sb_gray_y_init.value() + self.ui.sb_gray_y_size.value())) # noqa
        #self.jp.set_yObjeRng((self.ui.sb_obje_y_init.value(), self.ui.sb_obje_y_init.value() + self.ui.sb_obje_y_size.value())) # noqa
        self.ui.graph_2dimg.getView().invertY(not self.ui.cb_invert_y_axis_of_rawbayer.isChecked())
        _ = self.ui.cb_invert_y_axis_of_rawbayer.stateChanged.connect(
            lambda: self.ui.graph_2dimg.getView().invertY(not self.ui.cb_invert_y_axis_of_rawbayer.isChecked())
        )


        # init_2d_graph_hide_the_original_roi_buttons -----------------------------------------------------------------
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
            pos=[self.ui.sb_midx_init.value(), self.ui.sb_gray_y_init.value()],
            size=pg.Point(700, self.ui.sb_gray_y_size.value()),
            movable=True, scaleSnap=True, snapSize=2, translateSnap=True,
        )

        self.roi_gray_bglf = pg.ROI(
            pos=[self.ui.sb_midx_init.value() + self.ui.sb_lefx_init_rel.value(), self.ui.sb_gray_y_init.value()],
            size=pg.Point(self.ui.sb_lefx_size.value(), self.ui.sb_gray_y_size.value()),
            movable=True, scaleSnap=True, snapSize=2, translateSnap=True,
        )

        self.roi_gray_bgri = pg.ROI(
            pos=[self.ui.sb_midx_init.value() + self.ui.sb_rigx_init_rel.value(), self.ui.sb_gray_y_init.value()],
            size=pg.Point(self.ui.sb_rigx_size.value(), self.ui.sb_gray_y_size.value()),
            movable=True, scaleSnap=True, snapSize=2, translateSnap=True,
        )

        self.roi_obje_main = pg.ROI(
            pos=[self.ui.sb_midx_init.value(), self.ui.sb_obje_y_init.value()],
            size=pg.Point(700, self.ui.sb_obje_y_size.value()),
            movable=True, scaleSnap=True, snapSize=2, translateSnap=True,
        )

        self.roi_obje_bglf = pg.ROI(
            pos=[self.ui.sb_midx_init.value() + self.ui.sb_lefx_init_rel.value(), self.ui.sb_obje_y_init.value()],
            size=pg.Point(self.ui.sb_lefx_size.value(), self.ui.sb_obje_y_size.value()),
            movable=True, scaleSnap=True, snapSize=2, translateSnap=True,
        )

        self.roi_obje_bgri = pg.ROI(
            pos=[self.ui.sb_midx_init.value() + self.ui.sb_rigx_init_rel.value(), self.ui.sb_obje_y_init.value()],
            size=pg.Point(self.ui.sb_rigx_size.value(), self.ui.sb_obje_y_size.value()),
            movable=True, scaleSnap=True, snapSize=2, translateSnap=True,
        )
        # end init_all_6_roi ------------------------------------------------------------------------------------------

        self.graph2_curve_bg_gray_le_r = self.ui.graph_calc2_bg_gray.getPlotItem().plot(symbol="o", symbolSize=9, symbolBrush=(255, 000, 000), pen=None, name="R-gray-left")
        self.graph2_curve_bg_gray_le_g = self.ui.graph_calc2_bg_gray.getPlotItem().plot(symbol="o", symbolSize=9, symbolBrush=(000, 255, 000), pen=None, name="G-gray-left")
        self.graph2_curve_bg_gray_le_b = self.ui.graph_calc2_bg_gray.getPlotItem().plot(symbol="o", symbolSize=9, symbolBrush=(000, 000, 255), pen=None, name="B-gray-left")
        self.graph2_curve_bg_gray_re_r = self.ui.graph_calc2_bg_gray.getPlotItem().plot(symbol="x", symbolSize=9, symbolBrush=(255, 000, 000), pen=None, name="R-gray-right")
        self.graph2_curve_bg_gray_re_g = self.ui.graph_calc2_bg_gray.getPlotItem().plot(symbol="x", symbolSize=9, symbolBrush=(000, 255, 000), pen=None, name="G-gray-right")
        self.graph2_curve_bg_gray_re_b = self.ui.graph_calc2_bg_gray.getPlotItem().plot(symbol="x", symbolSize=9, symbolBrush=(000, 000, 255), pen=None, name="B-gray-right")
        self.graph2_curve_bg_gray_mi_r = self.ui.graph_calc2_bg_gray.getPlotItem().plot(pen=pg.mkPen("r", width=0, style=Qt.PenStyle.SolidLine), name="Estimated-R-bg")
        self.graph2_curve_bg_gray_mi_g = self.ui.graph_calc2_bg_gray.getPlotItem().plot(pen=pg.mkPen("g", width=0, style=Qt.PenStyle.SolidLine), name="Estimated-G-bg")
        self.graph2_curve_bg_gray_mi_b = self.ui.graph_calc2_bg_gray.getPlotItem().plot(pen=pg.mkPen("b", width=0, style=Qt.PenStyle.SolidLine), name="Estimated-B-bg")

        self.graph2_curve_bg_obje_le_r = self.ui.graph_calc2_bg_obje.getPlotItem().plot(symbol="o", symbolSize=9, symbolBrush=(255, 000, 000), pen=None, name="R-obje-left")
        self.graph2_curve_bg_obje_le_g = self.ui.graph_calc2_bg_obje.getPlotItem().plot(symbol="o", symbolSize=9, symbolBrush=(000, 255, 000), pen=None, name="G-obje-left")
        self.graph2_curve_bg_obje_le_b = self.ui.graph_calc2_bg_obje.getPlotItem().plot(symbol="o", symbolSize=9, symbolBrush=(000, 000, 255), pen=None, name="B-obje-left")
        self.graph2_curve_bg_obje_ri_r = self.ui.graph_calc2_bg_obje.getPlotItem().plot(symbol="x", symbolSize=9, symbolBrush=(255, 000, 000), pen=None, name="R-obje-right")
        self.graph2_curve_bg_obje_ri_g = self.ui.graph_calc2_bg_obje.getPlotItem().plot(symbol="x", symbolSize=9, symbolBrush=(000, 255, 000), pen=None, name="G-obje-right")
        self.graph2_curve_bg_obje_ri_b = self.ui.graph_calc2_bg_obje.getPlotItem().plot(symbol="x", symbolSize=9, symbolBrush=(000, 000, 255), pen=None, name="B-obje-right")
        self.graph2_curve_bg_obje_mi_r = self.ui.graph_calc2_bg_obje.getPlotItem().plot(pen=pg.mkPen("r", width=0, style=Qt.PenStyle.SolidLine), name="Estimated-R-bg")
        self.graph2_curve_bg_obje_mi_g = self.ui.graph_calc2_bg_obje.getPlotItem().plot(pen=pg.mkPen("g", width=0, style=Qt.PenStyle.SolidLine), name="Estimated-G-bg")
        self.graph2_curve_bg_obje_mi_b = self.ui.graph_calc2_bg_obje.getPlotItem().plot(pen=pg.mkPen("b", width=0, style=Qt.PenStyle.SolidLine), name="Estimated-B-bg")


        self.graph3_curve_759_calib_gray_r    = self.ui.graph_calc3_759_calib.getPlotItem().plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine), name="R-gray")
        self.graph3_curve_759_calib_gray_g    = self.ui.graph_calc3_759_calib.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="G-gray")
        self.graph3_curve_759_calib_gray_b    = self.ui.graph_calc3_759_calib.getPlotItem().plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine), name="B-gray")
        self.graph3_curve_759_calib_obje_r    = self.ui.graph_calc3_759_calib.getPlotItem().plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DashLine),  name="R-object")
        self.graph3_curve_759_calib_obje_g    = self.ui.graph_calc3_759_calib.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine),  name="G-object")
        self.graph3_curve_759_calib_obje_b    = self.ui.graph_calc3_759_calib.getPlotItem().plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DashLine),  name="B-object")
        self.graph3_curve_759_calib_gray_r_bg = self.ui.graph_calc3_759_calib.getPlotItem().plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DotLine),   name="BG: R-gray")
        self.graph3_curve_759_calib_gray_g_bg = self.ui.graph_calc3_759_calib.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DotLine),   name="BG: G-gray")
        self.graph3_curve_759_calib_gray_b_bg = self.ui.graph_calc3_759_calib.getPlotItem().plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DotLine),   name="BG: B-gray")
        self.graph3_curve_759_calib_obje_r_bg = self.ui.graph_calc3_759_calib.getPlotItem().plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DotLine),   name="BG: R-object")
        self.graph3_curve_759_calib_obje_g_bg = self.ui.graph_calc3_759_calib.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DotLine),   name="BG: G-object")
        self.graph3_curve_759_calib_obje_b_bg = self.ui.graph_calc3_759_calib.getPlotItem().plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DotLine),   name="BG: B-object")

        # graph3.5 for the sh
        self.graph3_5_gray2white_r = self.ui.graph_gray2white.getPlotItem().plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DotLine),  name="red")
        self.graph3_5_gray2white_g = self.ui.graph_gray2white.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DotLine),  name="green")
        self.graph3_5_gray2white_b = self.ui.graph_gray2white.getPlotItem().plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DotLine),  name="blue")
        self.graph3_5_gray2white_k = self.ui.graph_gray2white.getPlotItem().plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine),  name="black")

        # -------------------------------------------------------------------------------------------------------------------------
        self.graph4_curve_relf_r = self.ui.graph_calc4_refl_rgb.getPlotItem().plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine), name="R-refl")
        self.graph4_curve_relf_g = self.ui.graph_calc4_refl_rgb.getPlotItem().plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="G-refl")
        self.graph4_curve_relf_b = self.ui.graph_calc4_refl_rgb.getPlotItem().plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine), name="B-refl")

        # self.ui.graph_calc4_refl_rgb.getPlotItem().setLabels() # left="axis 1"
        self.p2 = pg.ViewBox()
        self.ui.graph_calc4_refl_rgb.getPlotItem().showAxis("right")
        self.ui.graph_calc4_refl_rgb.getPlotItem().scene().addItem(self.p2)
        self.ui.graph_calc4_refl_rgb.getPlotItem().getAxis("right").linkToView(self.p2)
        self.p2.setXLink(self.ui.graph_calc4_refl_rgb.getPlotItem().getViewBox())
        self.ui.graph_calc4_refl_rgb.getPlotItem().getAxis("right").setLabel("Weight of combination", color="#3f3f3f")


        def updateViews():
            #_ = self.ui.graph_calc4_refl_rgb.getPlotItem().addLegend()
            self.p2.setGeometry(self.ui.graph_calc4_refl_rgb.getPlotItem().getViewBox().sceneBoundingRect())
            self.p2.linkedViewChanged(self.ui.graph_calc4_refl_rgb.getPlotItem().getViewBox(), self.p2.XAxis)

        self.ui.graph_calc4_refl_rgb.getPlotItem().vb.sigResized.connect(updateViews)

        self.p2_weight_r = pg.PlotDataItem(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DashLine), name="R-weight")
        self.p2_weight_g = pg.PlotDataItem(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine), name="G-weight")
        self.p2_weight_b = pg.PlotDataItem(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DashLine), name="B-weight")


        self.p2.addItem(self.p2_weight_r)
        self.p2.addItem(self.p2_weight_g)
        self.p2.addItem(self.p2_weight_b)

        tmp_x = self.jp.gray.itp_hor_nm_array

        self.p2_weight_r.setData(tmp_x[:-100] / 10**9, self.jp.weight_r[:-100])
        self.p2_weight_g.setData(tmp_x[:-100] / 10**9, self.jp.weight_g[:-100])
        self.p2_weight_b.setData(tmp_x[:-100] / 10**9, self.jp.weight_b[:-100])

        updateViews()
        #   -----------------------------------------------------------------------------------------------------------
        self.graph_759nm_line_for_2dimg = pg.InfiniteLine(
            pos=192*2 + self.ui.sb_midx_init.value(), movable=False, angle=90, label="759.3nm",
            #labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True}
        )
        self.ui.graph_2dimg.getView().addItem(self.graph_759nm_line_for_2dimg)

        self.graph_desalted_graphs_sep_line_y0 = pg.InfiniteLine(pos=0, movable=False, angle=0)
        self.graph_desalted_graphs_sep_line_x0 = pg.InfiniteLine(pos=0, movable=False, angle=90)
        self.graph_desalted_graphs_sep_line_x1 = pg.InfiniteLine(pos=0, movable=False, angle=90)

        self.text_for_desalted_img_label0 = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">BG-Gray</span></div>',   anchor=(0, 0), border="w", fill=(100, 100, 100, 100))
        self.text_for_desalted_img_label1 = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">Gray</span></div>',      anchor=(0, 0), border="w", fill=(200,  50,  50, 100))
        self.text_for_desalted_img_label2 = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">BG-Gray</span></div>',   anchor=(0, 0), border="w", fill=(100, 100, 100, 100))
        self.text_for_desalted_img_label3 = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">BG-Object</span></div>', anchor=(0, 0), border="w", fill=(100, 100, 100, 100))
        self.text_for_desalted_img_label4 = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">Object</span></div>',    anchor=(0, 0), border="w", fill=(50,   50, 200, 100))
        self.text_for_desalted_img_label5 = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">BG-Object</span></div>', anchor=(0, 0), border="w", fill=(100, 100, 100, 100))

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
        self.graph_physical_spectrometer_shape_edges = np.array(
            [ [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0]]
        )

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
        #   -----------------------------------------------------------------------------------------------------------

        self.init_2d_graph_hide_the_original_roi_buttons()
        self.init_all_6_roi()
        # self.init_1_webfov_roi()
        self.init_sb_signals_for_ROI_controls()
        self.init_all_pyqtgraph()

        self.init_keyboard_bindings()
        self.init_actions()

        #self.update_physical_graph()

        self.init_physical_repr_graph()
        _ = self.ui.hs_physical_elv.valueChanged.connect(self.update_physical_graph)
        _ = self.ui.hs_physical_height.valueChanged.connect(self.update_physical_graph)


    def dir_searching_based_regex(self) -> None:
        current_search_prompt = self.ui.le_tv_name_narrower.text()
        if current_search_prompt == "":
            #self.fsmodel.setFilter(QDir.Filter.Files |  QDir.Filter.AllDirs)
            self.fsmodel.setFilter(QDir.Filter.Files |  QDir.Filter.AllDirs|  QDir.Filter.NoDotAndDotDot)
            self.fsmodel.setNameFilters((["*.jpeg"]))
            self.fsmodel.setNameFilterDisables(True)
        else:
            self.fsmodel.setFilter(QDir.Filter.Files |  QDir.Filter.Dirs|  QDir.Filter.NoDotAndDotDot)
            self.fsmodel.setNameFilters((["*" + current_search_prompt.replace(" ", "*") + "*"]))
            # need * regex on both side
            self.fsmodel.setNameFilterDisables(False)

    def init_2d_graph_hide_the_original_roi_buttons(self) -> None:
        """Hides the ROI/Menu buttons from the 3 images"""
        self.ui.graph_2dimg.ui.roiBtn.hide()
        self.ui.graph_2dimg.ui.menuBtn.hide()

        #self.ui.graph_2dimg.addItem(self.roi_label_obje)
        #self.ui.graph_2dimg.addItem(self.roi_label_gray)
        self.ui.graph_2dimg.getView().addItem(self.roi_label_obje)
        self.ui.graph_2dimg.getView().addItem(self.roi_label_gray)

    def init_all_6_roi(self) -> None:
        _ = self.roi_obje_main.addScaleHandle([0.5, 1], [0.5, 0])
        _ = self.roi_gray_main.addScaleHandle([0.5, 1], [0.5, 0])

        self.roi_obje_main.setZValue(10)
        self.roi_gray_main.setZValue(10)

        _ = self.roi_gray_bglf.addScaleHandle([0, 0.5], [1, 0.5])
        _ = self.roi_gray_bglf.addScaleHandle([1, 0.5], [0, 0.5])
        _ = self.roi_gray_bgri.addScaleHandle([1, 0.5], [0, 0.5])
        _ = self.roi_gray_bgri.addScaleHandle([0, 0.5], [1, 0.5])
        _ = self.roi_gray_bglf.setZValue(10)
        _ = self.roi_gray_bgri.setZValue(10)

        _ = self.roi_obje_bglf.addScaleHandle([0, 0.5], [1, 0.5])
        _ = self.roi_obje_bglf.addScaleHandle([1, 0.5], [0, 0.5])
        _ = self.roi_obje_bgri.addScaleHandle([1, 0.5], [0, 0.5])
        _ = self.roi_obje_bgri.addScaleHandle([0, 0.5], [1, 0.5])
        _ = self.roi_obje_bglf.setZValue(10)
        _ = self.roi_obje_bgri.setZValue(10)

        _ = self.ui.graph_2dimg.getView().addItem(self.roi_obje_main)
        _ = self.ui.graph_2dimg.getView().addItem(self.roi_obje_bgri)
        _ = self.ui.graph_2dimg.getView().addItem(self.roi_obje_bglf)
        _ = self.ui.graph_2dimg.getView().addItem(self.roi_gray_main)
        _ = self.ui.graph_2dimg.getView().addItem(self.roi_gray_bglf)
        _ = self.ui.graph_2dimg.getView().addItem(self.roi_gray_bgri)

        self.ui.graph_calc1_desalted_roi.getView().addItem(self.graph_desalted_graphs_sep_line_y0)
        self.ui.graph_calc1_desalted_roi.getView().addItem(self.graph_desalted_graphs_sep_line_x0)
        self.ui.graph_calc1_desalted_roi.getView().addItem(self.graph_desalted_graphs_sep_line_x1)

        self.ui.graph_calc1_desalted_roi.getView().addItem(self.text_for_desalted_img_label0)
        self.ui.graph_calc1_desalted_roi.getView().addItem(self.text_for_desalted_img_label1)
        self.ui.graph_calc1_desalted_roi.getView().addItem(self.text_for_desalted_img_label2)
        self.ui.graph_calc1_desalted_roi.getView().addItem(self.text_for_desalted_img_label3)
        self.ui.graph_calc1_desalted_roi.getView().addItem(self.text_for_desalted_img_label4)
        self.ui.graph_calc1_desalted_roi.getView().addItem(self.text_for_desalted_img_label5)

    def init_sb_signals_for_ROI_controls(self) -> None:
        _ = self.ui.sb_gray_y_init.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_gray_y_size.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_obje_y_init.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_obje_y_size.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_midx_init.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_midx_size.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_lefx_init_rel.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_lefx_size.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_rigx_init_rel.valueChanged.connect(self.update_raw_from_sb)
        _ = self.ui.sb_rigx_size.valueChanged.connect(self.update_raw_from_sb)

        _ = self.ui.sb_waveperpixel.valueChanged.connect(self.update_raw_roi_plot_when_sb_or_roi_moved)

        _ = self.roi_gray_main.sigRegionChanged.connect(lambda: self.handle_roi_change("gray", "middle"))
        _ = self.roi_gray_bglf.sigRegionChanged.connect(lambda: self.handle_roi_change("gray", "left"))
        _ = self.roi_gray_bgri.sigRegionChanged.connect(lambda: self.handle_roi_change("gray", "right"))

        _ = self.roi_obje_main.sigRegionChanged.connect(lambda: self.handle_roi_change("obje", "middle"))
        _ = self.roi_obje_bglf.sigRegionChanged.connect(lambda: self.handle_roi_change("obje", "left"))
        _ = self.roi_obje_bgri.sigRegionChanged.connect(lambda: self.handle_roi_change("obje", "right"))

    def init_all_pyqtgraph(self) -> None:
        # -------------------------------------------------------------------------------------------------------------
        _ = self.ui.graph_calc2_bg_gray.getPlotItem().addLegend()
        _ = self.ui.graph_calc2_bg_obje.getPlotItem().addLegend()

        self.ui.graph_calc2_bg_gray.getPlotItem().setLabel("left",   "Background", units="DN")
        self.ui.graph_calc2_bg_gray.getPlotItem().setLabel("bottom", "Wavelenght", units="m")
        self.ui.graph_calc2_bg_gray.getPlotItem().setTitle("Gray Region Background")

        self.ui.graph_calc2_bg_obje.getPlotItem().setLabel("left",   "Background", units="DN")
        self.ui.graph_calc2_bg_obje.getPlotItem().setLabel("bottom", "Wavelenght", units="m")
        self.ui.graph_calc2_bg_obje.getPlotItem().setTitle("Object Region Background")


        # --------graph 3:  759 calibration curves ---------------------------------------------------------------------
        # self.ui.graph_calc3_759_calib.getPlotItem().clear()
        _ = self.ui.graph_calc3_759_calib.getPlotItem().addLegend()
        self.ui.graph_calc3_759_calib.getPlotItem().addItem(
            pg.InfiniteLine(
                pos=759.37 / 10**9,
                movable=False, angle=90,
                label="x={value:0.2f}nm",
                labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True}))

        self.ui.graph_calc3_759_calib.getPlotItem().setLabel("left",   "Digital Number", units="DN")
        self.ui.graph_calc3_759_calib.getPlotItem().setLabel("bottom", "Wavelength",     units="m") #, unitPrefix= "n")
        self.ui.graph_calc3_759_calib.getPlotItem().setTitle("After 759nm calibration")

        # --------graph 4:  rgb refl  ---------------------------------------------------------------------
        # self.ui.graph_calc4_refl_rgb.getPlotItem().clear()
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
        # self.ui.graph_calc5_refl_final.getPlotItem().clear()


        self.ui.graph_calc5_refl_final.getPlotItem().setLabel("left", "Reflection")
        self.ui.graph_calc5_refl_final.getPlotItem().setLabel("bottom", "Wavelength", units="m")
        self.ui.graph_calc5_refl_final.getPlotItem().setTitle("Reflection")

        self.ui.graph_calc5_refl_final.getPlotItem().addItem(self.graph5_norm_one_line)
        self.ui.graph_calc5_refl_final.getPlotItem().addItem(self.graph5_norm_zero_line)
        _ = self.ui.graph_calc5_refl_final.getPlotItem().addLegend()


    def all_sb_signal_enable_or_disable(self, b: bool) -> None:
        """Temporaray block or not block the signals in order to 2 way control"""
        _ = self.ui.sb_lefx_size.blockSignals(b)
        _ = self.ui.sb_lefx_init_rel.blockSignals(b)
        _ = self.ui.sb_rigx_size.blockSignals(b)
        _ = self.ui.sb_rigx_init_rel.blockSignals(b)
        _ = self.ui.sb_midx_init.blockSignals(b)
        _ = self.ui.sb_midx_size.blockSignals(b)
        _ = self.ui.sb_gray_y_init.blockSignals(b)
        _ = self.ui.sb_gray_y_size.blockSignals(b)
        _ = self.ui.sb_obje_y_init.blockSignals(b)
        _ = self.ui.sb_obje_y_size.blockSignals(b)

    def handle_roi_change(self, gray_or_obje: str, left_middle_right: str) -> None:
        self.all_sb_signal_enable_or_disable(True)
        logger.debug(f"handle_roi_change: {self.roi_gray_main.getState()['pos']=}, {self.roi_gray_bglf.getState()['pos']=}")

        if gray_or_obje == "gray":
            if left_middle_right == "middle":
                gray_posx, gray_posy, gray_sizex, gray_sizey = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_gray_main.getState())

                self.ui.sb_midx_init.setValue(gray_posx)
                self.ui.sb_midx_size.setValue(gray_sizex)
                self.ui.sb_gray_y_init.setValue(gray_posy)
                self.ui.sb_gray_y_size.setValue(gray_sizey)

            elif left_middle_right == "left":
                gray_posx, _,          _, _ = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_gray_main.getState())
                bglf_posx, _, bglf_sizex, _ = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_gray_bglf.getState())
                self.ui.sb_lefx_init_rel.setValue(- gray_posx + bglf_posx)
                self.ui.sb_lefx_size.setValue(bglf_sizex)

            elif left_middle_right == "right":
                gray_posx, _,          _, _ = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_gray_main.getState())
                bgri_posx, _, bgri_sizex, _ = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_gray_bgri.getState())
                self.ui.sb_rigx_init_rel.setValue(- gray_posx + bgri_posx)
                self.ui.sb_rigx_size.setValue(bgri_sizex)

        elif gray_or_obje == "obje":
            if left_middle_right == "middle":
                obje_posx, obje_posy, obje_sizex, obje_sizey = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_obje_main.getState())

                self.ui.sb_midx_init.setValue(obje_posx)
                self.ui.sb_midx_size.setValue(obje_sizex)
                self.ui.sb_obje_y_init.setValue(obje_posy)
                self.ui.sb_obje_y_size.setValue(obje_sizey)

            elif left_middle_right == "left":
                gray_posx, _,          _, _ = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_gray_main.getState())
                bglf_posx, _, bglf_sizex, _ = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_obje_bglf.getState())

                self.ui.sb_lefx_init_rel.setValue(- gray_posx + bglf_posx)
                self.ui.sb_lefx_size.setValue(bglf_sizex)

            elif left_middle_right == "right":
                gray_posx, _,          _, _ = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_gray_main.getState())
                bgri_posx, _, bgri_sizex, _ = self.get_posx_posy_sizex_sizy_cleaner_carefuler_way(self.roi_obje_bgri.getState())

                self.ui.sb_rigx_init_rel.setValue(- gray_posx + bgri_posx)
                self.ui.sb_rigx_size.setValue(bgri_sizex)

        self.all_sb_signal_enable_or_disable(False)
        self.update_raw_from_sb()

    def get_posx_posy_sizex_sizy_cleaner_carefuler_way(self, tmp_roi_state: dict[str, pg.Point|float]) -> tuple[int, int, int, int]:
        #tmp_roi_state = tmp_roi.getState()
        assert ("pos" in tmp_roi_state) and ("size" in tmp_roi_state), "Err while returning roi"
        tmp_roi_pos = tmp_roi_state["pos"]
        tmp_roi_size = tmp_roi_state["size"]
        assert isinstance(tmp_roi_pos, QPointF) and isinstance(tmp_roi_size, QPointF), "Err while returning self.roi_gray_main.getState()"

        return int(tmp_roi_pos.x()), int(tmp_roi_pos.y()), int(tmp_roi_size.x()), int(tmp_roi_size.y())


    def update_raw_from_sb(self) -> None:
        _ = self.roi_gray_main.blockSignals(True)
        _ = self.roi_gray_bglf.blockSignals(True)
        _ = self.roi_gray_bgri.blockSignals(True)
        _ = self.roi_obje_main.blockSignals(True)
        _ = self.roi_obje_bglf.blockSignals(True)
        _ = self.roi_obje_bgri.blockSignals(True)

        self.roi_gray_main.setPos(self.ui.sb_midx_init.value(), self.ui.sb_gray_y_init.value())
        self.roi_gray_bglf.setPos(self.ui.sb_midx_init.value() + self.ui.sb_lefx_init_rel.value(), self.ui.sb_gray_y_init.value())
        self.roi_gray_bgri.setPos(self.ui.sb_midx_init.value() + self.ui.sb_rigx_init_rel.value(), self.ui.sb_gray_y_init.value())
        self.roi_obje_main.setPos(self.ui.sb_midx_init.value(), self.ui.sb_obje_y_init.value())
        self.roi_obje_bglf.setPos(self.ui.sb_midx_init.value() + self.ui.sb_lefx_init_rel.value(), self.ui.sb_obje_y_init.value())
        self.roi_obje_bgri.setPos(self.ui.sb_midx_init.value() + self.ui.sb_rigx_init_rel.value(), self.ui.sb_obje_y_init.value())

        self.roi_gray_main.setSize((self.ui.sb_midx_size.value(), self.ui.sb_gray_y_size.value()))
        self.roi_gray_bglf.setSize((self.ui.sb_lefx_size.value(), self.ui.sb_gray_y_size.value()))
        self.roi_gray_bgri.setSize((self.ui.sb_rigx_size.value(), self.ui.sb_gray_y_size.value()))
        self.roi_obje_main.setSize((self.ui.sb_midx_size.value(), self.ui.sb_obje_y_size.value()))
        self.roi_obje_bglf.setSize((self.ui.sb_lefx_size.value(), self.ui.sb_obje_y_size.value()))
        self.roi_obje_bgri.setSize((self.ui.sb_rigx_size.value(), self.ui.sb_obje_y_size.value()))
        self.graph_759nm_line_for_2dimg.setPos(pos=self.ui.sb_midx_init.value() + 192*2)

        _ = self.roi_gray_main.blockSignals(False)
        _ = self.roi_gray_bglf.blockSignals(False)
        _ = self.roi_gray_bgri.blockSignals(False)
        _ = self.roi_obje_main.blockSignals(False)
        _ = self.roi_obje_bglf.blockSignals(False)
        _ = self.roi_obje_bgri.blockSignals(False)

        # change the label position
        self.roi_label_gray.setPos(self.ui.sb_midx_init.value(), self.ui.sb_gray_y_init.value())
        self.roi_label_obje.setPos(self.ui.sb_midx_init.value(), self.ui.sb_obje_y_init.value())

        self.update_raw_roi_plot_when_sb_or_roi_moved()

        # when
        if not self.paramsChangingFromHistory:
            self.ui.cb_parameter_history.setCurrentIndex(0) # when change happens make it current

        # say reflection is changed
        #self.graph5_curve_relf.
        #self.ui.graph_calc5_refl_final.clear()

        self.update_fov_on_webcam()

    def update_fov_on_webcam(self) -> None:
        self.ui.l_target_distance.setText(f"Distance: {self.ui.hs_target_distance.value()}cm")
        fov_pw1 = self.pxlspec_to_pxlweb_formula(self.ui.hs_target_distance.value(), self.ui.sb_obje_y_init.value())
        fov_pw2 = self.pxlspec_to_pxlweb_formula(self.ui.hs_target_distance.value(), self.ui.sb_obje_y_init.value() + self.ui.sb_obje_y_size.value())
        self.roi_webcam_fov.setPos((310, fov_pw1))
        self.roi_webcam_fov.setSize((20, fov_pw2-fov_pw1))


    def update_raw_roi_plot_when_sb_or_roi_moved(self) -> None:
        """update raw dn plot, when either spinbox or ROI dragged"""
        self.ui.cb_parameter_history.setCurrentIndex(0)
        # print("i changed")

        self.ui.graph_raw.getPlotItem().clear()
        _ = self.ui.graph_raw.getPlotItem().addLegend()

        self.ui.graph_raw.addItem(
            pg.InfiniteLine(
                pos=759.37,
                movable=False, angle=90,
                label="x={value:0.2f}nm",
                labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True}
            )
        )

        tmp_x = get_wavelength_array(
            init_pxl=0,
            pxl_size=350,
            waveperpixel=self.ui.sb_waveperpixel.value(),
        )

        gray_roi_mid: NDArray[np.uint16] = self.jp.data[
            self.ui.sb_gray_y_init.value() : self.ui.sb_gray_y_init.value() + self.ui.sb_gray_y_size.value(),
            self.ui.sb_midx_init.value()   : self.ui.sb_midx_init.value()   + self.ui.sb_midx_size.value()
        ].astype(np.uint16)
        obje_roi_mid: NDArray[np.uint16] = self.jp.data[
            self.ui.sb_obje_y_init.value() : self.ui.sb_obje_y_init.value() + self.ui.sb_obje_y_size.value(),
            self.ui.sb_midx_init.value()   : self.ui.sb_midx_init.value()   + self.ui.sb_midx_size.value()
        ].astype(np.uint16)
        assert isinstance(gray_roi_mid, np.ndarray) and (gray_roi_mid.dtype == np.uint16)
        assert isinstance(obje_roi_mid, np.ndarray) and (obje_roi_mid.dtype == np.uint16)
        #print(obje_roi_mid.dtype)

        #tmp = self.jp.data[:].astype(np.uint16)
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_x, gray_roi_mid[1::2, 1::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine), name="R-gray")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_x, gray_roi_mid[1::2, 0::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="G-gray")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_x, gray_roi_mid[0::2, 1::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="G-gray")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_x, gray_roi_mid[0::2, 0::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine), name="B-gray")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_x, obje_roi_mid[1::2, 1::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DashLine),  name="R-object")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_x, obje_roi_mid[1::2, 0::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine),  name="G-object")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_x, obje_roi_mid[0::2, 1::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine),  name="G-object")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_x, obje_roi_mid[0::2, 0::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DashLine),  name="B-object")


        tmp_lef_x = get_wavelength_array(
            init_pxl=self.ui.sb_lefx_init_rel.value()//2,
            pxl_size=self.ui.sb_lefx_size.value()//2,
            waveperpixel=self.ui.sb_waveperpixel.value(),
        )
        tmp_rig_x = get_wavelength_array(
            init_pxl=self.ui.sb_rigx_init_rel.value()//2,
            pxl_size=self.ui.sb_rigx_size.value()//2,
            waveperpixel=self.ui.sb_waveperpixel.value(),
        )

        gray_roi_lef = self.jp.data[
            self.ui.sb_gray_y_init.value() : self.ui.sb_gray_y_init.value() + self.ui.sb_gray_y_size.value(),
            self.ui.sb_midx_init.value() + self.ui.sb_lefx_init_rel.value() : self.ui.sb_midx_init.value()  + self.ui.sb_lefx_init_rel.value() + self.ui.sb_lefx_size.value()
        ]

        gray_roi_rig = self.jp.data[
            self.ui.sb_gray_y_init.value() : self.ui.sb_gray_y_init.value() + self.ui.sb_gray_y_size.value(),
            self.ui.sb_midx_init.value() + self.ui.sb_rigx_init_rel.value() : self.ui.sb_midx_init.value()  + self.ui.sb_rigx_init_rel.value() + self.ui.sb_rigx_size.value()
        ]

        _ = self.ui.graph_raw.getPlotItem().plot(tmp_lef_x, gray_roi_lef[1::2, 1::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine), name="bgR-gray")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_lef_x, gray_roi_lef[1::2, 0::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="bgG-gray")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_lef_x, gray_roi_lef[0::2, 1::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="bgG-gray")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_lef_x, gray_roi_lef[0::2, 0::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine), name="bgB-gray")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_rig_x, gray_roi_rig[1::2, 1::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DashLine),  name="bgR-object")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_rig_x, gray_roi_rig[1::2, 0::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine),  name="bgG-object")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_rig_x, gray_roi_rig[0::2, 1::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine),  name="bgG-object")
        _ = self.ui.graph_raw.getPlotItem().plot(tmp_rig_x, gray_roi_rig[0::2, 0::2].mean(axis=0, dtype=np.float64), pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DashLine),  name="bgB-object")


    def handle_cb_calc5_norming(self) -> None:
        # print("i was clicked")
        self.ui.sb_calc5_norm_zero.setEnabled(self.ui.cb_calc5_norm.isChecked())
        self.ui.sb_calc5_norm_one.setEnabled(self.ui.cb_calc5_norm.isChecked())
        try:
            self.call_calibrate_and_calculate_calc5_refl_n_norm()
        except Exception as e:
            print(e)

    def toggle_filetype_visiblity(self, a: int) -> None:
        if a == 2:
            self.fsmodel.setNameFilters((["*.jpeg"]))
        else:
            self.fsmodel.setNameFilters((["*"]))

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
        _ = QShortcut(QKeySequence("Alt+F"),     self).activated.connect( lambda: self.ui.le_tv_name_narrower.setFocus())

    def init_actions(self) -> None:
        _ = self.ui.action_help.triggered.connect(self.open_help_page)
        # _ = self.ui.action_dir_cur_child_fold.connect( #lambda self.ui.tv_dir.collapse())
        # _ = self.ui.action_dir_cur_child_unfold.connect(self.ui.tv_dir.)
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
        # print(tmpdirectory)
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
                "Selected item is not a file.\n" +
                "If this is a folder press ENTER (or double mouseclick)" +
                "to enter this folder"
            )
            _ = dlg.exec()
            return False
        if not ((".jpeg" in basename) and (basename.count("_") in (3, 4))):
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Wrong File selected")
            dlg.setText(
                "Selected item is not (JPEG or Directory)\n" +
                "Please select JPEG or Directory"
            )
            _ = dlg.exec()
            return False

        self.jpeg_path = tmppath
        self.dir_path = os.path.dirname(self.jpeg_path)
        _ = self.ddtree.set_ddir(self.dir_path)
        self.ui.tb_meta_json.setText(self.ddtree.metajsonText)
        logger.info(f"short_cut_preview_raw_jpeg: {self.ddtree.webcamFP=}")

        if self.ddtree.webcamFP is not None:
            try:
                webcam_img = Image.open(self.ddtree.webcamFP)
                webcam = np.array(webcam_img)
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

        _ = self.jp.load_jpeg_file(self.jpeg_path, also_get_rgb_rerp=True)
        self.update_1_rawbayer_img_data_and_then_plot_below()

        # try to reset & repopulate paramHisotry combobox
        self.repopulate_param_hist_combobox()
        return True

    def repopulate_param_hist_combobox(self) -> None:
        self.paramLogPath = os.path.join(self.ddtree.ddir, "output", "export_log.csv")
        self.dfParamHistory = self.read_param_history_file_and_handle_if_corrupted(self.paramLogPath)
        self.ui.cb_parameter_history.clear()
        self.ui.cb_parameter_history.addItem("Current")                               # <-- current different
        self.ui.cb_parameter_history.addItems(self.dfParamHistory["date"].astype(str).tolist())


    def call_tv_onItemDoubleClicked(self, v: QModelIndex):
        tmp = self.fsmodel.filePath(v)
        if os.path.isdir(tmp):
            logger.info(f"call_tv_onItemClicked: {tmp}")
            self.short_cut_goto_selected_child_dir()
        else:
            _ = self.short_cut_preview_raw_jpeg()

    def call_calibrate_and_calculate(self) -> None:
        self.call_calibrate_and_calculate_calc1_desalt()           # done
        self.ui.pbar_calc.setValue(0)
        self.ui.tabWidget.setCurrentIndex(0)
        time.sleep(.1)
        self.call_calibrate_and_calculate_calc2_background()       # done
        self.ui.pbar_calc.setValue(25)
        self.ui.tabWidget.setCurrentIndex(1)
        time.sleep(.1)
        self.call_calibrate_and_calculate_calc3_759_calib()
        self.ui.pbar_calc.setValue(50)
        self.ui.tabWidget.setCurrentIndex(2)
        time.sleep(.1)

        # gray 2 white
        #self.call_calibrate_and_calculate_calc3_759_calib()
        self.call_calibrate_and_calculate_calc3_5_gray2white()
        self.ui.pbar_calc.setValue(60)
        self.ui.tabWidget.setCurrentIndex(3)
        time.sleep(.1)

        self.call_calibrate_and_calculate_calc4_rgb_refl()
        self.ui.pbar_calc.setValue(75)
        self.ui.tabWidget.setCurrentIndex(4)
        time.sleep(.1)

        self.call_calibrate_and_calculate_calc5_refl_n_norm()
        self.ui.pbar_calc.setValue(100)
        self.ui.tabWidget.setCurrentIndex(5)
        time.sleep(.1)


    def call_calibrate_and_calculate_calc1_desalt(self) -> None:
        self.jp.set_roi_geometry(
            xWaveRng=(self.ui.sb_midx_init.value(), self.ui.sb_midx_init.value() + self.ui.sb_midx_size.value()),
            xLfBgRng=(self.ui.sb_midx_init.value() + self.ui.sb_lefx_init_rel.value(), self.ui.sb_midx_init.value() + self.ui.sb_lefx_init_rel.value() + self.ui.sb_lefx_size.value()),
            xRiBgRng=(self.ui.sb_midx_init.value() + self.ui.sb_rigx_init_rel.value(), self.ui.sb_midx_init.value() + self.ui.sb_rigx_init_rel.value() + self.ui.sb_rigx_size.value()),
            yGrayRng=(self.ui.sb_gray_y_init.value(), self.ui.sb_gray_y_init.value() + self.ui.sb_gray_y_size.value()),
            yObjeRng=(self.ui.sb_obje_y_init.value(), self.ui.sb_obje_y_init.value() + self.ui.sb_obje_y_size.value()),
        )

        desaltedimg = np.concatenate(
            (np.concatenate((self.jp.gray_bgle.roi_desalted, self.jp.gray.roi_desalted, self.jp.gray_bgri.roi_desalted), axis=1),
             np.concatenate((self.jp.obje_bgle.roi_desalted, self.jp.obje.roi_desalted, self.jp.obje_bgri.roi_desalted), axis=1)),
            axis=0, dtype=np.int64
        )
        desalted_concatted_bayer_rgb_all_6roi = np.zeros(shape=(desaltedimg.shape[0], desaltedimg.shape[1], 3), dtype=np.int64)
        desalted_concatted_bayer_rgb_all_6roi[0::2, 0::2, 2] = desaltedimg[0::2, 0::2]
        desalted_concatted_bayer_rgb_all_6roi[0::2, 1::2, 1] = desaltedimg[0::2, 1::2]
        desalted_concatted_bayer_rgb_all_6roi[1::2, 0::2, 1] = desaltedimg[1::2, 0::2]
        desalted_concatted_bayer_rgb_all_6roi[1::2, 1::2, 0] = desaltedimg[1::2, 1::2]

        self.ui.graph_calc1_desalted_roi.setImage(
            img=desalted_concatted_bayer_rgb_all_6roi,
            levels=(desalted_concatted_bayer_rgb_all_6roi.min(), desalted_concatted_bayer_rgb_all_6roi.max()),
            axes={"x":1, "y":0, "c":2}
        )

        self.graph_desalted_graphs_sep_line_y0.setPos(self.ui.sb_gray_y_size.value())
        self.graph_desalted_graphs_sep_line_x0.setPos(self.ui.sb_lefx_size.value())
        self.graph_desalted_graphs_sep_line_x1.setPos(self.ui.sb_lefx_size.value() + self.ui.sb_midx_size.value())

        self.text_for_desalted_img_label0.setPos(0                                                             , 0)
        self.text_for_desalted_img_label1.setPos(self.ui.sb_lefx_size.value() + self.ui.sb_midx_size.value()/2 , 0)
        self.text_for_desalted_img_label2.setPos(self.ui.sb_lefx_size.value() + self.ui.sb_midx_size.value()   , 0)
        self.text_for_desalted_img_label3.setPos(0                                                             , self.ui.sb_gray_y_size.value())
        self.text_for_desalted_img_label4.setPos(self.ui.sb_lefx_size.value() + self.ui.sb_midx_size.value()/2 , self.ui.sb_gray_y_size.value())
        self.text_for_desalted_img_label5.setPos(self.ui.sb_lefx_size.value() + self.ui.sb_midx_size.value()   , self.ui.sb_gray_y_size.value())

    def call_calibrate_and_calculate_calc2_background(self) -> None:
        self.jp.background_calculation_on_all_channels_seperately()

        tmp_lef_x = get_wavelength_array(
            init_pxl=self.ui.sb_lefx_init_rel.value()//2,
            pxl_size=self.ui.sb_lefx_size.value()//2,
            waveperpixel=self.ui.sb_waveperpixel.value(),
        )
        tmp_rig_x = get_wavelength_array(
            init_pxl=self.ui.sb_rigx_init_rel.value()//2,
            pxl_size=self.ui.sb_rigx_size.value()//2,
            waveperpixel=self.ui.sb_waveperpixel.value(),
        )

        self.graph2_curve_bg_gray_le_r.setData(self.jp.gray_bgle.rchan_wl / 10**9, self.jp.gray_bgle.rchan_dn)
        self.graph2_curve_bg_gray_le_g.setData(self.jp.gray_bgle.gchan_wl / 10**9, self.jp.gray_bgle.gchan_dn)
        self.graph2_curve_bg_gray_le_b.setData(self.jp.gray_bgle.bchan_wl / 10**9, self.jp.gray_bgle.bchan_dn)
        self.graph2_curve_bg_gray_re_r.setData(self.jp.gray_bgri.rchan_wl / 10**9, self.jp.gray_bgri.rchan_dn)
        self.graph2_curve_bg_gray_re_g.setData(self.jp.gray_bgri.gchan_wl / 10**9, self.jp.gray_bgri.gchan_dn)
        self.graph2_curve_bg_gray_re_b.setData(self.jp.gray_bgri.bchan_wl / 10**9, self.jp.gray_bgri.bchan_dn)

        self.graph2_curve_bg_obje_le_r.setData(self.jp.obje_bgle.rchan_wl / 10**9, self.jp.obje_bgle.rchan_dn)
        self.graph2_curve_bg_obje_le_g.setData(self.jp.obje_bgle.gchan_wl / 10**9, self.jp.obje_bgle.gchan_dn)
        self.graph2_curve_bg_obje_le_b.setData(self.jp.obje_bgle.bchan_wl / 10**9, self.jp.obje_bgle.bchan_dn)
        self.graph2_curve_bg_obje_ri_r.setData(self.jp.obje_bgri.rchan_wl / 10**9, self.jp.obje_bgri.rchan_dn)
        self.graph2_curve_bg_obje_ri_g.setData(self.jp.obje_bgri.gchan_wl / 10**9, self.jp.obje_bgri.gchan_dn)
        self.graph2_curve_bg_obje_ri_b.setData(self.jp.obje_bgri.bchan_wl / 10**9, self.jp.obje_bgri.bchan_dn)

        tmp_bgx: NDArray[np.float64] = np.arange(tmp_lef_x.min(), tmp_rig_x.max(), 1, dtype=np.float64)

        self.graph2_curve_bg_gray_mi_r.setData(tmp_bgx / 10**9, background(tmp_bgx, *(self.jp.bg_gray_r_popt)))
        self.graph2_curve_bg_gray_mi_g.setData(tmp_bgx / 10**9, background(tmp_bgx, *(self.jp.bg_gray_g_popt)))
        self.graph2_curve_bg_gray_mi_b.setData(tmp_bgx / 10**9, background(tmp_bgx, *(self.jp.bg_gray_b_popt)))
        self.graph2_curve_bg_obje_mi_r.setData(tmp_bgx / 10**9, background(tmp_bgx, *(self.jp.bg_obje_r_popt)))
        self.graph2_curve_bg_obje_mi_g.setData(tmp_bgx / 10**9, background(tmp_bgx, *(self.jp.bg_obje_g_popt)))
        self.graph2_curve_bg_obje_mi_b.setData(tmp_bgx / 10**9, background(tmp_bgx, *(self.jp.bg_obje_b_popt)))


    def call_calibrate_and_calculate_calc3_759_calib(self) -> None:
        self.jp.calibrate_n_calculate_final_output()
        tmp_x = self.jp.gray.itp_hor_nm_array

        self.graph3_curve_759_calib_gray_r.setData(tmp_x/ 10**9, self.jp.gray.rchan_smdn_itp_after_759nm_calib)
        self.graph3_curve_759_calib_gray_g.setData(tmp_x/ 10**9, self.jp.gray.gchan_smdn_itp_after_759nm_calib)
        self.graph3_curve_759_calib_gray_b.setData(tmp_x/ 10**9, self.jp.gray.bchan_smdn_itp_after_759nm_calib)
        self.graph3_curve_759_calib_obje_r.setData(tmp_x/ 10**9, self.jp.obje.rchan_smdn_itp_after_759nm_calib)
        self.graph3_curve_759_calib_obje_g.setData(tmp_x/ 10**9, self.jp.obje.gchan_smdn_itp_after_759nm_calib)
        self.graph3_curve_759_calib_obje_b.setData(tmp_x/ 10**9, self.jp.obje.bchan_smdn_itp_after_759nm_calib)

        self.graph3_curve_759_calib_gray_r_bg.setData(tmp_x / 10**9, background(tmp_x, *(self.jp.bg_gray_r_popt)))
        self.graph3_curve_759_calib_gray_g_bg.setData(tmp_x / 10**9, background(tmp_x, *(self.jp.bg_gray_g_popt)))
        self.graph3_curve_759_calib_gray_b_bg.setData(tmp_x / 10**9, background(tmp_x, *(self.jp.bg_gray_b_popt)))
        self.graph3_curve_759_calib_obje_r_bg.setData(tmp_x / 10**9, background(tmp_x, *(self.jp.bg_obje_r_popt)))
        self.graph3_curve_759_calib_obje_g_bg.setData(tmp_x / 10**9, background(tmp_x, *(self.jp.bg_obje_g_popt)))
        self.graph3_curve_759_calib_obje_b_bg.setData(tmp_x / 10**9, background(tmp_x, *(self.jp.bg_obje_b_popt)))


    def call_calibrate_and_calculate_calc3_5_gray2white(self) -> None:
        self.jp.calibrate_n_calculate_final_output()
        tmp_x = self.jp.mgray2white[:, 0].astype(np.float64)

        self.graph3_5_gray2white_r.setData(tmp_x/ 10**9, self.jp.mgray2white[:, 3])
        self.graph3_5_gray2white_g.setData(tmp_x/ 10**9, self.jp.mgray2white[:, 2])
        self.graph3_5_gray2white_b.setData(tmp_x/ 10**9, self.jp.mgray2white[:, 1])
        self.graph3_5_gray2white_k.setData(tmp_x/ 10**9, self.jp.mgray2white[:, 4])

    def call_calibrate_and_calculate_calc4_rgb_refl(self) -> None:
        self.jp.fancy_reflectance()
        tmp_x = self.jp.gray.itp_hor_nm_array
        self.graph4_curve_relf_r.setData(tmp_x[:-100] / 10**9, self.jp.ref_fancy_r[:-100])
        self.graph4_curve_relf_g.setData(tmp_x[:-100] / 10**9, self.jp.ref_fancy_g[:-100])
        self.graph4_curve_relf_b.setData(tmp_x[:-100] / 10**9, self.jp.ref_fancy_b[:-100])


    def call_calibrate_and_calculate_calc5_refl_n_norm(self) -> None:
        self.jp.fancy_reflectance()
        tmp_x = self.jp.gray.itp_hor_nm_array

        if not self.ui.cb_calc5_norm.isChecked():
            self.graph5_curve_relf.setData(tmp_x[:-100] / 10**9, self.jp.ref_fancy[:-100]) #  // 10**9
        else:
            zero_index = int((self.ui.sb_calc5_norm_zero.value() - 400) / 0.5)
            one_index = int((self.ui.sb_calc5_norm_one.value() - 400 )/ 0.5)
            self.jp.normalize_the_fancy(zero_index, one_index)
            self.graph5_curve_relf.setData(tmp_x[:-100] / 10**9, self.jp.ref_fancy_normed[:-100]) # // 10**9
            self.ui.graph_calc5_refl_final.getPlotItem().getViewBox().setYRange(-0.1, 1.1)
            self.graph5_norm_one_line.setPos(self.ui.sb_calc5_norm_one.value() / 10**9)
            self.graph5_norm_zero_line.setPos(self.ui.sb_calc5_norm_zero.value() / 10**9)

    def update_1_rawbayer_img_data_and_then_plot_below(self) -> None:
        self.ui.graph_2dimg.clear()
        self.ui.graph_2dimg.setImage(
            img=self.jp.rgb if not self.ui.cb_rawbayer_visual_demosiac.isChecked() else self.jp.rgb_demosiac,
            levels=(0, 1024),
            axes={"x":1, "y":0, "c":2})
        self.update_raw_from_sb()


    def short_cut_export_raw_jpeg(self) -> None:
        """C-e: export"""
        if not self.short_cut_preview_raw_jpeg():    # checking the selected jpeg
            return

        self.call_calibrate_and_calculate()

        os.makedirs(os.path.join(self.ddtree.ddir, "output"), exist_ok=True)
        if self.ui.cb_export_bayer_as_npy.isChecked():
            outfname = os.path.join(self.ddtree.ddir, "output", "bayer.npy")
            np.save(outfname, self.jp.data)
        self.ui.pbar_export.setValue(25)
        if self.ui.cb_export_bayer_as_mat.isChecked():
            pass
        self.ui.pbar_export.setValue(50)
        if self.ui.cb_export_ref_CSV_simple.isChecked():
            tmpcsv = np.zeros((1000, 5), dtype=np.float64)
            #tmpcsv[:, 0] = self.jp.gray.rchan_759nm_calibrated.index.to_numpy(dtype=np.float64)[-1000:]
            tmpcsv[:, 0] = self.jp.gray.itp_hor_nm_array
            tmpcsv[:, 1] = self.jp.ref_fancy
            tmpcsv[:, 2] = self.jp.ref_fancy_normed if self.ui.cb_calc5_norm.isChecked() else 0
            tmpcsv[:, 3] = self.jp.obje_fancy_dn_bg_substracted
            tmpcsv[:, 4] = self.jp.gray_fancy_dn_bg_substracted
            outfname = os.path.join(os.path.join(self.ddtree.ddir, "output", datetime.now().strftime("refl_output_on_%Y%m%d_%H%M%S.csv")))
            logger.debug(f"short_cut_export_raw_jpeg: {outfname=}")
            np.savetxt(outfname,
                       tmpcsv,
                       ("%3.1f", "%2.5f", "%2.5f", "%3.2f", "%3.2f"),
                       header=f"wave, refl, refl_norm_{self.ui.sb_calc5_norm_zero.value()}_{self.ui.sb_calc5_norm_one.value()}, DN-obje(bg-substracted), DN-gray(bg-substracted)",
                       delimiter=",")
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
        self.repopulate_param_hist_combobox()

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
        self.ui.sb_lefx_init_rel.setValue(  self.dfParamHistory["lefx_init_rel"].astype(int).iloc[selected_row_num])
        self.ui.sb_lefx_size.setValue(      self.dfParamHistory["lefx_size"].astype(int).iloc[selected_row_num])
        self.ui.sb_rigx_init_rel.setValue(  self.dfParamHistory["rigx_init_rel"].astype(int).iloc[selected_row_num])
        self.ui.sb_rigx_size.setValue(      self.dfParamHistory["rigx_size"].astype(int).iloc[selected_row_num])
        self.ui.sb_gray_y_init.setValue(    self.dfParamHistory["gray_y_init"].astype(int).iloc[selected_row_num])
        self.ui.sb_gray_y_size.setValue(    self.dfParamHistory["gray_y_size"].astype(int).iloc[selected_row_num])
        self.ui.sb_obje_y_init.setValue(    self.dfParamHistory["obje_y_init"].astype(int).iloc[selected_row_num])
        self.ui.sb_obje_y_size.setValue(    self.dfParamHistory["obje_y_size"].astype(int).iloc[selected_row_num])
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
            "lefx_init_rel"    : [self.ui.sb_lefx_init_rel.value()],
            "lefx_size"        : [self.ui.sb_lefx_size.value()],
            "rigx_init_rel"    : [self.ui.sb_rigx_init_rel.value()],
            "rigx_size"        : [self.ui.sb_rigx_size.value()],
            "gray_y_init"      : [self.ui.sb_gray_y_init.value()],
            "gray_y_size"      : [self.ui.sb_gray_y_size.value()],
            "obje_y_init"      : [self.ui.sb_obje_y_init.value()],
            "obje_y_size"      : [self.ui.sb_obje_y_size.value()],
            "waveperpixel"     : [self.ui.sb_waveperpixel.value()],
            "calc1_desalt"     : [self.ui.cb_calc1_desalt.isChecked()],
            "calc2_background" : [self.ui.cb_calc2_background.isChecked()],
            "calc3_calibrate"  : [self.ui.cb_calc3_calibrate_759.isChecked()],
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
        # self.ui.sb_waveperpixel

    def pxlspec_to_pxlweb_formula(self, distance_in_cm: float, pxl_spec: int) -> float:
        return ( -0.212 + 0.316 / (distance_in_cm + 0.258)) * pxl_spec + 2351.944 / (distance_in_cm + 8.423) + 519.806

    def init_physical_repr_graph(self) -> None:
        #v = self.ui.graph_physical_orientation.addViewBox() # noqa # type: ignore
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
