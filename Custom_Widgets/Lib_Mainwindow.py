# Base libraries
import os
import logging
import subprocess
import platform

# Numerical/Visual packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes   import Axes
import cv2 as cv
from numpy._typing import NDArray
from scipy.io import savemat

# GUI packages
from PySide6.QtWidgets import QDialogButtonBox, QMainWindow, QWidget, QFileSystemModel
from PySide6.QtGui     import QKeySequence, QShortcut, QColor
from PySide6.QtCore    import QModelIndex,  QDir, Qt

# Custom packages
from Custom_UIs.UI_Mainwindow            import Ui_MainWindow
from Custom_Libs.Lib_DataDirTree         import DataDirTree
from Custom_Widgets.Lib_PlotConfigDialog import PlotConfigDialog
from bps_raw_jpeg_processer.src.bps_raw_jpeg_processer import JpegProcessor


system_str = platform.system()

logging.basicConfig(
    filename=f"app.{1}.log",   # TODO
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
    # this need to change according to OS
    # encoding="utf-8",
    # datefmt='%Y-%m-%d %H:%M:%S'
)

def open_a_file(filepath: str) -> None:
    try:
        if system_str == "Windows":                  # Windows
            os.startfile(filepath)                   # type: ignore
        elif system_str == "Darwin":                 # BSDs and macos
            subprocess.Popen( ("open ",  filepath),  # shell=True,
                stdin=None, stdout=None, stderr=None, close_fds=True)
        elif system_str == "Linux":                  # linux variants
            subprocess.Popen(
                ("xdg-open", os.path.abspath(filepath)), # hshell=True,
                stdin=None, stdout=None, stderr=None, close_fds=True)
        return None
    except Exception as e:
        print(e)
        return None



class FileSystemModel(QFileSystemModel): 
    # read from https://stackoverflow.com/a/40455027/14696853
    def __init__(self, *args, **kwargs):
        super(FileSystemModel, self).__init__(*args, **kwargs)
        self.setNameFilters( ( ["*.jpeg", "*.jpg", "*.json"] ) )
        #, "*.tiff", "*.npy", "*.mat", "*.png"]))
        #self.setNameFilterDisables(False)
        #self.setNameFilterDisables(True)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.ForegroundRole:
            text = index.data(Qt.ItemDataRole.DisplayRole)
            if (".jpeg" in text) and (text.count("_")==3):
                return QColor("#58cd1c")

            elif (text.count("_")==1 and 
                  (len(text) == 15) and 
                  text.replace("_", "").isnumeric()):
                return QColor("#288d4c")
        return super(FileSystemModel, self).data(index, role)


