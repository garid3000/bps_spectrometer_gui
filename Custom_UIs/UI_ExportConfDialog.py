# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_ExportConfDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
    QGridLayout,
    QGroupBox,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 0, 2, 1, 1)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb_plot_raw = QCheckBox(self.groupBox_2)
        self.cb_plot_raw.setObjectName("cb_plot_raw")

        self.verticalLayout_2.addWidget(self.cb_plot_raw)

        self.cb_plo_refl = QCheckBox(self.groupBox_2)
        self.cb_plo_refl.setObjectName("cb_plo_refl")

        self.verticalLayout_2.addWidget(self.cb_plo_refl)

        self._vs_3 = QSpacerItem(
            20, 166, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self._vs_3)

        self.cb_numerical = QCheckBox(self.groupBox_2)
        self.cb_numerical.setObjectName("cb_numerical")
        self.cb_numerical.setChecked(True)
        self.cb_numerical.setTristate(False)

        self.verticalLayout_2.addWidget(self.cb_numerical)

        self._vs_4 = QSpacerItem(
            20, 166, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self._vs_4)

        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_tif_1layer = QCheckBox(self.groupBox)
        self.cb_tif_1layer.setObjectName("cb_tif_1layer")

        self.verticalLayout.addWidget(self.cb_tif_1layer)

        self.cb_npy_1layer = QCheckBox(self.groupBox)
        self.cb_npy_1layer.setObjectName("cb_npy_1layer")

        self.verticalLayout.addWidget(self.cb_npy_1layer)

        self.cb_mat_1layer = QCheckBox(self.groupBox)
        self.cb_mat_1layer.setObjectName("cb_mat_1layer")

        self.verticalLayout.addWidget(self.cb_mat_1layer)

        self._vs_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self._vs_2)

        self.cb_tif_3layer = QCheckBox(self.groupBox)
        self.cb_tif_3layer.setObjectName("cb_tif_3layer")

        self.verticalLayout.addWidget(self.cb_tif_3layer)

        self.cb_npy_3layer = QCheckBox(self.groupBox)
        self.cb_npy_3layer.setObjectName("cb_npy_3layer")

        self.verticalLayout.addWidget(self.cb_npy_3layer)

        self.cb_mat_3layer = QCheckBox(self.groupBox)
        self.cb_mat_3layer.setObjectName("cb_mat_3layer")

        self.verticalLayout.addWidget(self.cb_mat_3layer)

        self._vs = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self._vs)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.groupBox_2.setTitle(
            QCoreApplication.translate("Dialog", "Spectrum Export", None)
        )
        self.cb_plot_raw.setText(
            QCoreApplication.translate("Dialog", "Plot Figure Raw (PNG)", None)
        )
        self.cb_plo_refl.setText(
            QCoreApplication.translate("Dialog", "Plot Figure Reflectance (PNG)", None)
        )
        # if QT_CONFIG(whatsthis)
        self.cb_numerical.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.cb_numerical.setText(
            QCoreApplication.translate("Dialog", "Numerical Spectrum Data (CSV)", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("Dialog", "Raw Bayer Export", None)
        )
        self.cb_tif_1layer.setText(
            QCoreApplication.translate("Dialog", "TIFF 10bit (2464x3280)", None)
        )
        self.cb_npy_1layer.setText(
            QCoreApplication.translate("Dialog", "NPY 10bit (2464x3280)", None)
        )
        self.cb_mat_1layer.setText(
            QCoreApplication.translate("Dialog", "MAT 10bit (2464x3280)", None)
        )
        self.cb_tif_3layer.setText(
            QCoreApplication.translate("Dialog", "TIFF 10bit (2464x3280x3)", None)
        )
        self.cb_npy_3layer.setText(
            QCoreApplication.translate("Dialog", "NPY 10bit (2464x3280x3)", None)
        )
        self.cb_mat_3layer.setText(
            QCoreApplication.translate("Dialog", "MAT 10bit (2464x3280x3)", None)
        )

    # retranslateUi
