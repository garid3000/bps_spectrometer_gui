#from typing import List

# import sys
#import numpy as np
#import numpy.typing as npt
import os
import logging
import cv2 as cv  # import cmap


from PySide6.QtWidgets import  (
    QMainWindow, QWidget, QFileDialog,    
)
# , QtCore
from Custom_UIs.UI_Mainwindow import Ui_MainWindow
from Custom_Libs.Lib_DataDirTree import DataDirTree
from bps_raw_jpeg_processer.src.bps_raw_jpeg_processer import JpegProcessor

logging.basicConfig(
    filename="/tmp/app.log",  # this need to change according to OS
    #encoding="utf-8",
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    #datefmt='%Y-%m-%d %H:%M:%S'
)


#from Custom_Widgets.Lib_ImagePrepperWidget import ImagePrepperWidget
#from Custom_Widgets.Lib_IndexCalcShowerGroupBox import IndexCalcShowerGroupBox
dbg_ddir: str = os.path.join(    # this contains selected path string
            "/home", "garid", "data_dump_badmasflash_2023_0117",
            "Data_cp_20230117_092825", "20230117_092051")



class TheMainWindow(QMainWindow):
    dir_path : str        = dbg_ddir
    ddtree   :DataDirTree = DataDirTree()
    jp       :JpegProcessor = JpegProcessor()

    def __init__(self, parent: QWidget | None = None) -> None:
        super(TheMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dir_path = dbg_ddir
        self.ui.pb_data_dir.clicked.connect(self.call_btnDirSelect)

        
    def call_btnDirSelect(self) -> None:
        """
        Opens file-dialog in order to select data directory.
        if:   self.dir_path exists in system, open that directory
        else: open at home directory
        """
        logging.debug(f"{self.__repr__()}: call_btnDirSelect, starting")
        if os.path.isdir(self.dir_path):
            tmpDir = QFileDialog.getExistingDirectory(self, "Choose Directory", self.dir_path)
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
        self.ui.limg_webcam.show_np_img(cv.imread(self.ddtree.webcamFP))
        return
