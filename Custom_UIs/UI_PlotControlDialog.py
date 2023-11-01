# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_PlotControlDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    Qt,
)
from PySide6.QtWidgets import (
    QCheckBox,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFormLayout,
    QFrame,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QSpacerItem,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(281, 541)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self._label_5 = QLabel(Dialog)
        self._label_5.setObjectName("_label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self._label_5)

        self.le_title = QLineEdit(Dialog)
        self.le_title.setObjectName("le_title")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_title)

        self._l = QFrame(Dialog)
        self._l.setObjectName("_l")
        self._l.setFrameShape(QFrame.Shape.HLine)
        self._l.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self._l)

        self._label_7 = QLabel(Dialog)
        self._label_7.setObjectName("_label_7")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self._label_7)

        self._label_2 = QLabel(Dialog)
        self._label_2.setObjectName("_label_2")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self._label_2)

        self.le_y_label = QLineEdit(Dialog)
        self.le_y_label.setObjectName("le_y_label")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.le_y_label)

        self._label_3 = QLabel(Dialog)
        self._label_3.setObjectName("_label_3")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self._label_3)

        self.sb_y_range_max = QDoubleSpinBox(Dialog)
        self.sb_y_range_max.setObjectName("sb_y_range_max")
        self.sb_y_range_max.setMinimum(-1000.000000000000000)
        self.sb_y_range_max.setMaximum(1500.000000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.sb_y_range_max)

        self._label_4 = QLabel(Dialog)
        self._label_4.setObjectName("_label_4")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self._label_4)

        self.sb_y_range_min = QDoubleSpinBox(Dialog)
        self.sb_y_range_min.setObjectName("sb_y_range_min")
        self.sb_y_range_min.setMinimum(-1000.000000000000000)
        self.sb_y_range_min.setMaximum(1500.000000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.sb_y_range_min)

        self._l_2 = QFrame(Dialog)
        self._l_2.setObjectName("_l_2")
        self._l_2.setFrameShape(QFrame.Shape.HLine)
        self._l_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self._l_2)

        self._label_8 = QLabel(Dialog)
        self._label_8.setObjectName("_label_8")

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self._label_8)

        self._label_9 = QLabel(Dialog)
        self._label_9.setObjectName("_label_9")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self._label_9)

        self.le_x_label = QLineEdit(Dialog)
        self.le_x_label.setObjectName("le_x_label")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.le_x_label)

        self._label_10 = QLabel(Dialog)
        self._label_10.setObjectName("_label_10")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self._label_10)

        self.sb_x_range_max = QDoubleSpinBox(Dialog)
        self.sb_x_range_max.setObjectName("sb_x_range_max")
        self.sb_x_range_max.setMinimum(-1000.000000000000000)
        self.sb_x_range_max.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.sb_x_range_max)

        self._label_6 = QLabel(Dialog)
        self._label_6.setObjectName("_label_6")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self._label_6)

        self.sb_x_range_min = QDoubleSpinBox(Dialog)
        self.sb_x_range_min.setObjectName("sb_x_range_min")
        self.sb_x_range_min.setMinimum(-1000.000000000000000)
        self.sb_x_range_min.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.sb_x_range_min)

        self._l_3 = QFrame(Dialog)
        self._l_3.setObjectName("_l_3")
        self._l_3.setFrameShape(QFrame.Shape.HLine)
        self._l_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(14, QFormLayout.SpanningRole, self._l_3)

        self.cb_grid = QCheckBox(Dialog)
        self.cb_grid.setObjectName("cb_grid")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_grid)

        self.cb_legend = QCheckBox(Dialog)
        self.cb_legend.setObjectName("cb_legend")
        self.cb_legend.setChecked(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cb_legend)

        self._label_1 = QLabel(Dialog)
        self._label_1.setObjectName("_label_1")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self._label_1)

        self.btn_box = QDialogButtonBox(Dialog)
        self.btn_box.setObjectName("btn_box")
        self.btn_box.setOrientation(Qt.Orientation.Horizontal)
        self.btn_box.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok | QDialogButtonBox.Reset
        )

        self.formLayout.setWidget(20, QFormLayout.SpanningRole, self.btn_box)

        self._label_11 = QLabel(Dialog)
        self._label_11.setObjectName("_label_11")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self._label_11)

        self._label_12 = QLabel(Dialog)
        self._label_12.setObjectName("_label_12")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self._label_12)

        self.sb_fig_size_x = QDoubleSpinBox(Dialog)
        self.sb_fig_size_x.setObjectName("sb_fig_size_x")
        self.sb_fig_size_x.setValue(6.400000000000000)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.sb_fig_size_x)

        self.sb_fig_size_y = QDoubleSpinBox(Dialog)
        self.sb_fig_size_y.setObjectName("sb_fig_size_y")
        self.sb_fig_size_y.setValue(4.800000000000000)

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.sb_fig_size_y)

        self._label = QLabel(Dialog)
        self._label.setObjectName("_label")

        self.formLayout.setWidget(15, QFormLayout.SpanningRole, self._label)

        self._label_13 = QLabel(Dialog)
        self._label_13.setObjectName("_label_13")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self._label_13)

        self.sb_fig_dpi = QDoubleSpinBox(Dialog)
        self.sb_fig_dpi.setObjectName("sb_fig_dpi")
        self.sb_fig_dpi.setMaximum(500.000000000000000)
        self.sb_fig_dpi.setValue(100.000000000000000)

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.sb_fig_dpi)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.formLayout.setItem(19, QFormLayout.LabelRole, self.verticalSpacer)

        self.retranslateUi(Dialog)
        self.btn_box.accepted.connect(Dialog.accept)
        self.btn_box.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self._label_5.setText(QCoreApplication.translate("Dialog", "Title Name", None))
        self.le_title.setText("")
        self._label_7.setText(QCoreApplication.translate("Dialog", "Y axis:", None))
        self._label_2.setText(QCoreApplication.translate("Dialog", "Y Label", None))
        self.le_y_label.setText("")
        self._label_3.setText(
            QCoreApplication.translate("Dialog", "Y Range Max (Top)", None)
        )
        self._label_4.setText(
            QCoreApplication.translate("Dialog", "Y Range Min (Bottom)", None)
        )
        self._label_8.setText(QCoreApplication.translate("Dialog", "X axis:", None))
        self._label_9.setText(QCoreApplication.translate("Dialog", "X axis name", None))
        self.le_x_label.setText("")
        self._label_10.setText(
            QCoreApplication.translate("Dialog", "X Range Max (Right)", None)
        )
        self._label_6.setText(
            QCoreApplication.translate("Dialog", "X Range Min (Left)", None)
        )
        self.cb_grid.setText(QCoreApplication.translate("Dialog", "Grid Lines", None))
        self.cb_legend.setText(QCoreApplication.translate("Dialog", "Legend", None))
        self._label_1.setText(QCoreApplication.translate("Dialog", "General:", None))
        self._label_11.setText(
            QCoreApplication.translate("Dialog", "Output Figure x size", None)
        )
        self._label_12.setText(
            QCoreApplication.translate("Dialog", "Output Figure y size", None)
        )
        self._label.setText(
            QCoreApplication.translate("Dialog", "Plot / figure size", None)
        )
        self._label_13.setText(
            QCoreApplication.translate("Dialog", "Output Figure DPI", None)
        )

    # retranslateUi
