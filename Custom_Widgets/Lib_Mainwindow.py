# Base libraries
import os
import tempfile
import logging
import subprocess
import platform
from datetime import datetime
from pathlib import Path
import pyqtgraph as pg

# Numerical/Visual packages
import numpy as np
import cv2 as cv

# GUI packages
from PySide6.QtWidgets import QDialogButtonBox, QMainWindow, QWidget, QFileSystemModel
from PySide6.QtGui import QKeySequence, QShortcut, QColor
from PySide6.QtCore import QModelIndex, QDir, Qt # QRect, 

# Custom packages
from Custom_UIs.UI_Mainwindow import Ui_MainWindow
from Custom_Libs.Lib_DataDirTree import DataDirTree
from Custom_Widgets.Lib_PlotConfigDialog import PlotConfigDialog
from bps_raw_jpeg_processer.src.bps_raw_jpeg_processer import JpegProcessor

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
                ("xdg-open", os.path.abspath(filepath)),  # hshell=True,
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

#class ConstantXROI(pg.ROI):
#    constant_left_x = 0
#
#    def setPos(self, pos, y=None, update=True, finish=True):
#        pos.setX(self.constant_left_x)
#        super().setPos(pos, y=y, update=update, finish=finish)

class TheMainWindow(QMainWindow):
    dir_path: str = QDir.homePath()
    jpeg_path: str
    ddtree: DataDirTree = DataDirTree()
    jp: JpegProcessor = JpegProcessor()
    # ex_type_dialog  : ExportTypeDialog # cant initialize Q widget an instance here.
    raw_pcon_dialog: PlotConfigDialog  # cant initialize Q widget an instance here.
    ref_pcon_dialog: PlotConfigDialog  # cant initialize Q widget an instance here.

    def __init__(self, parent: QWidget | None = None) -> None:
        super(TheMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.jp.set_xWaveRng(int(self.ui.sb_horx_left_pxl.text()))
        self.jp.set_yGrayRng((int(self.ui.sb_gray_top_pxl.text()), int(self.ui.sb_gray_bot_pxl.text())))
        self.jp.set_yObjeRng((int(self.ui.sb_obje_top_pxl.text()), int(self.ui.sb_obje_bot_pxl.text())))

        self.raw_pcon_dialog = PlotConfigDialog()
        self.ref_pcon_dialog = PlotConfigDialog()
        self.set_def_val_raw_ref_dialog()
        self.ui.tbtn_raw_spectrum_config.clicked.connect(self.raw_pcon_dialog.exec)
        self.ui.tbtn_ref_spectrum_config.clicked.connect(self.ref_pcon_dialog.exec)
        self.raw_pcon_dialog.ui.btn_box.accepted.connect(self.call_update_geometry_vals)
        self.ref_pcon_dialog.ui.btn_box.accepted.connect(self.call_update_geometry_vals)
        self.raw_pcon_dialog.ui.btn_box.button(QDialogButtonBox.StandardButton.Reset).clicked.connect(
            self.set_def_val_raw_ref_dialog
        )
        self.ref_pcon_dialog.ui.btn_box.button(QDialogButtonBox.StandardButton.Reset).clicked.connect(
            self.set_def_val_raw_ref_dialog
        )

        self.ui.pb_refresh.clicked.connect(self.call_update_geometry_vals)
        self.ui.pb_export.clicked.connect(self.call_export_data)

        # -----------------------------------------------------------------------------
        self.fsmodel = FileSystemModel()  # self.fsmodel = QFileSystemModel()
        self.fsmodel.setRootPath(QDir.homePath())

        self.ui.tv_dir.setModel(self.fsmodel)
        self.ui.tv_dir.setRootIndex(self.fsmodel.setRootPath(QDir.homePath()))
        self.ui.tv_dir.doubleClicked.connect(self.call_tv_onItemClicked)

        # self.ui.cb_ft_filter.stateChanged.connect(self.fsmodel.setNameFilterDisables)
        self.ui.cb_ft_filter.stateChanged.connect(self.toggle_filetype_visiblity)
        self.ui.cb_bayer_show_geometry.stateChanged.connect(self.update_visual_1_rawbayer_img_section)
        # -----------------------------------------------------------------------------
        self.roi_g = pg.ROI(
            pos=[self.ui.sb_horx_left_pxl.value(), self.ui.sb_gray_top_pxl.value()], 
            size=pg.Point(800, self.ui.sb_gray_top_pxl.value() - self.ui.sb_gray_bot_pxl.value()), 
            movable=True,
            scaleSnap=True,
            snapSize=2,
            translateSnap=True,
        )
        self.roi_o = pg.ROI(
            pos=[self.ui.sb_horx_left_pxl.value(), self.ui.sb_obje_top_pxl.value()], 
            size=pg.Point(800, self.ui.sb_obje_top_pxl.value() - self.ui.sb_obje_bot_pxl.value()), 
            movable=True,
            scaleSnap=True,
            snapSize=2,
            translateSnap=True,
        )
        #self.roi_g = pg.ROI([1480, 1250], pg.Point(800, 100), maxBounds=QRect(1480, 0, 800, 3000))
        #self.roi_o = pg.ROI([1480, 1350], pg.Point(800, 100), maxBounds=QRect(1480, 0, 800, 3000))
        #self.roi_g = ConstantXROI([1480, 1250], pg.Point(800, 100), maxBounds=QRect(1480, 0, 800, 3000))
        #self.roi_o = ConstantXROI([1480, 1350], pg.Point(800, 100), maxBounds=QRect(1480, 0, 800, 3000))
        
        self.roi_g.constant_left_x = 1480
        self.roi_o.constant_left_x = 1480

        #self.roi_o.addScaleHandle([0.5, 1], [0.5, 0.5])
        #self.roi_g.addScaleHandle([0.5, 1], [0.5, 0.5])

        self.roi_o.setZValue(10)
        self.roi_g.setZValue(10)

        self.ui.graph_2dimg.addItem(self.roi_o)
        self.ui.graph_2dimg.addItem(self.roi_g)

        # self.roi_g.sigRegionChanged.connect(self.updatePlot_g_roi)
        # self.roi_o.sigRegionChanged.connect(self.updatePlot_o_roi)



        self.init_keyboard_bindings()
        self.init_actions()

    def set_def_val_raw_ref_dialog(self):
        self.raw_pcon_dialog.ui.le_title.setText("Raw Digital Value")
        self.raw_pcon_dialog.ui.le_x_label.setText("Wavelength (nm)")
        self.raw_pcon_dialog.ui.le_y_label.setText("Digital Value (background removed)")
        self.raw_pcon_dialog.ui.sb_x_range_min.setValue(400)
        self.raw_pcon_dialog.ui.sb_x_range_max.setValue(900)
        self.raw_pcon_dialog.ui.sb_y_range_min.setValue(0)
        self.raw_pcon_dialog.ui.sb_y_range_max.setValue(1024)
        self.raw_pcon_dialog.ui.sb_fig_size_x.setValue(6.4)
        self.raw_pcon_dialog.ui.sb_fig_size_y.setValue(4.8)
        self.raw_pcon_dialog.ui.sb_fig_dpi.setValue(100)

        self.ref_pcon_dialog.ui.le_title.setText("Reflectance")
        self.ref_pcon_dialog.ui.le_x_label.setText("Wavelength (nm)")
        self.ref_pcon_dialog.ui.le_y_label.setText("Reflectance")
        self.ref_pcon_dialog.ui.sb_x_range_min.setValue(400)
        self.ref_pcon_dialog.ui.sb_x_range_max.setValue(900)
        self.ref_pcon_dialog.ui.sb_y_range_min.setValue(0)
        self.ref_pcon_dialog.ui.sb_y_range_max.setValue(2)
        self.ref_pcon_dialog.ui.sb_fig_size_x.setValue(6.4)
        self.ref_pcon_dialog.ui.sb_fig_size_y.setValue(4.8)
        self.ref_pcon_dialog.ui.sb_fig_dpi.setValue(100)

    def toggle_filetype_visiblity(self, a: int) -> None:
        if a:
            self.fsmodel.setNameFilters((["*.jpeg", "*.jpg", "*.json"]))
        else:
            self.fsmodel.setNameFilters((["*"]))

    def init_keyboard_bindings(self) -> None:
        QShortcut(QKeySequence("Ctrl+B"), self).activated.connect(self.short_cut_goto_parent_dir)
        QShortcut(QKeySequence("Backspace"), self).activated.connect(self.short_cut_goto_parent_dir)
        QShortcut(QKeySequence("Return"), self).activated.connect(self.short_cut_goto_selected_child_dir)
        QShortcut(QKeySequence("Space"), self).activated.connect(self.short_cut_preview_raw_jpeg)
        QShortcut(QKeySequence("Ctrl+E"), self).activated.connect(self.short_cut_export_raw_jpeg)
        QShortcut(QKeySequence("Ctrl+O"), self).activated.connect(self.short_cut_open_at_point)
        # QShortcut(QKeySequence("Ctrl+Shift+E"), self).activated.connect(self.ex_type_dialog.exec)
        QShortcut(QKeySequence("Ctrl+H"), self).activated.connect(self.open_help_page)
        QShortcut(QKeySequence("Ctrl+F"), self).activated.connect(self.ui.cb_ft_filter.toggle)
        QShortcut(QKeySequence("Ctrl+R"), self).activated.connect(self.call_update_geometry_vals)

        QShortcut(QKeySequence("Ctrl+P"), self).activated.connect(self.ref_pcon_dialog.exec)
        QShortcut(QKeySequence("Ctrl+Shift+P"), self).activated.connect(self.raw_pcon_dialog.exec)

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

    def open_help_page(self):
        open_file_externally("./docs/help.html")  # TODO need to change

    def short_cut_goto_parent_dir(self):
        logging.info("going to parent file")
        cur_root_index = self.ui.tv_dir.rootIndex()  # get .
        parent_of_cur_root_index = self.fsmodel.parent(cur_root_index)  # get ..
        self.ui.tv_dir.setRootIndex(parent_of_cur_root_index)  # set ..
        self.ui.tv_dir.setCurrentIndex(parent_of_cur_root_index)  # idk why this needed

    def short_cut_goto_selected_child_dir(self) -> None:
        sel_m_index = self.ui.tv_dir.currentIndex()  # get
        if self.fsmodel.hasChildren(sel_m_index):  # enter only if this has children
            self.ui.tv_dir.setRootIndex(sel_m_index)
        else:
            pass  # need to update jpeg_path here

    def short_cut_open_at_point(self):
        sel_m_index = self.ui.tv_dir.currentIndex()
        tmppath = self.fsmodel.filePath(sel_m_index)
        open_file_externally(tmppath)

    def short_cut_preview_raw_jpeg(self) -> bool:
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

    def short_cut_export_raw_jpeg(self):
        logging.info("exporting")
        if self.short_cut_preview_raw_jpeg():    # this itself it the exporting 
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
        self.jp.set_xWaveRng(int(self.ui.sb_horx_left_pxl.text()))
        self.jp.set_yGrayRng((int(self.ui.sb_gray_top_pxl.text()), int(self.ui.sb_gray_bot_pxl.text())))
        self.jp.set_yObjeRng((int(self.ui.sb_obje_top_pxl.text()), int(self.ui.sb_obje_bot_pxl.text())))

        self.roi_o.setPos(pos=(int(self.ui.sb_horx_left_pxl.text()), int(self.ui.sb_obje_top_pxl.text())))
        self.roi_g.setPos(pos=(int(self.ui.sb_horx_left_pxl.text()), int(self.ui.sb_gray_top_pxl.text())))

        self.roi_o.setSize(size=(800, int(self.ui.sb_obje_top_pxl.text())-int(self.ui.sb_obje_bot_pxl.text())))
        self.roi_g.setSize(size=(800, int(self.ui.sb_gray_top_pxl.text())-int(self.ui.sb_gray_bot_pxl.text())))
        self.refresh_plots()

    def update_jp_numerical_vals(self) -> None:
        self.jp.load_file(self.jpeg_path)
        self.jp.get_bayer()
        #self.jp.get_spectrums_channels_rgb()
        #self.jp.calc_shift_pixel_length()
        #self.jp.shiftall()
        #self.jp.calc_reflectance()
        #self.jp.fancy_reflectance()
        self.jp.get_spectrum()
        self.jp.fixme()
        self.jp.fancy_reflectance()

    # def updatePlot_g_roi(self) -> None:
    #     selected_o = self.roi_o.getState()

    #     self.roi_o.setPos(
    #         pos=pg.Point(self.ui.sb_horx_left_pxl.value(), selected_o["pos"].y())   
    #     )
    #     self.roi_o.setSize(
    #         size=pg.Point(800, selected_o["size"].y())   
    #     )
    #     self.update_geometry_parameters_after_roi_update()

    # def updatePlot_o_roi(self) -> None:
    #     selected_g = self.roi_g.getState()

    #     self.roi_g.setPos(
    #         pos=pg.Point(self.ui.sb_horx_left_pxl.value(), selected_g["pos"].y())   
    #     )
    #     self.roi_g.setSize(
    #         size=pg.Point(800, selected_g["size"].y())   
    #     )
    #     self.update_geometry_parameters_after_roi_update()


    # def update_geometry_parameters_after_roi_update(self) -> None:
    #     selected_o = self.roi_o.getState()
    #     selected_g = self.roi_g.getState()

    #     #self.ui.sb_horx_left_pxl.setValue(int(selected_o["pos"].x()))
    #     self.ui.sb_obje_top_pxl.setValue(int(selected_o["pos"].y()))
    #     self.ui.sb_obje_bot_pxl.setValue(int(selected_o["pos"].y() + selected_o["size"].y() ))
    #     self.ui.sb_gray_top_pxl.setValue(int(selected_g["pos"].y()))
    #     self.ui.sb_gray_bot_pxl.setValue(int(selected_g["pos"].y() + selected_g["size"].y() ))
    #     pass


    #     self.jp.set_xWaveRng(int(self.ui.sb_horx_left_pxl.text()))
    #     self.jp.set_yGrayRng((int(self.ui.sb_gray_top_pxl.text()), int(self.ui.sb_gray_bot_pxl.text())))
    #     self.jp.set_yObjeRng((int(self.ui.sb_obje_top_pxl.text()), int(self.ui.sb_obje_bot_pxl.text())))
    #     self.jp.get_bayer()
    #     self.jp.get_spectrum()
    #     self.jp.fixme()
    #     self.jp.fancy_reflectance()

    #     self.update_visual_2_raw_spectrum_section()

    def update_visual_1_rawbayer_img_section(self) -> None:
        self.ui.graph_2dimg.clear()
        self.ui.graph_2dimg.setImage(
            img=self.jp.rgb,
            levels=(0, 1024),
            axes={"x":1, "y":0, "c":2}
        )
        self.ui.graph_2dimg.ui.roiBtn.hide()
        self.ui.graph_2dimg.ui.menuBtn.hide()

    def update_visual_2_raw_spectrum_section(self) -> None:
        self.ui.graph_raw.clear()
        inf1 = pg.InfiniteLine(
            pos=759.3,
            movable=False, angle=90, 
            label="x={value:0.2f}nm", 
            labelOpts={"position":200, "color": (200,200,100), "fill": (200,200,200,50), "movable": True}
        )
        self.ui.graph_raw.addItem(inf1)
        self.ui.graph_raw.addLegend()

        self.ui.graph_raw.plot(self.jp.obje.rchan.index[:350], self.jp.obje.rchan["dn"].values[:350], pen=pg.mkPen("r", width=1, style=Qt.PenStyle.SolidLine), name="R-object")
        self.ui.graph_raw.plot(self.jp.obje.gchan.index[:700], self.jp.obje.gchan["dn"].values[:700], pen=pg.mkPen("g", width=1, style=Qt.PenStyle.SolidLine), name="G-object")
        self.ui.graph_raw.plot(self.jp.obje.bchan.index[:350], self.jp.obje.bchan["dn"].values[:350], pen=pg.mkPen("b", width=1, style=Qt.PenStyle.SolidLine), name="B-object")

        self.ui.graph_raw.plot(self.jp.gray.rchan.index[:350], self.jp.gray.rchan["dn"].values[:350], pen=pg.mkPen("r", width=1, style=Qt.PenStyle.DashLine),  name="R-gray")
        self.ui.graph_raw.plot(self.jp.gray.gchan.index[:700], self.jp.gray.gchan["dn"].values[:700], pen=pg.mkPen("g", width=1, style=Qt.PenStyle.DashLine),  name="G-gray")
        self.ui.graph_raw.plot(self.jp.gray.bchan.index[:350], self.jp.gray.bchan["dn"].values[:350], pen=pg.mkPen("b", width=1, style=Qt.PenStyle.DashLine),  name="B-gray")
        
        self.ui.graph_raw.setXRange(400,900)
        self.ui.graph_raw.setYRange(0,1024)

        

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
        """Exports"""
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
