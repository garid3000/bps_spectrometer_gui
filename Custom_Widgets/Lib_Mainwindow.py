#from typing import List

# import sys
import os
import logging
import numpy as np
#import numpy.typing as npt
import matplotlib.pyplot as plt
import cv2 as cv  # import cmap


from PySide6.QtWidgets import  (
    QMainWindow, QWidget, QFileDialog,    
)
# , QtCore
from Custom_UIs.UI_Mainwindow import Ui_MainWindow
from Custom_Libs.Lib_DataDirTree import DataDirTree
from Custom_Widgets.Lib_ExportTypeDialog import ExportTypeDialog
from bps_raw_jpeg_processer.src.bps_raw_jpeg_processer import JpegProcessor

logging.basicConfig(
    filename="/tmp/app.log",  # this need to change according to OS
    #encoding="utf-8",
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
    #datefmt='%Y-%m-%d %H:%M:%S'
)


dbg_ddir: str = os.path.join(    # this contains selected path string
            "/home", "garid", "data_dump_badmasflash_2023_0117",
            "Data_cp_20230117_092825", "20230117_092051")



class TheMainWindow(QMainWindow):
    dir_path       : str             = dbg_ddir
    ddtree         :DataDirTree      = DataDirTree()
    jp             :JpegProcessor    = JpegProcessor()
    ex_type_dialog :ExportTypeDialog # = ExportTypeDialog() # cannot initialize here due to lib.


    def __init__(self, parent: QWidget | None = None) -> None:
        super(TheMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ex_type_dialog   = ExportTypeDialog()

        self.dir_path = dbg_ddir
        self.ui.pb_data_dir.clicked.connect(self.call_btnDirSelect)
        self.ui.actionOpen_Directory.triggered.connect(self.call_btnDirSelect)
        self.ui.pb_refresh.clicked.connect(self.call_btnRefresh)
        self.ui.cob_jpeg_selector.textActivated.connect(self.refresh_plots)
        self.ui.pb_conf_export.clicked.connect(self.ex_type_dialog.exec)

        
    def call_btnDirSelect(self) -> None:
        """
        Opens file-dialog in order to select data directory.
        if:   self.dir_path exists in system, open that directory
        else: open at home directory
        """
        logging.debug(f"{self.__repr__()}: call_btnDirSelect, starting")
        if os.path.isdir(self.dir_path):
            tmpDir = QFileDialog.getExistingDirectory(
                    self, "Choose Directory", self.dir_path) 
            logging.debug(f"{self.__repr__()}: call_btnDirSelect, opening at old point")
        else:
            tmpDir = QFileDialog.getExistingDirectory(self, "Choose Directory", "")
            logging.debug(f"{self.__repr__()}: call_btnDirSelect, opening at new point")

        # checks user if cancelled
        self.dir_path = tmpDir if os.path.isdir(tmpDir) else self.dir_path
        self.ui.le_data_dir.setText(self.dir_path)
        logging.debug(f"{self.__repr__()}: call_btnDirSelect, end: {self.dir_path}")

        # =============================================================================
        self.ddtree.set_ddir(self.dir_path)
        self.ui.cob_jpeg_selector.clear()        # clear jpeg
        self.ui.cob_jpeg_selector.addItems(self.ddtree.jpegFnames)
        self.ui.tb_meta_json.setText(self.ddtree.metajsonText)
        self.ui.tb_data_dir_tree.setText(self.ddtree.directory_structure())
        # =============================================================================
        self.ui.limg_webcam.show_np_img(cv.imread(self.ddtree.webcamFP).astype(np.uint8))
        return
    
    def call_btnRefresh(self) -> None:
        self.jp.set_xWaveRng( int(self.ui.sb_horx_left_pxl.text()) )
        self.jp.set_yGrayRng(
            (int(self.ui.sb_gray_top_pxl.text()), int(self.ui.sb_gray_bot_pxl.text())))
        self.jp.set_yObjeRng(
            (int(self.ui.sb_obje_top_pxl.text()), int(self.ui.sb_obje_bot_pxl.text())))
        self.refresh_plots("hi")

    def refresh_plots(self, atgivenjpeg: str) -> None:
        print(atgivenjpeg)

        #= ===========================================================================
        self.jp.load_file(os.path.join(self.dir_path, atgivenjpeg))
        self.jp.get_bayer()
        self.jp.get_spectrums_channels_rgb()
        self.jp.calc_shift_pixel_length()
        self.jp.shiftall()
        self.jp.calc_reflectance()
        self.jp.fancy_reflectance()
        #= visuals ====================================================================
        self.ui.limg_bayer_full.show_np_img(
            arr=(self.jp.rgb // 4).astype(np.uint8),
            outwidth = 1000
        )

        self.ui.limg_bayer_gray.show_np_img(
            arr=( 
                 self.jp.rgb[ 
                              self.jp.yGrayRng[0]: self.jp.yGrayRng[1],
                              self.jp.xWaveRng[0]: self.jp.xWaveRng[1], 
                              : 
                              ] // 4
                 ).astype(np.uint8),
            outwidth = 800
        )
        

        self.ui.limg_bayer_obje.show_np_img(
            arr=( 
                 self.jp.rgb[ 
                              self.jp.yObjeRng[0]: self.jp.yObjeRng[1],
                              self.jp.xWaveRng[0]: self.jp.xWaveRng[1], 
                              : 
                              ]// 4
                 ).astype(np.uint8),
            outwidth = 800
        )
        #= visuals ====================================================================
        fig: plt.Figure
        ax: plt.Axes
        fig, ax = plt.subplots()
        #ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
        ax.plot(self.jp.xwave, self.jp.gray4_mean["chan0_r"], "--", color="red",   label="red")
        ax.plot(self.jp.xwave, self.jp.gray4_mean["chan1_g"], "--", color="green", label="green")
        ax.plot(self.jp.xwave, self.jp.gray4_mean["chan2_G"], "--", color="black", label="green2")
        ax.plot(self.jp.xwave, self.jp.gray4_mean["chan3_b"], "--", color="blue",  label="blue")

        ax.plot(self.jp.xwave, self.jp.obje4_mean["chan0_r"], color="red",   label="red")
        ax.plot(self.jp.xwave, self.jp.obje4_mean["chan1_g"], color="green", label="green")
        ax.plot(self.jp.xwave, self.jp.obje4_mean["chan2_G"], color="black", label="green2")
        ax.plot(self.jp.xwave, self.jp.obje4_mean["chan3_b"], color="blue",  label="blue")
        print(self.jp.xwave)

        #ax.vlines(192*2, 0, 1024, linestyles='dashdot')
        ax.vlines(759, 0, 1024, linestyles='dashdot')
        ax.legend()

        fig.canvas.draw()
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8)
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        #cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.ui.limg_raw_spectrum.show_np_img( arr = img, outwidth= 640)

        #= visuals ====================================================================
        fig, ax = plt.subplots()
        #ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
        ax.plot(self.jp.xwave, self.jp.ref_fancy, color="black",   label="reflectance")
        ax.legend()

        fig.canvas.draw()
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8)
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        #cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.ui.limg_refl_spectrum.show_np_img( arr = img, outwidth= 640)

