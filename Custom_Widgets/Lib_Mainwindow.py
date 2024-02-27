# ---------- Base libraries -------------------------------------------------------------------------------------------
import os
import tempfile
import logging
import subprocess
import platform
from datetime import datetime
from pathlib import Path
import pyqtgraph as pg

# ---------- Numerical Visual packages---------------------------------------------------------------------------------
import numpy as np
import cv2 as cv

# ---------- GUI libraries --------------------------------------------------------------------------------------------
from PySide6.QtWidgets import QMainWindow, QWidget, QFileSystemModel
from PySide6.QtGui import QKeySequence, QShortcut, QColor
from PySide6.QtCore import QModelIndex, QDir, Qt

# ---------- Custom libs ----------------------------------------------------------------------------------------------
from Custom_UIs.UI_Mainwindow import Ui_MainWindow
from Custom_Libs.Lib_DataDirTree import DataDirTree
# from Custom_Widgets.Lib_PlotConfigDialog import PlotConfigDialog
from bps_raw_jpeg_processer.src.bps_raw_jpeg_processer import JpegProcessor

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
        self.setNameFilters((["*.jpeg", "*.jpg", "*.json"]))
        # , "*.tiff", "*.npy", "*.mat", "*.png"]))
        # self.setNameFilterDisables(False)
        # self.setNameFilterDisables(True)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.ForegroundRole:
            text = index.data(Qt.ItemDataRole.DisplayRole)
            if (".jpeg" in text) and (text.count("_") == 3):
                return QColor("#58cd1c")

            elif text.count("_") == 1 and (len(text) == 15) and text.replace("_", "").isnumeric():
                return QColor("#288d4c")
        return super(FileSystemModel, self).data(index, role)

