# ---------- Base libraries -------------------------------------------------------------------------------------------
import os
import tempfile
import logging
import subprocess
import platform
from datetime import datetime
from pathlib import Path
import pyqtgraph as pg
import time

# ---------- Numerical Visual packages---------------------------------------------------------------------------------
import numpy as np
import cv2 as cv

# ---------- GUI libraries --------------------------------------------------------------------------------------------
from PySide6.QtWidgets import QMainWindow, QWidget, QFileSystemModel, QMessageBox
from PySide6.QtGui import QKeySequence, QShortcut, QColor
from PySide6.QtCore import QModelIndex, QDir, Qt

# ---------- Custom libs ----------------------------------------------------------------------------------------------
from Custom_UIs.UI_Mainwindow import Ui_MainWindow
from Custom_Libs.Lib_DataDirTree import DataDirTree
# from Custom_Widgets.Lib_PlotConfigDialog import PlotConfigDialog
from bps_raw_jpeg_processer.src.bps_raw_jpeg_processer import (
    JpegProcessor,  get_wavelength_array, background # desalt_2d_array_by_vertically_median_filter,
)

# ---------- Some logging ---------------------------------------------------------------------------------------------
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")


system_str = platform.system()

logging.basicConfig(
    filename= Path(tempfile.gettempdir()) / datetime.now().strftime("%Y%m%d_%H%M%S.log"),
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
)


def open_file_externally(filepath: str) -> None:
    """Opens given file externally, without hanging current running python script."""
    try:
        if system_str == "Windows":  # Windows
            os.startfile(filepath)  # type: ignore
        elif system_str == "Darwin":  # BSDs and macos
            subprocess.Popen(("open ", filepath), stdin=None, stdout=None, stderr=None, close_fds=True)  # shell=True,
        elif system_str == "Linux":  # linux variants
            subprocess.Popen(
                ("xdg-open", os.path.abspath(filepath)),  # shell=True,
                stdin=None,
                stdout=None,
                stderr=None,
                close_fds=True,
            )
        else:
            logging.warning(f"Strange os-platform string id: {system_str}")
            logging.warning(" - Cannot open file")
        return None
    except Exception as e:
        logging.warning(f"error when openning {filepath}:\n{e}")
        return None


class FileSystemModel(QFileSystemModel):
    # read from https://stackoverflow.com/a/40455027/14696853
    def __init__(self, *args, **kwargs):
        super(FileSystemModel, self).__init__(*args, **kwargs)
        #self.setNameFilters((["*.jpeg", "*.jpg", "*.json"]))
        self.setNameFilters((["*.jpeg"]))
        # , "*.tiff", "*.npy", "*.mat", "*.png"]))
        # self.setNameFilterDisables(False)
        # self.setNameFilterDisables(True)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.ForegroundRole:
            text = index.data(Qt.ItemDataRole.DisplayRole)
            if (".jpeg" in text) and (text.count("_") in (3, 4)) and text.replace(".jpeg", "").replace("_", "").isnumeric():
                return QColor("#58cd1c")

            elif text.count("_") == 1 and (len(text) == 15) and text.replace("_", "").isnumeric():
                return QColor("#288d4c")
        return super(FileSystemModel, self).data(index, role)

