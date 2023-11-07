import sys
from PySide6 import QtWidgets  # QtCore
from Custom_Widgets.Lib_Mainwindow import TheMainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = TheMainWindow()
    # w.setWindowFlags(
    #    QtCore.Qt.WindowType.WindowContextHelpButtonHint | QtCore.Qt.WindowType.WindowCloseButtonHint
    # )
    w.show()
    sys.exit(app.exec())