class TheMainWindow(QMainWindow):
    dir_path: str = QDir.homePath()
    jpeg_path: str
    help_html_path: str = os.path.join(QDir.currentPath(), "docs/help.html") # need change on the binary release
    ddtree: DataDirTree = DataDirTree()
    jp: JpegProcessor = JpegProcessor()

    def __init__(self, parent: QWidget | None = None) -> None:
        super(TheMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pb_refresh.clicked.connect(self.call_update_geometry_vals)
        self.ui.pb_export.clicked.connect(self.call_export_data)

        # --------------- initialize the file system ----------------------------------
        self.fsmodel = FileSystemModel()                     # prev. QFileSystemModel()
        self.fsmodel.setRootPath(QDir.homePath())

        self.ui.tv_dir.setModel(self.fsmodel)
        self.ui.tv_dir.setRootIndex(self.fsmodel.setRootPath(QDir.homePath()))
        self.ui.tv_dir.doubleClicked.connect(self.call_tv_onItemClicked)
        # self.ui.cb_ft_filter.stateChanged.connect(self.fsmodel.setNameFilterDisables)
        self.ui.cb_ft_filter.stateChanged.connect(self.toggle_filetype_visiblity)
        self.ui.cb_bayer_show_geometry.stateChanged.connect(self.update_visual_1_rawbayer_img_section)
        self.ui.pb_waveperpixel_reset.clicked.connect(lambda: self.ui.sb_waveperpixel.setValue(1.8385))

        # -----------------------------------------------------------------------------
        self.jp.set_xWaveRng(self.ui.sb_midx_init.value())
        self.jp.set_yGrayRng((self.ui.sb_gray_y_init.value(), self.ui.sb_gray_y_init.value() + self.ui.sb_gray_y_size.value())) # noqa
        self.jp.set_yObjeRng((self.ui.sb_obje_y_init.value(), self.ui.sb_obje_y_init.value() + self.ui.sb_obje_y_size.value())) # noqa

        self.init_2d_graph_hide_the_original_roi_buttons()
        self.init_all_6_roi()
        self.init_sb_signals()

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


    def init_sb_signals(self) -> None:
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

    def all_sb_signal_block(self, b: bool) -> None:
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
        self.all_sb_signal_block(True)
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

        self.all_sb_signal_block(False)
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

        tmp_x = self.jp.get_wavelength_array(
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


        tmp_lef_x = self.jp.get_wavelength_array(
            init_pxl=self.ui.sb_lefx_init_rel.value()//2,
            pxl_size=self.ui.sb_lefx_size.value()//2,
            waveperpixel=self.ui.sb_waveperpixel.value(),
        )
        tmp_rig_x = self.jp.get_wavelength_array(
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
        

    def toggle_filetype_visiblity(self, a: int) -> None:
        if a:
            self.fsmodel.setNameFilters((["*.jpeg", "*.jpg", "*.json"]))
        else:
            self.fsmodel.setNameFilters((["*"]))

    def init_keyboard_bindings(self) -> None:
        QShortcut(QKeySequence("Ctrl+B"),    self).activated.connect(self.short_cut_goto_parent_dir)
        QShortcut(QKeySequence("Backspace"), self).activated.connect(self.short_cut_goto_parent_dir)
        QShortcut(QKeySequence("Return"),    self).activated.connect(self.short_cut_goto_selected_child_dir)
        QShortcut(QKeySequence("Space"),     self).activated.connect(self.short_cut_preview_raw_jpeg)
        QShortcut(QKeySequence("Ctrl+E"),    self).activated.connect(self.short_cut_export_raw_jpeg)
        QShortcut(QKeySequence("Ctrl+O"),    self).activated.connect(self.short_cut_open_at_point)
        QShortcut(QKeySequence("Ctrl+H"),    self).activated.connect(self.open_help_page)
        QShortcut(QKeySequence("Ctrl+F"),    self).activated.connect(self.ui.cb_ft_filter.toggle)
        QShortcut(QKeySequence("Ctrl+R"),    self).activated.connect(self.call_update_geometry_vals)

        # QShortcut(QKeySequence("Ctrl+Shift+E"), self).activated.connect(self.ex_type_dialog.exec)
        # QShortcut(QKeySequence("Ctrl+P"), self).activated.connect(self.ref_pcon_dialog.exec)
        # QShortcut(QKeySequence("Ctrl+Shift+P"), self).activated.connect(self.raw_pcon_dialog.exec)

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
            return False
        if not ((".jpeg" in basename) and (basename.count("_") == 3)):
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
        self.refresh_plots()
        return True

    def short_cut_export_raw_jpeg(self) -> None:
        """C-e: export"""
        logging.info("exporting")
        if self.short_cut_preview_raw_jpeg():    # checking the selected jpeg
            self.call_export_data()

    # @QtCore.pyqtSlot(QTreeWidgetItem, int)
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
            self.ui.limg_webcam.show_np_img(cv.imread(self.ddtree.webcamFP).astype(np.uint8))
            self.refresh_plots()

    def call_update_geometry_vals(self) -> None:
        # self.jp.set_xWaveRng(self.ui.sb_midx_init.value())
        # self.jp.set_yGrayRng((self.ui.sb_gray_y_init.value(), self.ui.sb_gray_y_init.value() + self.ui.sb_gray_y_size.value()))
        # self.jp.set_yObjeRng((self.ui.sb_obje_y_init.value(), self.ui.sb_obje_y_init.value() + self.ui.sb_obje_y_size.value()))

        # self.roi_obje_main.setPos(pos=(int(self.ui.sb_horx_left_pxl.text()), int(self.ui.sb_obje_top_pxl.text())))
        # self.roi_gray_main.setPos(pos=(int(self.ui.sb_horx_left_pxl.text()), int(self.ui.sb_gray_top_pxl.text())))

        # self.roi_obje_main.setSize(size=(800, int(self.ui.sb_obje_top_pxl.text())-int(self.ui.sb_obje_size_pxl.text())))
        # self.roi_gray_main.setSize(size=(800, int(self.ui.sb_gray_top_pxl.text())-int(self.ui.sb_gray_size_pxl.text())))
        self.refresh_plots()

    def update_jp_numerical_vals(self) -> None:
        self.jp.load_file(self.jpeg_path)
        self.jp.get_bayer()

        self.jp.get_spectrum()
        self.jp.fixme()
        self.jp.fancy_reflectance()

    def update_visual_1_rawbayer_img_section(self) -> None:
        self.ui.graph_2dimg.clear()
        self.ui.graph_2dimg.setImage(
            img=self.jp.rgb,
            levels=(0, 1024),
            axes={"x":1, "y":0, "c":2}
        )

    def update_visual_2_raw_spectrum_section(self) -> None:
        """remobed"""
        pass

    def update_visual_3_ref_spectrum_section(self) -> None:
        self.ui.graph_ref.clear()
        self.ui.graph_ref.plot(
            self.jp.obje.rchan_final.index[-1000:], 
            self.jp.ref_fancy,
        )

    def refresh_plots(self) -> None:
        self.update_jp_numerical_vals()
        self.update_visual_1_rawbayer_img_section()
        self.update_visual_2_raw_spectrum_section()
        self.update_visual_3_ref_spectrum_section()

    def call_export_data(self) -> None:
        """Export"""
        os.makedirs(os.path.join(self.ddtree.ddir, "output"), exist_ok=True)
        if self.ui.cb_export_bayer_as_npy.isChecked():
            pass
        if self.ui.cb_export_bayer_as_tif.isChecked():
            pass
        if self.ui.cb_export_bayer_as_mat.isChecked():
            pass
        if self.ui.cb_export_ref_plot_as_png.isChecked():
            pass
        if self.ui.cb_export_raw_plot_as_png.isChecked():
            pass