class TheMainWindow(QMainWindow):
    dir_path        : str              = QDir.homePath()
    ddtree          : DataDirTree       = DataDirTree()
    jp              : JpegProcessor     = JpegProcessor()
    jpeg_path       : str
    #ex_type_dialog  : ExportTypeDialog # cant initialize Q widget an instance here.
    raw_pcon_dialog : PlotConfigDialog # cant initialize Q widget an instance here.
    ref_pcon_dialog : PlotConfigDialog # cant initialize Q widget an instance here.

    raw_plot_as_npimg : NDArray[np.uint8] = np.zeros((10, 10, 3), dtype=np.uint8)
    ref_plot_as_npimg : NDArray[np.uint8] = np.zeros((10, 10, 3), dtype=np.uint8)


    def __init__(self, parent: QWidget | None = None) -> None:
        super(TheMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.raw_pcon_dialog = PlotConfigDialog()
        self.ref_pcon_dialog = PlotConfigDialog()
        self.set_def_val_raw_ref_dialog()
        self.ui.tbtn_raw_spectrum_config.clicked.connect(self.raw_pcon_dialog.exec)
        self.ui.tbtn_ref_spectrum_config.clicked.connect(self.ref_pcon_dialog.exec)
        self.raw_pcon_dialog.ui.btn_box.accepted.connect(self.call_update_geometry_vals)
        self.ref_pcon_dialog.ui.btn_box.accepted.connect(self.call_update_geometry_vals)
        self.raw_pcon_dialog.ui.btn_box.button(QDialogButtonBox.StandardButton.Reset).clicked.connect(self.set_def_val_raw_ref_dialog)
        self.ref_pcon_dialog.ui.btn_box.button(QDialogButtonBox.StandardButton.Reset).clicked.connect(self.set_def_val_raw_ref_dialog)

        self.ui.pb_refresh.clicked.connect(self.call_update_geometry_vals)
        self.ui.pb_export.clicked.connect(self.call_export_data)


        # -----------------------------------------------------------------------------
        self.fsmodel = FileSystemModel()            # self.fsmodel = QFileSystemModel()
        self.fsmodel.setRootPath(QDir.homePath())

        self.ui.tv_dir.setModel(self.fsmodel)
        self.ui.tv_dir.setRootIndex(self.fsmodel.setRootPath(QDir.homePath()))
        self.ui.tv_dir.doubleClicked.connect(self.call_open_folder_or_preview_jpeg)

        #self.ui.cb_ft_filter.stateChanged.connect(self.fsmodel.setNameFilterDisables)
        self.ui.cb_ft_filter.stateChanged.connect(self.toggle_filetype_visiblity)
        self.ui.cb_bayer_show_geometry.stateChanged.connect(self.update_visual_1_rawbayer_img_section)
        self.ui.cb_raw_show_bg.stateChanged.connect(self.update_visual_2_raw_spectrum_section)
        # -----------------------------------------------------------------------------
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
            self.fsmodel.setNameFilters( ( ["*.jpeg", "*.jpg", "*.json"] ) )
        else:
            self.fsmodel.setNameFilters( ( ["*"] ) )



    def init_keyboard_bindings(self) -> None:
        QShortcut(QKeySequence("Ctrl+B"),       self).activated.connect(self.short_cut_goto_parent_dir)
        QShortcut(QKeySequence("Backspace"),    self).activated.connect(self.short_cut_goto_parent_dir)
        QShortcut(QKeySequence("Return"),       self).activated.connect(self.short_cut_goto_selected_child_dir)
        QShortcut(QKeySequence("Space"),        self).activated.connect(self.short_cut_preview_raw_jpeg)
        QShortcut(QKeySequence("Ctrl+E"),       self).activated.connect(self.short_cut_export_raw_jpeg)
        QShortcut(QKeySequence("Ctrl+O"),       self).activated.connect(self.short_cut_open_at_point)
        #QShortcut(QKeySequence("Ctrl+Shift+E"), self).activated.connect(self.ex_type_dialog.exec)
        QShortcut(QKeySequence("Ctrl+H"),       self).activated.connect(self.open_help_page)
        QShortcut(QKeySequence("Ctrl+F"),       self).activated.connect(self.ui.cb_ft_filter.toggle)
        QShortcut(QKeySequence("Ctrl+R"),       self).activated.connect(self.call_update_geometry_vals)

        QShortcut(QKeySequence("Ctrl+P"),       self).activated.connect(self.ref_pcon_dialog.exec)
        QShortcut(QKeySequence("Ctrl+Shift+P"), self).activated.connect(self.raw_pcon_dialog.exec)


    def init_actions(self) -> None:
        self.ui.action_help.triggered.connect(self.open_help_page)
        #self.ui.action_dir_cur_child_fold.connect( #lambda self.ui.tv_dir.collapse())
        #self.ui.action_dir_cur_child_unfold.connect(self.ui.tv_dir.)

        self.ui.action_dir_goto_cur_child.triggered.connect(self.short_cut_goto_selected_child_dir)
        self.ui.action_dir_goto_parent.triggered.connect(self.short_cut_goto_parent_dir)
        self.ui.action_dir_ft_filter_toggle.triggered.connect(self.ui.cb_ft_filter.toggle)

        self.ui.action_cur_jpeg_export.triggered.connect(self.short_cut_export_raw_jpeg)
        self.ui.action_cur_jpeg_preview.triggered.connect(self.short_cut_preview_raw_jpeg)
        self.ui.action_cur_file_open.triggered.connect(self.short_cut_open_at_point)


    def open_help_page(self):
        open_a_file("/home/garid/Projects/psm/bps_spectrometer_gui/docs/help.html")

    def short_cut_goto_parent_dir(self):
        print("goto parent")
        cur_root_index           = self.ui.tv_dir.rootIndex()          # get .
        parent_of_cur_root_index = self.fsmodel.parent(cur_root_index) # get ..
        self.ui.tv_dir.setRootIndex(parent_of_cur_root_index)          # set ..
        self.ui.tv_dir.setCurrentIndex(parent_of_cur_root_index)   # idk why this needed
    

    def short_cut_goto_selected_child_dir(self) -> None:
        sel_m_index = self.ui.tv_dir.currentIndex()    # get
        if self.fsmodel.hasChildren(sel_m_index):      # enter only if this has children
            self.ui.tv_dir.setRootIndex(sel_m_index)
        else:
            pass                                       # need to update jpeg_path here 

    def short_cut_open_at_point(self):
        sel_m_index = self.ui.tv_dir.currentIndex()
        tmppath = self.fsmodel.filePath(sel_m_index)
        open_a_file(tmppath)


    def short_cut_preview_raw_jpeg(self) -> bool:
        sel_m_index = self.ui.tv_dir.currentIndex()
        tmppath = self.fsmodel.filePath(sel_m_index)
        basename = os.path.basename(tmppath)
        print("space press", tmppath)
        if not os.path.isfile(tmppath):
            return False
        if not ((".jpeg" in basename) and 
                (basename.count("_")==3)):
            return False

        self.jpeg_path = tmppath
        self.dir_path  = os.path.dirname(self.jpeg_path)
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
        if self.short_cut_preview_raw_jpeg():
            self.call_export_data()
        
    def call_open_folder_or_preview_jpeg(self, v: QModelIndex):
        tmp  = self.fsmodel.filePath(v)
        if os.path.isdir(tmp):
            self.ui.tv_dir.setRootIndex(v)
        else:
            self.short_cut_preview_raw_jpeg()
    
    def call_update_geometry_vals(self) -> None:
        self.jp.set_xWaveRng(  int(self.ui.sb_horx_left_pxl.text()) )
        self.jp.set_yGrayRng( (int(self.ui.sb_gray_top_pxl.text()), int(self.ui.sb_gray_bot_pxl.text())))
        self.jp.set_yObjeRng( (int(self.ui.sb_obje_top_pxl.text()), int(self.ui.sb_obje_bot_pxl.text())))
        self.refresh_plots()

    def update_jp_numerical_vals(self) -> None:
        self.jp.load_file(self.jpeg_path)
        self.jp.get_bayer()
        self.jp.get_spectrums_channels_rgb()
        if self.ui.cb_fraunhofer_calib.isChecked():
            self.jp.calc_shift_pixel_length()
            self.jp.shiftall()
            print("shift")
        self.jp.calc_reflectance()
        self.jp.fancy_reflectance()

    def update_visual_1_rawbayer_img_section(self) -> None:
        tmp = (self.jp.rgb // 4).astype(np.uint8)
        
        tmp = cv.rectangle(
                tmp, 
                (self.jp.xWaveRng[0], self.jp.yGrayRng[0]),
                (self.jp.xWaveRng[1], self.jp.yGrayRng[1]),
                (255, 0, 0),
                thickness=8)

        tmp = cv.rectangle(
                tmp, 
                (self.jp.xLfBgRng[0], self.jp.yGrayRng[0]),
                (self.jp.xLfBgRng[1], self.jp.yGrayRng[1]),
                (255, 0, 0),
                thickness=8)

        tmp = cv.rectangle(
                tmp, 
                (self.jp.xRiBgRng[0], self.jp.yGrayRng[0]),
                (self.jp.xRiBgRng[1], self.jp.yGrayRng[1]),
                (255, 0, 0),
                thickness=8)



        if self.ui.cb_bayer_show_geometry.isChecked():
            tmp = cv.putText(tmp, str(self.ui.sb_horx_left_pxl.value()) + "px",
                             (self.jp.xWaveRng[0]//2, self.jp.yObjeRng[0]//2), 
                             0,  4, (0, 255, 0), 8, cv.LINE_AA)
            tmp = cv.arrowedLine(tmp,  
                    (0,                   self.jp.yObjeRng[0]//2), 
                    (self.jp.xWaveRng[0], self.jp.yObjeRng[0]//2), 
                    (0, 255, 0), 
                    thickness=8)

            tmp = cv.putText(tmp, str(self.ui.sb_gray_top_pxl.value()) + "px",
                             (self.jp.xWaveRng[0]//2, 3*self.jp.yGrayRng[0]//4), 
                             0,  4, (255, 0, 0), 8, cv.LINE_AA)

            tmp = cv.arrowedLine(tmp,  
                    (self.jp.xWaveRng[0]//2, 0                  ), 
                    (self.jp.xWaveRng[0]//2, self.jp.yGrayRng[0]), 
                    (255, 0, 0), 
                    thickness=8)

            tmp = cv.putText(tmp, str(self.ui.sb_obje_top_pxl.value()) + "px",
                             (self.jp.xWaveRng[0]//4, 3*self.jp.yObjeRng[0]//4), 
                             0,  4, (0, 0, 255), 8, cv.LINE_AA)

            tmp = cv.arrowedLine(tmp,  
                    (self.jp.xWaveRng[0]//4, 0                  ), 
                    (self.jp.xWaveRng[0]//4, self.jp.yObjeRng[0]), 
                    (0, 0, 255), 
                    thickness=8)




        tmp = cv.rectangle(
                tmp, 
                (self.jp.xWaveRng[0], self.jp.yObjeRng[0]),
                (self.jp.xWaveRng[1], self.jp.yObjeRng[1]),
                (0, 0, 255),
                thickness=8)

        tmp = cv.rectangle(
                tmp, 
                (self.jp.xLfBgRng[0], self.jp.yObjeRng[0]),
                (self.jp.xLfBgRng[1], self.jp.yObjeRng[1]),
                (0, 0, 255),
                thickness=8)

        tmp = cv.rectangle(
                tmp, 
                (self.jp.xRiBgRng[0], self.jp.yObjeRng[0]),
                (self.jp.xRiBgRng[1], self.jp.yObjeRng[1]),
                (0, 0, 255),
                thickness=8)



        self.ui.limg_bayer_full.show_np_img(
            arr=tmp,
            outwidth = 480
        )

        self.ui.limg_bayer_gray.show_np_img(
            arr=( 
                 self.jp.rgb[ 
                              self.jp.yGrayRng[0]: self.jp.yGrayRng[1],
                              self.jp.xWaveRng[0]: self.jp.xWaveRng[1], 
                              : 
                              ] // 4
                 ).astype(np.uint8),
            outwidth = 480
        )
        

        self.ui.limg_bayer_obje.show_np_img(
            arr=( 
                 self.jp.rgb[ 
                              self.jp.yObjeRng[0]: self.jp.yObjeRng[1],
                              self.jp.xWaveRng[0]: self.jp.xWaveRng[1], 
                              : 
                              ]// 4
                 ).astype(np.uint8),
            outwidth = 480
        )
    def update_visual_2_raw_spectrum_section(self) -> None:
        fig: Figure
        ax: Axes
        fig, ax = plt.subplots()

        ax.plot(self.jp.xwave, self.jp.gray4_mean["chan0_r"], "r--", label="red")    
        ax.plot(self.jp.xwave, self.jp.gray4_mean["chan2_G"], "k--", label="green2")
        ax.plot(self.jp.xwave, self.jp.gray4_mean["chan1_g"], "g--", label="green")
        ax.plot(self.jp.xwave, self.jp.gray4_mean["chan3_b"], "b--", label="blue")

        ax.plot(self.jp.xwave, self.jp.obje4_mean["chan0_r"], "r-", label="red")
        ax.plot(self.jp.xwave, self.jp.obje4_mean["chan2_G"], "k-", label="green2")
        ax.plot(self.jp.xwave, self.jp.obje4_mean["chan1_g"], "g-", label="green")
        ax.plot(self.jp.xwave, self.jp.obje4_mean["chan3_b"], "b-", label="blue")
        print(self.jp.xwave)

        if self.ui.cb_raw_show_bg.isChecked():
            ax.plot(self.jp.xwave, self.jp.bg_gray4["chan0_r"], "r--") #, label="red")
            ax.plot(self.jp.xwave, self.jp.bg_gray4["chan2_G"], "k--") #, label="green2")
            ax.plot(self.jp.xwave, self.jp.bg_gray4["chan1_g"], "g--") #, label="green")
            ax.plot(self.jp.xwave, self.jp.bg_gray4["chan3_b"], "b--") #, label="blue")

            ax.plot(self.jp.xwave, self.jp.bg_obje4["chan0_r"], "r-") #, label="red")
            ax.plot(self.jp.xwave, self.jp.bg_obje4["chan2_G"], "k-") #, label="green2")
            ax.plot(self.jp.xwave, self.jp.bg_obje4["chan1_g"], "g-") #, label="green")
            ax.plot(self.jp.xwave, self.jp.bg_obje4["chan3_b"], "b-") #, label="blue")


        ax.vlines(759, 0, 1024) # the 759nm
        if self.raw_pcon_dialog.ui.cb_legend.isChecked():
            ax.legend()
        if self.raw_pcon_dialog.ui.cb_grid.isChecked():
            ax.grid()
        ax.set_xlim(
            left=self.raw_pcon_dialog.ui.sb_x_range_min.value(),
            right=self.raw_pcon_dialog.ui.sb_x_range_max.value(),
        )
        ax.set_ylim(
            bottom=self.raw_pcon_dialog.ui.sb_y_range_min.value(),
            top=self.raw_pcon_dialog.ui.sb_y_range_max.value(),
        )
        ax.set_title(self.raw_pcon_dialog.ui.le_title.text())
        ax.set_xlabel(self.raw_pcon_dialog.ui.le_x_label.text())
        ax.set_ylabel(self.raw_pcon_dialog.ui.le_y_label.text())

        fig.set_size_inches(
            w=self.raw_pcon_dialog.ui.sb_fig_size_x.value(),
            h=self.raw_pcon_dialog.ui.sb_fig_size_y.value(),
        )
        fig.set_dpi(self.raw_pcon_dialog.ui.sb_fig_dpi.value())

        fig.canvas.draw()
        self.raw_plot_as_npimg = np.fromstring(
                fig.canvas.tostring_rgb(), dtype=np.uint8).reshape(fig.canvas.get_width_height()[::-1] + (3,)) # type: ignore
        self.ui.limg_raw_spectrum.show_np_img(arr = self.raw_plot_as_npimg, outwidth= 480)

    def update_visual_3_ref_spectrum_section(self) -> None:
        fig, ax = plt.subplots()
        ax.plot(self.jp.xwave, self.jp.ref_fancy, color="black",   label="reflectance")

        ax.vlines(759, 0, 1024) # the 759nm
        if self.ref_pcon_dialog.ui.cb_legend.isChecked():
            ax.legend()
        if self.ref_pcon_dialog.ui.cb_grid.isChecked():
            ax.grid()
        ax.set_xlim(
            left=self.ref_pcon_dialog.ui.sb_x_range_min.value(),
            right=self.ref_pcon_dialog.ui.sb_x_range_max.value(),
        )
        ax.set_ylim(
            bottom=self.ref_pcon_dialog.ui.sb_y_range_min.value(),
            top=self.ref_pcon_dialog.ui.sb_y_range_max.value(),
        )
        ax.set_title(self.ref_pcon_dialog.ui.le_title.text())
        ax.set_xlabel(self.ref_pcon_dialog.ui.le_x_label.text())
        ax.set_ylabel(self.ref_pcon_dialog.ui.le_y_label.text())

        fig.set_size_inches(
            w=self.ref_pcon_dialog.ui.sb_fig_size_x.value(),
            h=self.ref_pcon_dialog.ui.sb_fig_size_y.value(),
        )
        fig.set_dpi(self.ref_pcon_dialog.ui.sb_fig_dpi.value())

        fig.canvas.draw()
        self.ref_plot_as_npimg = np.fromstring(
                fig.canvas.tostring_rgb(), dtype=np.uint8).reshape(fig.canvas.get_width_height()[::-1] + (3,)) # type: ignore
        self.ui.limg_ref_spectrum.show_np_img(arr = self.ref_plot_as_npimg, outwidth= 480)

    def refresh_plots(self) -> None:
        self.ui.pb_redraw_progress.setValue(0)
        self.update_jp_numerical_vals()
        self.ui.pb_redraw_progress.setValue(25)
        self.update_visual_1_rawbayer_img_section()
        self.ui.pb_redraw_progress.setValue(50)
        self.update_visual_2_raw_spectrum_section()
        self.ui.pb_redraw_progress.setValue(75)
        self.update_visual_3_ref_spectrum_section()
        self.ui.pb_redraw_progress.setValue(100)

    def call_export_data(self) -> None:
        """Exports"""
        self.export_output_dir = os.path.join(self.ddtree.ddir, "output")
        self.export_output_file_template = os.path.join(
                self.ddtree.ddir, "output", os.path.basename(self.jpeg_path).replace(".jpeg", ""))

        os.makedirs(self.export_output_dir, exist_ok=True)

        if self.ui.cb_rawbayer_export_npy.isChecked():
            np.save(self.export_output_file_template + ".npy", self.jp.data)

        if self.ui.cb_rawbayer_export_tif.isChecked():
            cv.imwrite(self.export_output_file_template + ".tif", self.jp.data)

        if self.ui.cb_rawbayer_export_mat.isChecked():
            savemat(
                self.export_output_file_template + ".mat", 
                {"rawbayer": self.jp.data}
            )

        if self.ui.cb_rawspect_export_plot.isChecked():
            cv.imwrite(self.export_output_file_template + "_raw.png", self.raw_plot_as_npimg)

        if self.ui.cb_refspect_export_plot.isChecked():
            cv.imwrite(self.export_output_file_template + "_ref.png", self.ref_plot_as_npimg)
