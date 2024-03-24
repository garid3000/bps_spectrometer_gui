import sys
from PySide6 import QtWidgets
from Custom_Widgets.Lib_Mainwindow import TheMainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = TheMainWindow()
    w.show()
    sys.exit(app.exec())
