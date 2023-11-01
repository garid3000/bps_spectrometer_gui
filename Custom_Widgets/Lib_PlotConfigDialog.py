import sys
from PySide6.QtWidgets import QDialog, QApplication

try:
    from Custom_UIs.UI_PlotControlDialog import Ui_Dialog
except Exception:
    sys.path.append("..")
    from Custom_UIs.UI_PlotControlDialog import Ui_Dialog

class PlotConfigDialog(QDialog):
    def __init__(self, parent: QDialog | None = None) -> None:
        super(PlotConfigDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = PlotConfigDialog()
    Dialog.show()
    sys.exit(app.exec())
