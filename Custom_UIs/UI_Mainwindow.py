# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QFont,
)
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFrame,
    QGridLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QSplitter,
    QStatusBar,
    QTabWidget,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from Custom_Libs.Lib_QLabelClick_Widget_NoUI import QLabelClick


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow) -> None:
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.actionOpen_Directory = QAction(MainWindow)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.actionSave_Raw_Bayer_as = QAction(MainWindow)
        self.actionSave_Raw_Bayer_as.setObjectName("actionSave_Raw_Bayer_as")
        self.actionSave_configuration = QAction(MainWindow)
        self.actionSave_configuration.setObjectName("actionSave_configuration")
        self.actionLoad_geometry_configuration = QAction(MainWindow)
        self.actionLoad_geometry_configuration.setObjectName(
            "actionLoad_geometry_configuration"
        )
        self.actionRead_Tutorial = QAction(MainWindow)
        self.actionRead_Tutorial.setObjectName("actionRead_Tutorial")
        self.actionRead_Dependencies = QAction(MainWindow)
        self.actionRead_Dependencies.setObjectName("actionRead_Dependencies")
        self.actionContact_information = QAction(MainWindow)
        self.actionContact_information.setObjectName("actionContact_information")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionContact = QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.splitter = QSplitter(self.groupBox_3)
        self.splitter.setObjectName("splitter")
        self.splitter.setLineWidth(2)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.gp_webcam_meta = QGroupBox(self.splitter)
        self.gp_webcam_meta.setObjectName("gp_webcam_meta")
        self.verticalLayout = QVBoxLayout(self.gp_webcam_meta)
        self.verticalLayout.setObjectName("verticalLayout")
        self.limg_webcam = QLabelClick(self.gp_webcam_meta)
        self.limg_webcam.setObjectName("limg_webcam")

        self.verticalLayout.addWidget(self.limg_webcam)

        self.tb_meta_json = QTextBrowser(self.gp_webcam_meta)
        self.tb_meta_json.setObjectName("tb_meta_json")
        font = QFont()
        font.setFamilies(["Monospace"])
        self.tb_meta_json.setFont(font)

        self.verticalLayout.addWidget(self.tb_meta_json)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.splitter.addWidget(self.gp_webcam_meta)
        self.gp_spectral_panel = QGroupBox(self.splitter)
        self.gp_spectral_panel.setObjectName("gp_spectral_panel")
        self.gridLayout_4 = QGridLayout(self.gp_spectral_panel)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pb_export = QPushButton(self.gp_spectral_panel)
        self.pb_export.setObjectName("pb_export")

        self.gridLayout_4.addWidget(self.pb_export, 1, 2, 1, 1)

        self.pb_conf_export = QPushButton(self.gp_spectral_panel)
        self.pb_conf_export.setObjectName("pb_conf_export")

        self.gridLayout_4.addWidget(self.pb_conf_export, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(self.gp_spectral_panel)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_6 = QGridLayout(self.tab_1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.limg_bayer_full = QLabelClick(self.tab_1)
        self.limg_bayer_full.setObjectName("limg_bayer_full")

        self.gridLayout_6.addWidget(self.limg_bayer_full, 0, 0, 1, 1)

        self.limg_bayer_gray = QLabelClick(self.tab_1)
        self.limg_bayer_gray.setObjectName("limg_bayer_gray")

        self.gridLayout_6.addWidget(self.limg_bayer_gray, 1, 0, 1, 1)

        self.limg_bayer_obje = QLabelClick(self.tab_1)
        self.limg_bayer_obje.setObjectName("limg_bayer_obje")

        self.gridLayout_6.addWidget(self.limg_bayer_obje, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.limg_raw_spectrum = QLabelClick(self.tab_2)
        self.limg_raw_spectrum.setObjectName("limg_raw_spectrum")

        self.verticalLayout_4.addWidget(self.limg_raw_spectrum)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.limg_refl_spectrum = QLabelClick(self.tab_3)
        self.limg_refl_spectrum.setObjectName("limg_refl_spectrum")

        self.verticalLayout_5.addWidget(self.limg_refl_spectrum)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 3)

        self.splitter.addWidget(self.gp_spectral_panel)

        self.gridLayout_5.addWidget(self.splitter, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 3, 1)

        self.gb_dir_panel = QGroupBox(self.centralwidget)
        self.gb_dir_panel.setObjectName("gb_dir_panel")
        self.gridLayout_3 = QGridLayout(self.gb_dir_panel)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cob_jpeg_selector = QComboBox(self.gb_dir_panel)
        self.cob_jpeg_selector.setObjectName("cob_jpeg_selector")

        self.gridLayout_3.addWidget(self.cob_jpeg_selector, 5, 0, 1, 1)

        self.pb_data_dir = QPushButton(self.gb_dir_panel)
        self.pb_data_dir.setObjectName("pb_data_dir")

        self.gridLayout_3.addWidget(self.pb_data_dir, 1, 0, 1, 1)

        self.le_data_dir = QLineEdit(self.gb_dir_panel)
        self.le_data_dir.setObjectName("le_data_dir")

        self.gridLayout_3.addWidget(self.le_data_dir, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.comboBox = QComboBox(self.gb_dir_panel)
        self.comboBox.setObjectName("comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 4, 0, 1, 1)

        self.tb_data_dir_tree = QTextBrowser(self.gb_dir_panel)
        self.tb_data_dir_tree.setObjectName("tb_data_dir_tree")
        self.tb_data_dir_tree.setFont(font)

        self.gridLayout_3.addWidget(self.tb_data_dir_tree, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.gridLayout.addWidget(self.gb_dir_panel, 0, 0, 1, 1)

        self.gb_control_panel = QGroupBox(self.centralwidget)
        self.gb_control_panel.setObjectName("gb_control_panel")
        self.gridLayout_2 = QGridLayout(self.gb_control_panel)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sb_obje_top_pxl = QSpinBox(self.gb_control_panel)
        self.sb_obje_top_pxl.setObjectName("sb_obje_top_pxl")
        self.sb_obje_top_pxl.setMinimum(500)
        self.sb_obje_top_pxl.setMaximum(2000)
        self.sb_obje_top_pxl.setValue(1200)

        self.gridLayout_2.addWidget(self.sb_obje_top_pxl, 4, 1, 1, 1)

        self.pb_refresh = QPushButton(self.gb_control_panel)
        self.pb_refresh.setObjectName("pb_refresh")

        self.gridLayout_2.addWidget(self.pb_refresh, 6, 1, 1, 2)

        self.sb_horx_left_pxl = QSpinBox(self.gb_control_panel)
        self.sb_horx_left_pxl.setObjectName("sb_horx_left_pxl")
        self.sb_horx_left_pxl.setMinimum(900)
        self.sb_horx_left_pxl.setMaximum(1700)
        self.sb_horx_left_pxl.setValue(1350)

        self.gridLayout_2.addWidget(self.sb_horx_left_pxl, 0, 1, 1, 1)

        self._label_1 = QLabel(self.gb_control_panel)
        self._label_1.setObjectName("_label_1")

        self.gridLayout_2.addWidget(self._label_1, 0, 0, 1, 1)

        self._line = QFrame(self.gb_control_panel)
        self._line.setObjectName("_line")
        self._line.setFrameShape(QFrame.Shape.HLine)
        self._line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self._line, 2, 0, 1, 3)

        self._label_2 = QLabel(self.gb_control_panel)
        self._label_2.setObjectName("_label_2")

        self.gridLayout_2.addWidget(self._label_2, 3, 0, 1, 1)

        self._label_4 = QLabel(self.gb_control_panel)
        self._label_4.setObjectName("_label_4")

        self.gridLayout_2.addWidget(self._label_4, 1, 0, 1, 1)

        self.sb_obje_bot_pxl = QSpinBox(self.gb_control_panel)
        self.sb_obje_bot_pxl.setObjectName("sb_obje_bot_pxl")
        self.sb_obje_bot_pxl.setMinimum(500)
        self.sb_obje_bot_pxl.setMaximum(2000)
        self.sb_obje_bot_pxl.setValue(1250)

        self.gridLayout_2.addWidget(self.sb_obje_bot_pxl, 4, 2, 1, 1)

        self._label_3 = QLabel(self.gb_control_panel)
        self._label_3.setObjectName("_label_3")

        self.gridLayout_2.addWidget(self._label_3, 4, 0, 1, 1)

        self.cb_fraunhofer = QCheckBox(self.gb_control_panel)
        self.cb_fraunhofer.setObjectName("cb_fraunhofer")

        self.gridLayout_2.addWidget(self.cb_fraunhofer, 1, 2, 1, 1)

        self.sb_gray_bot_pxl = QSpinBox(self.gb_control_panel)
        self.sb_gray_bot_pxl.setObjectName("sb_gray_bot_pxl")
        self.sb_gray_bot_pxl.setMinimum(500)
        self.sb_gray_bot_pxl.setMaximum(2000)
        self.sb_gray_bot_pxl.setValue(1100)

        self.gridLayout_2.addWidget(self.sb_gray_bot_pxl, 3, 2, 1, 1)

        self.sb_gray_top_pxl = QSpinBox(self.gb_control_panel)
        self.sb_gray_top_pxl.setObjectName("sb_gray_top_pxl")
        self.sb_gray_top_pxl.setMinimum(500)
        self.sb_gray_top_pxl.setMaximum(2000)
        self.sb_gray_top_pxl.setValue(1050)

        self.gridLayout_2.addWidget(self.sb_gray_top_pxl, 3, 1, 1, 1)

        self.sb_horx_frau_pxl = QSpinBox(self.gb_control_panel)
        self.sb_horx_frau_pxl.setObjectName("sb_horx_frau_pxl")
        self.sb_horx_frau_pxl.setEnabled(False)
        self.sb_horx_frau_pxl.setMaximum(9999)
        self.sb_horx_frau_pxl.setValue(190)

        self.gridLayout_2.addWidget(self.sb_horx_frau_pxl, 1, 1, 1, 1)

        self._line_2 = QFrame(self.gb_control_panel)
        self._line_2.setObjectName("_line_2")
        self._line_2.setFrameShape(QFrame.Shape.HLine)
        self._line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self._line_2, 5, 0, 1, 3)

        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.gridLayout.addWidget(self.gb_control_panel, 2, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTutorial = QMenu(self.menubar)
        self.menuTutorial.setObjectName("menuTutorial")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTutorial.menuAction())
        self.menuFile.addAction(self.actionOpen_Directory)
        self.menuFile.addAction(self.actionLoad_geometry_configuration)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_configuration)
        self.menuFile.addAction(self.actionSave_Raw_Bayer_as)
        self.menuFile.addSeparator()
        self.menuTutorial.addAction(self.actionRead_Tutorial)
        self.menuTutorial.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow: QMainWindow) -> None:
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.actionOpen_Directory.setText(
            QCoreApplication.translate("MainWindow", "Open Directory", None)
        )
        self.actionSave_Raw_Bayer_as.setText(
            QCoreApplication.translate("MainWindow", "Export Raw-Bayer as", None)
        )
        self.actionSave_configuration.setText(
            QCoreApplication.translate(
                "MainWindow", "Save geometry configuration", None
            )
        )
        self.actionLoad_geometry_configuration.setText(
            QCoreApplication.translate(
                "MainWindow", "Load geometry configuration", None
            )
        )
        self.actionRead_Tutorial.setText(
            QCoreApplication.translate("MainWindow", "Open Manual", None)
        )
        self.actionRead_Dependencies.setText(
            QCoreApplication.translate("MainWindow", "Read Dependencies", None)
        )
        self.actionContact_information.setText(
            QCoreApplication.translate("MainWindow", "Contact information", None)
        )
        self.actionAbout.setText(
            QCoreApplication.translate("MainWindow", "About", None)
        )
        self.actionContact.setText(
            QCoreApplication.translate("MainWindow", "Contact", None)
        )
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", "Data", None))
        self.gp_webcam_meta.setTitle(
            QCoreApplication.translate("MainWindow", "Webcam + Meta Data", None)
        )
        self.limg_webcam.setText(QCoreApplication.translate("MainWindow", "....", None))
        self.gp_spectral_panel.setTitle(
            QCoreApplication.translate("MainWindow", "Spectral data Panel", None)
        )
        self.pb_export.setText(QCoreApplication.translate("MainWindow", "Export", None))
        self.pb_conf_export.setText(
            QCoreApplication.translate("MainWindow", "Configure Export", None)
        )
        self.limg_bayer_full.setText(
            QCoreApplication.translate("MainWindow", "....", None)
        )
        self.limg_bayer_gray.setText(
            QCoreApplication.translate("MainWindow", "....", None)
        )
        self.limg_bayer_obje.setText(
            QCoreApplication.translate("MainWindow", "....", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_1),
            QCoreApplication.translate("MainWindow", "Raw Bayer", None),
        )
        self.limg_raw_spectrum.setText(
            QCoreApplication.translate("MainWindow", "....", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "Spectrum (Raw)", None),
        )
        self.limg_refl_spectrum.setText(
            QCoreApplication.translate("MainWindow", "....", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "Spectrum (Reflectance)", None),
        )
        self.gb_dir_panel.setTitle(
            QCoreApplication.translate("MainWindow", "Directory Control Panel", None)
        )
        self.pb_data_dir.setText(
            QCoreApplication.translate("MainWindow", "Open Directory", None)
        )
        self.gb_control_panel.setTitle(
            QCoreApplication.translate("MainWindow", "Geometry control panel", None)
        )
        self.pb_refresh.setText(
            QCoreApplication.translate("MainWindow", "Refresh (Redraw)", None)
        )
        self._label_1.setText(
            QCoreApplication.translate("MainWindow", "Horizontal Left Pixel", None)
        )
        self._label_2.setText(
            QCoreApplication.translate("MainWindow", "Vert. Gray Pixel Range", None)
        )
        self._label_4.setText(
            QCoreApplication.translate("MainWindow", "Horizontal Fraunhofer", None)
        )
        self._label_3.setText(
            QCoreApplication.translate("MainWindow", "Vert. Object Pixel Range", None)
        )
        self.cb_fraunhofer.setText(
            QCoreApplication.translate("MainWindow", "Calibrate", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuTutorial.setTitle(
            QCoreApplication.translate("MainWindow", "Help", None)
        )

    # retranslateUi
