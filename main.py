import sys
import logging
import tempfile
from pathlib import Path
from datetime import datetime
from PySide6.QtWidgets import QApplication
from Custom_Widgets.Lib_Mainwindow import TheMainWindow


# ---------- Setting logging files ------------------------------------------------------------------------------------
LOG_FILE_PATH = Path(tempfile.gettempdir()) / datetime.now().strftime("%Y%m%d_%H%M%S.log")

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.DEBUG if "debug" in sys.argv else logging.INFO,
)
print(f"--- LOG_FILE_PATH = {LOG_FILE_PATH.__str__()} ----------------------")


# ---------- The main window gui --------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TheMainWindow()
    w.show()
    sys.exit(app.exec())
