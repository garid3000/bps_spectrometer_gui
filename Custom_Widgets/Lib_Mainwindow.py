#from typing import List

# import sys
#import numpy as np
#import numpy.typing as npt
#import cv2 as cv  # import cmap

from PySide6 import QtWidgets # , QtCore
from Custom_UIs.UI_Mainwindow import Ui_MainWindow

#from Custom_Widgets.Lib_ImagePrepperWidget import ImagePrepperWidget
#from Custom_Widgets.Lib_IndexCalcShowerGroupBox import IndexCalcShowerGroupBox


class TheMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super(TheMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