class TheMainWindow(QMainWindow):
    dir_path: str = QDir.homePath()
    jpeg_path: str
    help_html_path: str = os.path.join(QDir.currentPath(), "docs/help.html") # need change on the binary release?
    ddtree: DataDirTree = DataDirTree()
    jp: JpegProcessor = JpegProcessor()

    def __init__(self, parent: QWidget | None = None) -> None:
        super(TheMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pb_calibrate_calculate.clicked.connect(self.call_calibrate_and_calculate)
        self.ui.pb_export.clicked.connect(self.short_cut_export_raw_jpeg)
        self.ui.pb_dir_goto_parent.clicked.connect(self.short_cut_goto_parent_dir)
        #self.ui.cb_rawbayer_visual_demosiac.valueChanged(self.)
        self.ui.cb_rawbayer_visual_demosiac.stateChanged.connect(self.update_1_rawbayer_img_data_and_then_plot_below)
                                                         

        # --------------- initialize the file system ----------------------------------
        self.fsmodel = FileSystemModel()                     # prev. QFileSystemModel()
        self.fsmodel.setRootPath(QDir.homePath())

        self.ui.tv_dir.setModel(self.fsmodel)
        self.ui.tv_dir.setRootIndex(self.fsmodel.setRootPath(QDir.homePath()))
        self.short_cut_goto_parent_dir()
        self.ui.tv_dir.doubleClicked.connect(self.call_tv_onItemClicked)
        # self.ui.cb_ft_filter.stateChanged.connect(self.fsmodel.setNameFilterDisables)
        self.ui.cb_ft_filter.stateChanged.connect(self.toggle_filetype_visiblity)
        self.ui.cb_calc5_norm.stateChanged.connect(self.handle_cb_calc5_norming)
        self.ui.sb_calc5_norm_zero.valueChanged.connect(self.handle_cb_calc5_norming)
        self.ui.sb_calc5_norm_one.valueChanged.connect(self.handle_cb_calc5_norming)
        #self.ui.cb_bayer_show_geometry.stateChanged.connect(self.update_visual_1_rawbayer_img_section)
        self.ui.pb_waveperpixel_reset.clicked.connect(lambda: self.ui.sb_waveperpixel.setValue(1.8385))

        # -----------------------------------------------------------------------------
        #self.jp.set_xWaveRng(self.ui.sb_midx_init.value())
        #self.jp.set_yGrayRng((self.ui.sb_gray_y_init.value(), self.ui.sb_gray_y_init.value() + self.ui.sb_gray_y_size.value())) # noqa
        #self.jp.set_yObjeRng((self.ui.sb_obje_y_init.value(), self.ui.sb_obje_y_init.value() + self.ui.sb_obje_y_size.value())) # noqa

        self.init_2d_graph_hide_the_original_roi_buttons()
        self.init_all_6_roi()
        self.init_sb_signals_for_ROI_controls()
        self.init_all_pyqtgraph()

        self.init_keyboard_bindings()
        self.init_actions()

    def init_2d_graph_hide_the_original_roi_buttons(self) -> None:
        """Hides the ROI/Menu buttons from the 3 images"""
        self.ui.graph_2dimg.ui.roiBtn.hide()
        self.ui.graph_2dimg.ui.menuBtn.hide()

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

        self.ui.graph_2dimg.addItem(self.roi_label_obje)
        self.ui.graph_2dimg.addItem(self.roi_label_gray)

    def init_all_6_roi(self) -> None:
        """Initializes ROI"""

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


        self.roi_obje_main.addScaleHandle([0.5, 1], [0.5, 0])
        self.roi_gray_main.addScaleHandle([0.5, 1], [0.5, 0])

        self.roi_obje_main.setZValue(10)
        self.roi_gray_main.setZValue(10)

        self.roi_gray_bglf.addScaleHandle([0, 0.5], [1, 0.5])
        self.roi_gray_bglf.addScaleHandle([1, 0.5], [0, 0.5])
        self.roi_gray_bgri.addScaleHandle([1, 0.5], [0, 0.5])
        self.roi_gray_bgri.addScaleHandle([0, 0.5], [1, 0.5])
        self.roi_gray_bglf.setZValue(10)
        self.roi_gray_bgri.setZValue(10)

        self.roi_obje_bglf.addScaleHandle([0, 0.5], [1, 0.5])
        self.roi_obje_bglf.addScaleHandle([1, 0.5], [0, 0.5])
        self.roi_obje_bgri.addScaleHandle([1, 0.5], [0, 0.5])
        self.roi_obje_bgri.addScaleHandle([0, 0.5], [1, 0.5])
        self.roi_obje_bglf.setZValue(10)
        self.roi_obje_bgri.setZValue(10)


        self.ui.graph_2dimg.addItem(self.roi_obje_main)
        self.ui.graph_2dimg.addItem(self.roi_obje_bgri)
        self.ui.graph_2dimg.addItem(self.roi_obje_bglf)
        self.ui.graph_2dimg.addItem(self.roi_gray_main)
        self.ui.graph_2dimg.addItem(self.roi_gray_bglf)
        self.ui.graph_2dimg.addItem(self.roi_gray_bgri)

        self.graph_759nm_line_for_2dimg = pg.InfiniteLine(
            pos=192*2 + self.ui.sb_midx_init.value(), movable=False, angle=90, label="759.3nm", 
            #labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True}
        )
        self.ui.graph_2dimg.addItem(self.graph_759nm_line_for_2dimg)
        
        self.graph_desalted_graphs_sep_line_y0 = pg.InfiniteLine(pos=0, movable=False, angle=0)
        self.graph_desalted_graphs_sep_line_x0 = pg.InfiniteLine(pos=0, movable=False, angle=90)
        self.graph_desalted_graphs_sep_line_x1 = pg.InfiniteLine(pos=0, movable=False, angle=90)
        self.ui.graph_calc1_desalted_roi.addItem(self.graph_desalted_graphs_sep_line_y0)
        self.ui.graph_calc1_desalted_roi.addItem(self.graph_desalted_graphs_sep_line_x0)
        self.ui.graph_calc1_desalted_roi.addItem(self.graph_desalted_graphs_sep_line_x1)



        self.text_for_desalted_img_label0 = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">BG-Gray</span></div>',   anchor=(0, 0), border="w", fill=(100, 100, 100, 100))
        self.text_for_desalted_img_label1 = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">Gray</span></div>',      anchor=(0, 0), border="w", fill=(200,  50,  50, 100))
        self.text_for_desalted_img_label2 = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">BG-Gray</span></div>',   anchor=(0, 0), border="w", fill=(100, 100, 100, 100))
        self.text_for_desalted_img_label3 = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">BG-Object</span></div>', anchor=(0, 0), border="w", fill=(100, 100, 100, 100))
        self.text_for_desalted_img_label4 = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">Object</span></div>',    anchor=(0, 0), border="w", fill=(50,   50, 200, 100))
        self.text_for_desalted_img_label5 = pg.TextItem(html='<div style="text-align: center"><span style="color: #FFF;">BG-Object</span></div>', anchor=(0, 0), border="w", fill=(100, 100, 100, 100))

        self.ui.graph_calc1_desalted_roi.addItem(self.text_for_desalted_img_label0)
        self.ui.graph_calc1_desalted_roi.addItem(self.text_for_desalted_img_label1)
        self.ui.graph_calc1_desalted_roi.addItem(self.text_for_desalted_img_label2)
        self.ui.graph_calc1_desalted_roi.addItem(self.text_for_desalted_img_label3)
        self.ui.graph_calc1_desalted_roi.addItem(self.text_for_desalted_img_label4)
        self.ui.graph_calc1_desalted_roi.addItem(self.text_for_desalted_img_label5)

    def init_sb_signals_for_ROI_controls(self) -> None:
        self.ui.sb_gray_y_init.valueChanged.connect(self.update_raw_from_sb)
        self.ui.sb_gray_y_size.valueChanged.connect(self.update_raw_from_sb)
        self.ui.sb_obje_y_init.valueChanged.connect(self.update_raw_from_sb)
        self.ui.sb_obje_y_size.valueChanged.connect(self.update_raw_from_sb)
        self.ui.sb_midx_init.valueChanged.connect(self.update_raw_from_sb)
        self.ui.sb_midx_size.valueChanged.connect(self.update_raw_from_sb)
        self.ui.sb_lefx_init_rel.valueChanged.connect(self.update_raw_from_sb)
        self.ui.sb_lefx_size.valueChanged.connect(self.update_raw_from_sb)
        self.ui.sb_rigx_init_rel.valueChanged.connect(self.update_raw_from_sb)
        self.ui.sb_rigx_size.valueChanged.connect(self.update_raw_from_sb)

        self.ui.sb_waveperpixel.valueChanged.connect(self.update_raw_roi_plot_when_sb_or_roi_moved)

        self.roi_gray_main.sigRegionChanged.connect(lambda: self.handle_roi_change("gray", "middle"))
        self.roi_gray_bglf.sigRegionChanged.connect(lambda: self.handle_roi_change("gray", "left"))
        self.roi_gray_bgri.sigRegionChanged.connect(lambda: self.handle_roi_change("gray", "right"))

        self.roi_obje_main.sigRegionChanged.connect(lambda: self.handle_roi_change("obje", "middle"))
        self.roi_obje_bglf.sigRegionChanged.connect(lambda: self.handle_roi_change("obje", "left"))
        self.roi_obje_bgri.sigRegionChanged.connect(lambda: self.handle_roi_change("obje", "right"))

    def init_all_pyqtgraph(self) -> None:
        # -------------------------------------------------------------------------------------------------------------
        self.ui.graph_calc2_bg_gray.addLegend()
        self.ui.graph_calc2_bg_obje.addLegend()

        self.ui.graph_calc2_bg_gray.setLabel("left",   "Background",             units="DN")
        self.ui.graph_calc2_bg_gray.setLabel("bottom", "Wavelenght",             units="nm")
        self.ui.graph_calc2_bg_gray.setLabel("top",    "Gray Region Background")

        self.ui.graph_calc2_bg_obje.setLabel("left",   "Background", units="DN")
        self.ui.graph_calc2_bg_obje.setLabel("bottom", "Wavelenght", units="nm")
        self.ui.graph_calc2_bg_obje.setLabel("top",    "Object Region Background")


        self.graph2_curve_bg_gray_le_r = self.ui.graph_calc2_bg_gray.plot(symbol="o", symbolSize=9, symbolBrush=(255, 000, 000), pen=None, name="R-gray-left")
        self.graph2_curve_bg_gray_le_g = self.ui.graph_calc2_bg_gray.plot(symbol="o", symbolSize=9, symbolBrush=(000, 255, 000), pen=None, name="G-gray-left")
        self.graph2_curve_bg_gray_le_b = self.ui.graph_calc2_bg_gray.plot(symbol="o", symbolSize=9, symbolBrush=(000, 000, 255), pen=None, name="B-gray-left")
        self.graph2_curve_bg_gray_re_r = self.ui.graph_calc2_bg_gray.plot(symbol="x", symbolSize=9, symbolBrush=(255, 000, 000), pen=None, name="R-gray-right")
        self.graph2_curve_bg_gray_re_g = self.ui.graph_calc2_bg_gray.plot(symbol="x", symbolSize=9, symbolBrush=(000, 255, 000), pen=None, name="G-gray-right")
        self.graph2_curve_bg_gray_re_b = self.ui.graph_calc2_bg_gray.plot(symbol="x", symbolSize=9, symbolBrush=(000, 000, 255), pen=None, name="B-gray-right")
        self.graph2_curve_bg_gray_mi_r = self.ui.graph_calc2_bg_gray.plot(pen=pg.mkPen("r", width=0, style=Qt.PenStyle.SolidLine), name="Estimated-R-bg")
        self.graph2_curve_bg_gray_mi_g = self.ui.graph_calc2_bg_gray.plot(pen=pg.mkPen("g", width=0, style=Qt.PenStyle.SolidLine), name="Estimated-G-bg")
        self.graph2_curve_bg_gray_mi_b = self.ui.graph_calc2_bg_gray.plot(pen=pg.mkPen("b", width=0, style=Qt.PenStyle.SolidLine), name="Estimated-B-bg")


        self.graph2_curve_bg_obje_le_r = self.ui.graph_calc2_bg_obje.plot(symbol="o", symbolSize=9, symbolBrush=(255, 000, 000), pen=None, name="R-obje-left")
        self.graph2_curve_bg_obje_le_g = self.ui.graph_calc2_bg_obje.plot(symbol="o", symbolSize=9, symbolBrush=(000, 255, 000), pen=None, name="G-obje-left")
        self.graph2_curve_bg_obje_le_b = self.ui.graph_calc2_bg_obje.plot(symbol="o", symbolSize=9, symbolBrush=(000, 000, 255), pen=None, name="B-obje-left")
        self.graph2_curve_bg_obje_ri_r = self.ui.graph_calc2_bg_obje.plot(symbol="x", symbolSize=9, symbolBrush=(255, 000, 000), pen=None, name="R-obje-right")
        self.graph2_curve_bg_obje_ri_g = self.ui.graph_calc2_bg_obje.plot(symbol="x", symbolSize=9, symbolBrush=(000, 255, 000), pen=None, name="G-obje-right")
        self.graph2_curve_bg_obje_ri_b = self.ui.graph_calc2_bg_obje.plot(symbol="x", symbolSize=9, symbolBrush=(000, 000, 255), pen=None, name="B-obje-right")
        self.graph2_curve_bg_obje_mi_r = self.ui.graph_calc2_bg_obje.plot(pen=pg.mkPen("r", width=0, style=Qt.PenStyle.SolidLine), name="Estimated-R-bg")
        self.graph2_curve_bg_obje_mi_g = self.ui.graph_calc2_bg_obje.plot(pen=pg.mkPen("g", width=0, style=Qt.PenStyle.SolidLine), name="Estimated-G-bg")
        self.graph2_curve_bg_obje_mi_b = self.ui.graph_calc2_bg_obje.plot(pen=pg.mkPen("b", width=0, style=Qt.PenStyle.SolidLine), name="Estimated-B-bg")

        # --------graph 3:  759 calibration curves ---------------------------------------------------------------------
        self.ui.graph_calc3_759_calib.clear()
        self.ui.graph_calc3_759_calib.addLegend()
        self.ui.graph_calc3_759_calib.addItem(
            pg.InfiniteLine(
                pos=759.3,
                movable=False, angle=90, 
                label="x={value:0.2f}nm", 
                labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True}))

        self.ui.graph_calc3_759_calib.setLabel("left",   "Digital Number", units="DN")
        self.ui.graph_calc3_759_calib.setLabel("bottom", "Wavelength",     units="nm")
        self.ui.graph_calc3_759_calib.setLabel("top",    "After 759nm calibration")

        self.graph3_curve_759_calib_gray_r = self.ui.graph_calc3_759_calib.plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine), name="R-gray")
        self.graph3_curve_759_calib_gray_g = self.ui.graph_calc3_759_calib.plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="G-gray")
        self.graph3_curve_759_calib_gray_b = self.ui.graph_calc3_759_calib.plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine), name="B-gray")
        self.graph3_curve_759_calib_obje_r = self.ui.graph_calc3_759_calib.plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DashLine),  name="R-object")
        self.graph3_curve_759_calib_obje_g = self.ui.graph_calc3_759_calib.plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine),  name="G-object")
        self.graph3_curve_759_calib_obje_b = self.ui.graph_calc3_759_calib.plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DashLine),  name="B-object")
        self.graph3_curve_759_calib_gray_r_bg = self.ui.graph_calc3_759_calib.plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DotLine),  name="BG: R-gray")
        self.graph3_curve_759_calib_gray_g_bg = self.ui.graph_calc3_759_calib.plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DotLine),  name="BG: G-gray")
        self.graph3_curve_759_calib_gray_b_bg = self.ui.graph_calc3_759_calib.plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DotLine),  name="BG: B-gray")
        self.graph3_curve_759_calib_obje_r_bg = self.ui.graph_calc3_759_calib.plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DotLine),  name="BG: R-object")
        self.graph3_curve_759_calib_obje_g_bg = self.ui.graph_calc3_759_calib.plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DotLine),  name="BG: G-object")
        self.graph3_curve_759_calib_obje_b_bg = self.ui.graph_calc3_759_calib.plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DotLine),  name="BG: B-object")

        # --------graph 4:  rgb refl  ---------------------------------------------------------------------
        self.ui.graph_calc4_refl_rgb.clear()
        self.ui.graph_calc4_refl_rgb.addLegend()
        self.ui.graph_calc4_refl_rgb.addItem(
            pg.InfiniteLine(
                pos=759.3,
                movable=False, angle=90, 
                label="x={value:0.2f}nm", 
                labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True}))

        self.ui.graph_calc4_refl_rgb.setLabel("left",   "Reflection")
        self.ui.graph_calc4_refl_rgb.setLabel("bottom", "Wavelength",     units="nm")
        self.ui.graph_calc4_refl_rgb.setLabel("top",    "Reflection RGB 3 channels")

        self.graph4_curve_relf_r = self.ui.graph_calc4_refl_rgb.plot(pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine), name="R-refl")
        self.graph4_curve_relf_g = self.ui.graph_calc4_refl_rgb.plot(pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="G-refl")
        self.graph4_curve_relf_b = self.ui.graph_calc4_refl_rgb.plot(pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine), name="B-refl")

        # --------graph 5:  rgb     ---------------------------------------------------------------------
        self.ui.graph_calc5_refl_final.clear()
        self.ui.graph_calc5_refl_final.addLegend()

        self.graph5_norm_zero_line = pg.InfiniteLine(
                pos=self.ui.sb_calc5_norm_zero.value(),
                movable=False, angle=90, 
                label="x={value:0.2f}nm", 
                labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True})
        self.graph5_norm_one_line = pg.InfiniteLine(
                pos=self.ui.sb_calc5_norm_one.value(),
                movable=False, angle=90, 
                label="x={value:0.2f}nm", 
                labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True})

        self.ui.graph_calc5_refl_final.setLabel("left",   "Reflection")
        self.ui.graph_calc5_refl_final.setLabel("bottom", "Wavelength",     units="nm")
        self.ui.graph_calc5_refl_final.setLabel("top",    "Reflection")

        self.ui.graph_calc5_refl_final.addItem(self.graph5_norm_one_line)
        self.ui.graph_calc5_refl_final.addItem(self.graph5_norm_zero_line)
        self.graph5_curve_relf = self.ui.graph_calc5_refl_final.plot(pen=pg.mkPen("k", width=1, style=Qt.PenStyle.SolidLine), name="Reflection")
        

    def all_sb_signal_enable_or_disable(self, b: bool) -> None:
        """Temporaray block or not block the signals in order to 2 way control"""
        self.ui.sb_lefx_size.blockSignals(b)
        self.ui.sb_lefx_init_rel.blockSignals(b)
        self.ui.sb_lefx_ends.blockSignals(b)
        self.ui.sb_rigx_size.blockSignals(b)
        self.ui.sb_rigx_init_rel.blockSignals(b)
        self.ui.sb_rigx_ends.blockSignals(b)
        self.ui.sb_midx_init.blockSignals(b)
        self.ui.sb_midx_size.blockSignals(b)
        self.ui.sb_midx_ends.blockSignals(b)
        self.ui.sb_gray_y_init.blockSignals(b)
        self.ui.sb_gray_y_size.blockSignals(b)
        self.ui.sb_gray_y_ends.blockSignals(b)
        self.ui.sb_obje_y_init.blockSignals(b)
        self.ui.sb_obje_y_size.blockSignals(b)
        self.ui.sb_obje_y_ends.blockSignals(b)
    
    def handle_roi_change(self, gray_or_obje: str, left_middle_right: str) -> None:
        self.all_sb_signal_enable_or_disable(True)
        print(self.roi_gray_main.getState()["pos"], self.roi_gray_bglf.getState()["pos"])

        if gray_or_obje == "gray":
            if left_middle_right == "middle":
                self.ui.sb_midx_init.setValue(self.roi_gray_main.getState()["pos"].x() )
                self.ui.sb_midx_size.setValue(self.roi_gray_main.getState()["size"].x())
                self.ui.sb_gray_y_init.setValue(self.roi_gray_main.getState()["pos"].y() )
                self.ui.sb_gray_y_size.setValue(self.roi_gray_main.getState()["size"].y())
                #self.ui.sb_midx_ends.setValue()
            elif left_middle_right == "left":
                self.ui.sb_lefx_init_rel.setValue(- self.roi_gray_main.getState()["pos"].x() + self.roi_gray_bglf.getState()["pos"].x())
                self.ui.sb_lefx_size.setValue(self.roi_gray_bglf.getState()["size"].x())
            elif left_middle_right == "right":
                self.ui.sb_rigx_init_rel.setValue(- self.roi_gray_main.getState()["pos"].x() + self.roi_gray_bgri.getState()["pos"].x())
                self.ui.sb_rigx_size.setValue(self.roi_gray_bgri.getState()["size"].x())
        elif gray_or_obje == "obje":
            if left_middle_right == "middle":
                self.ui.sb_midx_init.setValue(self.roi_obje_main.getState()["pos"].x() )
                self.ui.sb_midx_size.setValue(self.roi_obje_main.getState()["size"].x())
                self.ui.sb_obje_y_init.setValue(self.roi_obje_main.getState()["pos"].y() )
                self.ui.sb_obje_y_size.setValue(self.roi_obje_main.getState()["size"].y())
                #self.ui.sb_midx_ends.setValue()
            elif left_middle_right == "left":
                self.ui.sb_lefx_init_rel.setValue(- self.roi_gray_main.getState()["pos"].x() + self.roi_obje_bglf.getState()["pos"].x())
                self.ui.sb_lefx_size.setValue(self.roi_obje_bglf.getState()["size"].x())
            elif left_middle_right == "right":
                self.ui.sb_rigx_init_rel.setValue(- self.roi_gray_main.getState()["pos"].x() + self.roi_obje_bgri.getState()["pos"].x())
                self.ui.sb_rigx_size.setValue(self.roi_obje_bgri.getState()["size"].x())

        self.all_sb_signal_enable_or_disable(False)
        self.update_raw_from_sb()


    def update_raw_from_sb(self) -> None:
        self.roi_gray_main.blockSignals(True)
        self.roi_gray_bglf.blockSignals(True)
        self.roi_gray_bgri.blockSignals(True)
        self.roi_obje_main.blockSignals(True)
        self.roi_obje_bglf.blockSignals(True)
        self.roi_obje_bgri.blockSignals(True)

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

        self.roi_gray_main.blockSignals(False)
        self.roi_gray_bglf.blockSignals(False)
        self.roi_gray_bgri.blockSignals(False)
        self.roi_obje_main.blockSignals(False)
        self.roi_obje_bglf.blockSignals(False)
        self.roi_obje_bgri.blockSignals(False)
        
        # change the label position
        self.roi_label_gray.setPos(self.ui.sb_midx_init.value(), self.ui.sb_gray_y_init.value())
        self.roi_label_obje.setPos(self.ui.sb_midx_init.value(), self.ui.sb_obje_y_init.value())

        self.update_raw_roi_plot_when_sb_or_roi_moved()
    
    def update_raw_roi_plot_when_sb_or_roi_moved(self) -> None:
        """update raw dn plot, when either spinbox or ROI dragged"""
        self.ui.graph_raw.clear()
        self.ui.graph_raw.addLegend()

        inf1 = pg.InfiniteLine(
            pos=759.3,
            movable=False, angle=90, 
            label="x={value:0.2f}nm", 
            labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True}
        )
        self.ui.graph_raw.addItem(inf1)

        tmp_x = get_wavelength_array(
            init_pxl=0,
            pxl_size=350,
            waveperpixel=self.ui.sb_waveperpixel.value(),
        )

        gray_roi_mid = self.jp.data[
            self.ui.sb_gray_y_init.value() : self.ui.sb_gray_y_init.value() + self.ui.sb_gray_y_size.value(),
            self.ui.sb_midx_init.value()   : self.ui.sb_midx_init.value()   + self.ui.sb_midx_size.value()
        ]
        obje_roi_mid = self.jp.data[
            self.ui.sb_obje_y_init.value() : self.ui.sb_obje_y_init.value() + self.ui.sb_obje_y_size.value(),
            self.ui.sb_midx_init.value()   : self.ui.sb_midx_init.value()   + self.ui.sb_midx_size.value()
        ]

        self.ui.graph_raw.plot(tmp_x, gray_roi_mid[1::2, 1::2].mean(axis=0), pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine), name="R-gray")
        self.ui.graph_raw.plot(tmp_x, gray_roi_mid[1::2, 0::2].mean(axis=0), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="G-gray")
        self.ui.graph_raw.plot(tmp_x, gray_roi_mid[0::2, 1::2].mean(axis=0), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="G-gray")
        self.ui.graph_raw.plot(tmp_x, gray_roi_mid[0::2, 0::2].mean(axis=0), pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine), name="B-gray")

        self.ui.graph_raw.plot(tmp_x, obje_roi_mid[1::2, 1::2].mean(axis=0), pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DashLine), name="R-object")
        self.ui.graph_raw.plot(tmp_x, obje_roi_mid[1::2, 0::2].mean(axis=0), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine), name="G-object")
        self.ui.graph_raw.plot(tmp_x, obje_roi_mid[0::2, 1::2].mean(axis=0), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine), name="G-object")
        self.ui.graph_raw.plot(tmp_x, obje_roi_mid[0::2, 0::2].mean(axis=0), pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DashLine), name="B-object")


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

        self.ui.graph_raw.plot(tmp_lef_x, gray_roi_lef[1::2, 1::2].mean(axis=0), pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine), name="bgR-gray")
        self.ui.graph_raw.plot(tmp_lef_x, gray_roi_lef[1::2, 0::2].mean(axis=0), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="bgG-gray")
        self.ui.graph_raw.plot(tmp_lef_x, gray_roi_lef[0::2, 1::2].mean(axis=0), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="bgG-gray")
        self.ui.graph_raw.plot(tmp_lef_x, gray_roi_lef[0::2, 0::2].mean(axis=0), pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine), name="bgB-gray")

        self.ui.graph_raw.plot(tmp_rig_x, gray_roi_rig[1::2, 1::2].mean(axis=0), pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DashLine), name="bgR-object")
        self.ui.graph_raw.plot(tmp_rig_x, gray_roi_rig[1::2, 0::2].mean(axis=0), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine), name="bgG-object")
        self.ui.graph_raw.plot(tmp_rig_x, gray_roi_rig[0::2, 1::2].mean(axis=0), pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine), name="bgG-object")
        self.ui.graph_raw.plot(tmp_rig_x, gray_roi_rig[0::2, 0::2].mean(axis=0), pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DashLine), name="bgB-object")
        

    def handle_cb_calc5_norming(self) -> None:
        print("i was clicked")
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
        QShortcut(QKeySequence("Ctrl+B"),    self).activated.connect(self.short_cut_goto_parent_dir)
        QShortcut(QKeySequence("Backspace"), self).activated.connect(self.short_cut_goto_parent_dir)
        QShortcut(QKeySequence("Return"),    self).activated.connect(self.short_cut_goto_selected_child_dir)

        QShortcut(QKeySequence("Space"),     self).activated.connect(self.short_cut_preview_raw_jpeg)
        QShortcut(QKeySequence("Ctrl+R"),    self).activated.connect(self.call_calibrate_and_calculate)
        QShortcut(QKeySequence("Ctrl+E"),    self).activated.connect(self.short_cut_export_raw_jpeg)
        QShortcut(QKeySequence("Ctrl+O"),    self).activated.connect(self.short_cut_open_at_point)
        QShortcut(QKeySequence("Ctrl+H"),    self).activated.connect(self.open_help_page)
        QShortcut(QKeySequence("Ctrl+F"),    self).activated.connect(self.ui.cb_ft_filter.toggle)

    def init_actions(self) -> None:
        self.ui.action_help.triggered.connect(self.open_help_page)
        # self.ui.action_dir_cur_child_fold.connect( #lambda self.ui.tv_dir.collapse())
        # self.ui.action_dir_cur_child_unfold.connect(self.ui.tv_dir.)

        self.ui.action_dir_goto_cur_child.triggered.connect(self.short_cut_goto_selected_child_dir)
        self.ui.action_dir_goto_parent.triggered.connect(self.short_cut_goto_parent_dir)
        self.ui.action_dir_ft_filter_toggle.triggered.connect(self.ui.cb_ft_filter.toggle)

        self.ui.action_cur_jpeg_export.triggered.connect(self.short_cut_export_raw_jpeg)
        self.ui.action_cur_jpeg_preview.triggered.connect(self.short_cut_preview_raw_jpeg)
        self.ui.action_cur_file_open.triggered.connect(self.short_cut_open_at_point)

    def open_help_page(self) -> None:
        """Opens help page."""
        open_file_externally(self.help_html_path)

    def short_cut_goto_parent_dir(self) -> None:
        """Go to parent directory, Backspace"""
        logging.info("going to parent file")
        cur_root_index = self.ui.tv_dir.rootIndex()  # get .
        parent_of_cur_root_index = self.fsmodel.parent(cur_root_index)  # get ..
        self.ui.tv_dir.setRootIndex(parent_of_cur_root_index)  # set ..
        self.ui.tv_dir.setCurrentIndex(parent_of_cur_root_index)  # idk why this needed

    def short_cut_goto_selected_child_dir(self) -> None:
        """Enter: the directory"""
        sel_m_index = self.ui.tv_dir.currentIndex()  # get
        if self.fsmodel.hasChildren(sel_m_index):  # enter only if this has children
            self.ui.tv_dir.setRootIndex(sel_m_index)
        else:
            pass  # need to update jpeg_path here

    def short_cut_open_at_point(self) -> None:
        """C-o: opens file externally"""
        sel_m_index = self.ui.tv_dir.currentIndex()
        tmppath = self.fsmodel.filePath(sel_m_index)
        open_file_externally(tmppath)

    def short_cut_preview_raw_jpeg(self) -> bool:
        """SPC"""
        sel_m_index = self.ui.tv_dir.currentIndex()
        tmppath = self.fsmodel.filePath(sel_m_index)
        basename = os.path.basename(tmppath)
        logging.info("space press "+ tmppath)
        if not os.path.isfile(tmppath):
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Wrong File selected")
            dlg.setText("Selected item is not a file.\n if this is directory/folder press ENTER to go inside of this folder")
            dlg.exec()
            return False
        if not ((".jpeg" in basename) and (basename.count("_") in (3, 4))):
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Wrong File selected")
            dlg.setText("Selected item  is not JPEG file,\nPlease select JPEG file and try again")
            dlg.exec()
            return False

        self.jpeg_path = tmppath
        self.dir_path = os.path.dirname(self.jpeg_path)
        self.ddtree.set_ddir(self.dir_path)
        self.ui.tb_meta_json.setText(self.ddtree.metajsonText)
        self.ui.limg_webcam.show_np_img(
            cv.imread(self.ddtree.webcamFP).astype(np.uint8)[:, :, ::-1]
            if os.path.isfile(self.ddtree.webcamFP)
            else np.zeros((10, 10, 3), dtype=np.uint8)
        )
        self.jp.load_jpeg_file(self.jpeg_path, also_get_rgb_rerp=True)
        self.update_1_rawbayer_img_data_and_then_plot_below()
        return True

    def call_tv_onItemClicked(self, v: QModelIndex):
        tmp = self.fsmodel.filePath(v)
        if os.path.isdir(tmp):
            logging.info(f"call_tv_onItemClicked: {tmp}")
            self.ui.tv_dir.setRootIndex(v)
            logging.info(self.fsmodel.rootPath())
        else:
            self.jpeg_path = self.fsmodel.filePath(v)
            self.dir_path = os.path.dirname(self.jpeg_path)
            logging.info(self.dir_path + "\t" + self.jpeg_path)
            self.ddtree.set_ddir(self.dir_path)
            self.ui.tb_meta_json.setText(self.ddtree.metajsonText)
            self.ui.limg_webcam.show_np_img(
                cv.imread(self.ddtree.webcamFP).astype(np.uint8)[:, :, ::-1])
            #self.jp_load_newly_selected_jpeg_file()
            self.jp.load_jpeg_file(self.jpeg_path, also_get_rgb_rerp=True)
            self.update_1_rawbayer_img_data_and_then_plot_below()

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

        self.call_calibrate_and_calculate_calc4_rgb_refl()
        self.ui.pbar_calc.setValue(75)
        self.ui.tabWidget.setCurrentIndex(3)
        time.sleep(.1)

        self.call_calibrate_and_calculate_calc5_refl_n_norm()
        self.ui.pbar_calc.setValue(100)
        self.ui.tabWidget.setCurrentIndex(4)
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
        desalted_concatted_bayer_rgb_all_6roi = np.zeros((desaltedimg.shape[0], desaltedimg.shape[1], 3), dtype=np.int64)
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
        self.jp.background_calculation()
        
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

        self.graph2_curve_bg_gray_le_r.setData(tmp_lef_x, self.jp.gray_bgle.rchan["dn"].values[:self.jp.gray_bgle.raw_hor_pxl]) 
        self.graph2_curve_bg_gray_le_g.setData(tmp_lef_x, self.jp.gray_bgle.gchan["dn"].values[:self.jp.gray_bgle.raw_hor_pxl]) 
        self.graph2_curve_bg_gray_le_b.setData(tmp_lef_x, self.jp.gray_bgle.bchan["dn"].values[:self.jp.gray_bgle.raw_hor_pxl]) 
        self.graph2_curve_bg_gray_re_r.setData(tmp_rig_x, self.jp.gray_bgri.rchan["dn"].values[:self.jp.gray_bgri.raw_hor_pxl]) 
        self.graph2_curve_bg_gray_re_g.setData(tmp_rig_x, self.jp.gray_bgri.gchan["dn"].values[:self.jp.gray_bgri.raw_hor_pxl]) 
        self.graph2_curve_bg_gray_re_b.setData(tmp_rig_x, self.jp.gray_bgri.bchan["dn"].values[:self.jp.gray_bgri.raw_hor_pxl]) 

        self.graph2_curve_bg_obje_le_r.setData(tmp_lef_x, self.jp.obje_bgle.rchan["dn"].values[:self.jp.obje_bgle.raw_hor_pxl]) 
        self.graph2_curve_bg_obje_le_g.setData(tmp_lef_x, self.jp.obje_bgle.gchan["dn"].values[:self.jp.obje_bgle.raw_hor_pxl]) 
        self.graph2_curve_bg_obje_le_b.setData(tmp_lef_x, self.jp.obje_bgle.bchan["dn"].values[:self.jp.obje_bgle.raw_hor_pxl]) 
        self.graph2_curve_bg_obje_ri_r.setData(tmp_rig_x, self.jp.obje_bgri.rchan["dn"].values[:self.jp.obje_bgri.raw_hor_pxl]) 
        self.graph2_curve_bg_obje_ri_g.setData(tmp_rig_x, self.jp.obje_bgri.gchan["dn"].values[:self.jp.obje_bgri.raw_hor_pxl]) 
        self.graph2_curve_bg_obje_ri_b.setData(tmp_rig_x, self.jp.obje_bgri.bchan["dn"].values[:self.jp.obje_bgri.raw_hor_pxl]) 

        tmp_bgx = np.arange(tmp_lef_x.min(), tmp_rig_x.max(), 1)

        self.graph2_curve_bg_gray_mi_r.setData(tmp_bgx, background(tmp_bgx, *(self.jp.bg_gray_r_popt)))
        self.graph2_curve_bg_gray_mi_g.setData(tmp_bgx, background(tmp_bgx, *(self.jp.bg_gray_g_popt)))
        self.graph2_curve_bg_gray_mi_b.setData(tmp_bgx, background(tmp_bgx, *(self.jp.bg_gray_b_popt)))
        self.graph2_curve_bg_obje_mi_r.setData(tmp_bgx, background(tmp_bgx, *(self.jp.bg_obje_r_popt)))
        self.graph2_curve_bg_obje_mi_g.setData(tmp_bgx, background(tmp_bgx, *(self.jp.bg_obje_g_popt)))
        self.graph2_curve_bg_obje_mi_b.setData(tmp_bgx, background(tmp_bgx, *(self.jp.bg_obje_b_popt)))


    def call_calibrate_and_calculate_calc3_759_calib(self) -> None:
        self.jp.calibrate_n_calculate_final_output()
        tmp_x = self.jp.gray.rchan_759nm_calibrated.index[-1000:]
        self.graph3_curve_759_calib_gray_r.setData(tmp_x, np.array(self.jp.gray.rchan_759nm_calibrated["final"])[-1000:])
        self.graph3_curve_759_calib_gray_g.setData(tmp_x, np.array(self.jp.gray.gchan_759nm_calibrated["final"])[-1000:])
        self.graph3_curve_759_calib_gray_b.setData(tmp_x, np.array(self.jp.gray.bchan_759nm_calibrated["final"])[-1000:])
        self.graph3_curve_759_calib_obje_r.setData(tmp_x, np.array(self.jp.obje.rchan_759nm_calibrated["final"])[-1000:])
        self.graph3_curve_759_calib_obje_g.setData(tmp_x, np.array(self.jp.obje.gchan_759nm_calibrated["final"])[-1000:])
        self.graph3_curve_759_calib_obje_b.setData(tmp_x, np.array(self.jp.obje.bchan_759nm_calibrated["final"])[-1000:])

        self.graph3_curve_759_calib_gray_r_bg.setData(tmp_x, background(tmp_x, *(self.jp.bg_gray_r_popt)))
        self.graph3_curve_759_calib_gray_g_bg.setData(tmp_x, background(tmp_x, *(self.jp.bg_gray_g_popt)))
        self.graph3_curve_759_calib_gray_b_bg.setData(tmp_x, background(tmp_x, *(self.jp.bg_gray_b_popt)))
        self.graph3_curve_759_calib_obje_r_bg.setData(tmp_x, background(tmp_x, *(self.jp.bg_obje_r_popt)))
        self.graph3_curve_759_calib_obje_g_bg.setData(tmp_x, background(tmp_x, *(self.jp.bg_obje_g_popt)))
        self.graph3_curve_759_calib_obje_b_bg.setData(tmp_x, background(tmp_x, *(self.jp.bg_obje_b_popt)))
    
    def call_calibrate_and_calculate_calc4_rgb_refl(self) -> None:
        self.jp.fancy_reflectance()
        tmp_x = self.jp.gray.rchan_759nm_calibrated.index[-1000:]
        self.graph4_curve_relf_r.setData(tmp_x, self.jp.ref_fancy_r) # noqa
        self.graph4_curve_relf_g.setData(tmp_x, self.jp.ref_fancy_g) # noqa
        self.graph4_curve_relf_b.setData(tmp_x, self.jp.ref_fancy_b) # noqa


    def call_calibrate_and_calculate_calc5_refl_n_norm(self) -> None:
        self.jp.fancy_reflectance()
        tmp_x = self.jp.gray.rchan_759nm_calibrated.index[-1000:]

        if not self.ui.cb_calc5_norm.isChecked():
            self.graph5_curve_relf.setData(tmp_x, self.jp.ref_fancy)
        else:
            zero_index = int((self.ui.sb_calc5_norm_zero.value() - 400) / 0.5)
            one_index = int((self.ui.sb_calc5_norm_one.value() - 400 )/ 0.5)
            self.jp.normalize_the_fancy(zero_index, one_index)
            self.graph5_curve_relf.setData(tmp_x, self.jp.ref_fancy_normed)
            self.ui.graph_calc5_refl_final.setYRange(-0.1, 1.1)
            self.graph5_norm_one_line.setPos(self.ui.sb_calc5_norm_one.value())
            self.graph5_norm_zero_line.setPos(self.ui.sb_calc5_norm_zero.value())

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
            outfname = os.path.join(os.path.join(self.ddtree.ddir, "output", "bayer.npy"))
            np.save(outfname, self.jp.data)
        self.ui.pbar_export.setValue(25)
        if self.ui.cb_export_bayer_as_mat.isChecked():
            pass
        self.ui.pbar_export.setValue(50)
        if self.ui.cb_export_ref_CSV_simple.isChecked():
            tmpcsv = np.zeros((1000, 3), dtype=np.float64)
            tmpcsv[:, 0] = self.jp.gray.rchan_759nm_calibrated.index[-1000:]
            tmpcsv[:, 1] = self.jp.ref_fancy
            tmpcsv[:, 2] = self.jp.ref_fancy_normed if self.ui.cb_calc5_norm.isChecked() else 0
            outfname = os.path.join(os.path.join(self.ddtree.ddir, "output", "refl_output.csv"))
            print(outfname)
            np.savetxt(outfname, 
                       tmpcsv, 
                       ("%3.1f", "%2.5f", "%2.5f"), 
                       header=f"wave, refl, refl_norm_{self.ui.sb_calc5_norm_zero.value()}_{self.ui.sb_calc5_norm_one.value()}", 
                       delimiter=",")
        self.ui.pbar_export.setValue(100)

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Exported")
        dlg.setText("Export Finished")
        dlg.exec()
