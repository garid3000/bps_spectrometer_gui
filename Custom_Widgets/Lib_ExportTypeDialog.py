import sys
#from typing import List
#import numpy as np
#import numpy.typing as npt
#import cv2 as cv  # import cmap
from PySide6.QtWidgets import QDialog, QApplication
#, QtGui, QtCore

try:
    from Custom_UIs.UI_ExportConfDialog import Ui_Dialog
except Exception:
    sys.path.append("..")
    from Custom_UIs.UI_ExportConfDialog import Ui_Dialog


class ExportTypeDialog(QDialog):
    def __init__(self, parent: QDialog | None = None) -> None:
        super(ExportTypeDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = ExportTypeDialog
    Dialog.show()
    sys.exit(app.exec())
