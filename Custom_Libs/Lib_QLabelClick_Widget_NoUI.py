import numpy as np
import numpy.typing as npt
from PySide6 import  QtCore #QtGui,
from PySide6.QtWidgets import QLabel, QGroupBox
from PySide6.QtGui import QImage, QPixmap, QMouseEvent


class QLabelClick(QLabel):
    clicked = QtCore.Signal(tuple)  # emitting signal (self.id, click_y, click_x)
    id: int  # id

    img_w: int  # image width
    img_h: int  # image height
    img_c: int  # image channel

    horScale: float  # scale for calculating Actual Pixel Position

    def __init__(self, parent: QLabel | QGroupBox | None = None, id: int = 0) -> None:
        super(QLabelClick, self).__init__(parent)
        self.id = id
        self.horScale = 1

    def setId(self, id: int) -> None:
        self.id = id

    def mousePressEvent(self, event: QMouseEvent) -> None:
        emitting_tuple: tuple[int, int, int] = (
            self.id,
            round(event.position().y() * self.horScale),
            round(event.position().x() * self.horScale),
        )

        self.clicked.emit(emitting_tuple)
        QLabel.mousePressEvent(self, event)
        print(f"pressed {emitting_tuple=}")

    def show_np_img(self, arr: npt.NDArray[np.uint8], outwidth: int = 320) -> None:
        assert arr.ndim == 3
        self.img_h, self.img_w, self.img_c = arr.shape
        self.horScale = self.img_w / outwidth

        assert self.img_c == 3
        qImg = QImage(
            bytes(arr.data),
            self.img_w,
            self.img_h,
            self.img_w * self.img_c,
            QImage.Format.Format_RGB888,
        )
        self.setPixmap(QPixmap.fromImage(qImg).scaledToWidth(outwidth))
