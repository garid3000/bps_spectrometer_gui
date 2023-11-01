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
    QBrush,
    QColor,
    QFont,
    QPalette,
)
from PySide6.QtWidgets import (
    QCheckBox,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QSplitter,
    QStatusBar,
    QTextBrowser,
    QToolButton,
    QTreeView,
    QVBoxLayout,
    QWidget,
)

from Custom_Libs.Lib_QLabelClick_Widget_NoUI import QLabelClick


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow) -> None:
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 521)
        self.actionOpen_Directory = QAction(MainWindow)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.action_cur_jpeg_export = QAction(MainWindow)
        self.action_cur_jpeg_export.setObjectName("action_cur_jpeg_export")
        self.action_geometry_load = QAction(MainWindow)
        self.action_geometry_load.setObjectName("action_geometry_load")
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.actionRead_Dependencies = QAction(MainWindow)
        self.actionRead_Dependencies.setObjectName("actionRead_Dependencies")
        self.actionContact_information = QAction(MainWindow)
        self.actionContact_information.setObjectName("actionContact_information")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.actionContact = QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.action_cur_jpeg_preview = QAction(MainWindow)
        self.action_cur_jpeg_preview.setObjectName("action_cur_jpeg_preview")
        self.action_dir_goto_parent = QAction(MainWindow)
        self.action_dir_goto_parent.setObjectName("action_dir_goto_parent")
        self.action_dir_goto_cur_child = QAction(MainWindow)
        self.action_dir_goto_cur_child.setObjectName("action_dir_goto_cur_child")
        self.action_dir_cur_child_fold = QAction(MainWindow)
        self.action_dir_cur_child_fold.setObjectName("action_dir_cur_child_fold")
        self.action_dir_cur_child_unfold = QAction(MainWindow)
        self.action_dir_cur_child_unfold.setObjectName("action_dir_cur_child_unfold")
        self.action_cur_file_open = QAction(MainWindow)
        self.action_cur_file_open.setObjectName("action_cur_file_open")
        self.actionsdf = QAction(MainWindow)
        self.actionsdf.setObjectName("actionsdf")
        self.actionSave_geometry_configuration_Ctrl_Shift_L = QAction(MainWindow)
        self.actionSave_geometry_configuration_Ctrl_Shift_L.setObjectName(
            "actionSave_geometry_configuration_Ctrl_Shift_L"
        )
        self.action_dir_ft_filter_toggle = QAction(MainWindow)
        self.action_dir_ft_filter_toggle.setObjectName("action_dir_ft_filter_toggle")
        self.action_tabs_show_tab1 = QAction(MainWindow)
        self.action_tabs_show_tab1.setObjectName("action_tabs_show_tab1")
        self.action_tabs_show_tab2 = QAction(MainWindow)
        self.action_tabs_show_tab2.setObjectName("action_tabs_show_tab2")
        self.action_tabs_show_tab3 = QAction(MainWindow)
        self.action_tabs_show_tab3.setObjectName("action_tabs_show_tab3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gb_dir_panel = QGroupBox(self.layoutWidget)
        self.gb_dir_panel.setObjectName("gb_dir_panel")
        self.gridLayout_3 = QGridLayout(self.gb_dir_panel)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tv_dir = QTreeView(self.gb_dir_panel)
        self.tv_dir.setObjectName("tv_dir")
        font = QFont()
        font.setFamilies(["Monospace"])
        font.setPointSize(10)
        self.tv_dir.setFont(font)
        self.tv_dir.setSortingEnabled(True)

        self.gridLayout_3.addWidget(self.tv_dir, 1, 0, 1, 1)

        self.cb_ft_filter = QCheckBox(self.gb_dir_panel)
        self.cb_ft_filter.setObjectName("cb_ft_filter")
        self.cb_ft_filter.setChecked(True)

        self.gridLayout_3.addWidget(self.cb_ft_filter, 0, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.gb_dir_panel)

        self.gb_control_panel = QGroupBox(self.layoutWidget)
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
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self._label_1.setPalette(palette)

        self.gridLayout_2.addWidget(self._label_1, 0, 0, 1, 1)

        self._line = QFrame(self.gb_control_panel)
        self._line.setObjectName("_line")
        self._line.setFrameShape(QFrame.Shape.HLine)
        self._line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self._line, 2, 0, 1, 3)

        self._label_2 = QLabel(self.gb_control_panel)
        self._label_2.setObjectName("_label_2")
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        self._label_2.setPalette(palette1)

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
        palette2 = QPalette()
        brush2 = QBrush(QColor(0, 0, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        self._label_3.setPalette(palette2)

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

        self.verticalLayout_2.addWidget(self.gb_control_panel)

        self.splitter.addWidget(self.layoutWidget)
        self.gp_webcam_meta = QGroupBox(self.splitter)
        self.gp_webcam_meta.setObjectName("gp_webcam_meta")
        self.verticalLayout = QVBoxLayout(self.gp_webcam_meta)
        self.verticalLayout.setObjectName("verticalLayout")
        self.limg_webcam = QLabelClick(self.gp_webcam_meta)
        self.limg_webcam.setObjectName("limg_webcam")

        self.verticalLayout.addWidget(self.limg_webcam)

        self.tb_meta_json = QTextBrowser(self.gp_webcam_meta)
        self.tb_meta_json.setObjectName("tb_meta_json")
        font1 = QFont()
        font1.setFamilies(["Monospace"])
        self.tb_meta_json.setFont(font1)

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

        self.gridLayout_4.addWidget(self.pb_export, 2, 2, 1, 1)

        self.checkBox_6 = QCheckBox(self.gp_spectral_panel)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_6.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_6, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(self.gp_spectral_panel)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 321, 412))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.label.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(13, QFormLayout.SpanningRole, self.line)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.label_2.setFont(font3)

        self.formLayout.setWidget(15, QFormLayout.SpanningRole, self.label_2)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(21, QFormLayout.SpanningRole, self.line_2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font3)

        self.formLayout.setWidget(23, QFormLayout.SpanningRole, self.label_3)

        self.limg_bayer_full = QLabelClick(self.scrollAreaWidgetContents)
        self.limg_bayer_full.setObjectName("limg_bayer_full")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.limg_bayer_full)

        self.limg_bayer_gray = QLabelClick(self.scrollAreaWidgetContents)
        self.limg_bayer_gray.setObjectName("limg_bayer_gray")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.limg_bayer_gray)

        self.limg_bayer_obje = QLabelClick(self.scrollAreaWidgetContents)
        self.limg_bayer_obje.setObjectName("limg_bayer_obje")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.limg_bayer_obje)

        self.checkBox_4 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_4.setObjectName("checkBox_4")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.checkBox_4)

        self.tbtn_raw_spectrum_config = QToolButton(self.scrollAreaWidgetContents)
        self.tbtn_raw_spectrum_config.setObjectName("tbtn_raw_spectrum_config")

        self.formLayout.setWidget(
            16, QFormLayout.FieldRole, self.tbtn_raw_spectrum_config
        )

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setObjectName("checkBox_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.checkBox_2)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName("checkBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.checkBox)

        self.checkBox_3 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setObjectName("checkBox_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.checkBox_3)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.formLayout.setItem(7, QFormLayout.SpanningRole, self.verticalSpacer)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.formLayout.setItem(20, QFormLayout.SpanningRole, self.verticalSpacer_3)

        self.tbtn_ref_spectrum_config = QToolButton(self.scrollAreaWidgetContents)
        self.tbtn_ref_spectrum_config.setObjectName("tbtn_ref_spectrum_config")

        self.formLayout.setWidget(
            24, QFormLayout.FieldRole, self.tbtn_ref_spectrum_config
        )

        self.checkBox_5 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setObjectName("checkBox_5")

        self.formLayout.setWidget(24, QFormLayout.LabelRole, self.checkBox_5)

        self.limg_ref_spectrum = QLabelClick(self.scrollAreaWidgetContents)
        self.limg_ref_spectrum.setObjectName("limg_ref_spectrum")

        self.formLayout.setWidget(25, QFormLayout.SpanningRole, self.limg_ref_spectrum)

        self.limg_raw_spectrum = QLabelClick(self.scrollAreaWidgetContents)
        self.limg_raw_spectrum.setObjectName("limg_raw_spectrum")

        self.formLayout.setWidget(17, QFormLayout.SpanningRole, self.limg_raw_spectrum)

        self.cb_bayer_show_geometry = QCheckBox(self.scrollAreaWidgetContents)
        self.cb_bayer_show_geometry.setObjectName("cb_bayer_show_geometry")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cb_bayer_show_geometry)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 3)

        self.splitter.addWidget(self.gp_spectral_panel)

        self.verticalLayout_3.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 956, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDirectory_operations = QMenu(self.menuFile)
        self.menuDirectory_operations.setObjectName("menuDirectory_operations")
        self.menuType_Here = QMenu(self.menuFile)
        self.menuType_Here.setObjectName("menuType_Here")
        self.menuFile_Operations_on_selected_file = QMenu(self.menuFile)
        self.menuFile_Operations_on_selected_file.setObjectName(
            "menuFile_Operations_on_selected_file"
        )
        self.menuGeometry_Settings = QMenu(self.menuFile)
        self.menuGeometry_Settings.setObjectName("menuGeometry_Settings")
        self.menuTutorial = QMenu(self.menubar)
        self.menuTutorial.setObjectName("menuTutorial")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTutorial.menuAction())
        self.menuFile.addAction(self.menuDirectory_operations.menuAction())
        self.menuFile.addAction(self.menuFile_Operations_on_selected_file.menuAction())
        self.menuFile.addAction(self.menuGeometry_Settings.menuAction())
        self.menuFile.addAction(self.menuType_Here.menuAction())
        self.menuDirectory_operations.addAction(self.action_dir_cur_child_unfold)
        self.menuDirectory_operations.addAction(self.action_dir_cur_child_fold)
        self.menuDirectory_operations.addAction(self.action_dir_goto_cur_child)
        self.menuDirectory_operations.addAction(self.action_dir_goto_parent)
        self.menuDirectory_operations.addAction(self.action_dir_ft_filter_toggle)
        self.menuFile_Operations_on_selected_file.addAction(
            self.action_cur_jpeg_preview
        )
        self.menuFile_Operations_on_selected_file.addAction(self.action_cur_jpeg_export)
        self.menuFile_Operations_on_selected_file.addAction(self.action_cur_file_open)
        self.menuGeometry_Settings.addAction(self.action_geometry_load)
        self.menuGeometry_Settings.addAction(
            self.actionSave_geometry_configuration_Ctrl_Shift_L
        )
        self.menuTutorial.addAction(self.action_help)
        self.menuTutorial.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow: QMainWindow) -> None:
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.actionOpen_Directory.setText(
            QCoreApplication.translate("MainWindow", "Open Directory", None)
        )
        self.action_cur_jpeg_export.setText(
            QCoreApplication.translate("MainWindow", "Export (Ctlr-E)", None)
        )
        self.action_geometry_load.setText(
            QCoreApplication.translate(
                "MainWindow", "Load geometry configuration (Ctrl + L)", None
            )
        )
        self.action_help.setText(
            QCoreApplication.translate("MainWindow", "Help (Ctrl+H)", None)
        )
        self.actionRead_Dependencies.setText(
            QCoreApplication.translate("MainWindow", "Read Dependencies", None)
        )
        self.actionContact_information.setText(
            QCoreApplication.translate("MainWindow", "Contact information", None)
        )
        self.action_about.setText(
            QCoreApplication.translate("MainWindow", "About (Ctrl+A)", None)
        )
        self.actionContact.setText(
            QCoreApplication.translate("MainWindow", "Contact", None)
        )
        self.action_cur_jpeg_preview.setText(
            QCoreApplication.translate("MainWindow", "Preview (Space)", None)
        )
        self.action_dir_goto_parent.setText(
            QCoreApplication.translate(
                "MainWindow", "Go to Parent Directory (Backspace)", None
            )
        )
        self.action_dir_goto_cur_child.setText(
            QCoreApplication.translate(
                "MainWindow", "Go inside Selected Directory (Enter)", None
            )
        )
        self.action_dir_cur_child_fold.setText(
            QCoreApplication.translate(
                "MainWindow", "Fold Selected Directory (Left Arrow)", None
            )
        )
        self.action_dir_cur_child_unfold.setText(
            QCoreApplication.translate(
                "MainWindow", "Unfold Selected Directory (Right Arrow)", None
            )
        )
        self.action_cur_file_open.setText(
            QCoreApplication.translate(
                "MainWindow", "Open with an external app (Ctrl+O)", None
            )
        )
        self.actionsdf.setText(QCoreApplication.translate("MainWindow", "sdf", None))
        self.actionSave_geometry_configuration_Ctrl_Shift_L.setText(
            QCoreApplication.translate(
                "MainWindow", "Save geometry configuration (Ctrl + Shift + L)", None
            )
        )
        self.action_dir_ft_filter_toggle.setText(
            QCoreApplication.translate(
                "MainWindow", "File type filter toggle (Ctrl+F)", None
            )
        )
        self.action_tabs_show_tab1.setText(
            QCoreApplication.translate(
                "MainWindow", "Raw Bayer Tab (Ctrl+1) or (Alt+1)", None
            )
        )
        self.action_tabs_show_tab2.setText(
            QCoreApplication.translate(
                "MainWindow", "Spectrum-Raw Tab (Ctrl+2) or (Alt+2)", None
            )
        )
        self.action_tabs_show_tab3.setText(
            QCoreApplication.translate(
                "MainWindow", "Spectrum-Reflectance Tab (Ctrl+3) or (Alt+3)", None
            )
        )
        self.gb_dir_panel.setTitle(
            QCoreApplication.translate("MainWindow", "Directory Control Panel", None)
        )
        self.cb_ft_filter.setText(
            QCoreApplication.translate("MainWindow", "File type filter (Ctrl-F)", None)
        )
        self.gb_control_panel.setTitle(
            QCoreApplication.translate("MainWindow", "Geometry control panel", None)
        )
        self.pb_refresh.setText(
            QCoreApplication.translate("MainWindow", "Refresh (Ctrl+R)", None)
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
        self.gp_webcam_meta.setTitle(
            QCoreApplication.translate("MainWindow", "Webcam + Meta Data Panel", None)
        )
        self.limg_webcam.setText(QCoreApplication.translate("MainWindow", "....", None))
        self.gp_spectral_panel.setTitle(
            QCoreApplication.translate("MainWindow", "Spectral Data Panel", None)
        )
        self.pb_export.setText(
            QCoreApplication.translate("MainWindow", "Export (Ctrl+E)", None)
        )
        self.checkBox_6.setText(
            QCoreApplication.translate(
                "MainWindow", "Export Numerical Values  (CSV)", None
            )
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "1. Raw Bayer", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow", "2. Raw Spectrum (Ditigal Number)", None
            )
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "3. Spectrum (Reflectance)", None)
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
        self.checkBox_4.setText(
            QCoreApplication.translate("MainWindow", "Export Plot (PNG)", None)
        )
        self.tbtn_raw_spectrum_config.setText(
            QCoreApplication.translate("MainWindow", "Plot Config (Ctrl+Shift+P)", None)
        )
        self.checkBox_2.setText(
            QCoreApplication.translate("MainWindow", "Export (Bayer as NPY)", None)
        )
        self.checkBox.setText(
            QCoreApplication.translate("MainWindow", "Export (Bayer as TIF)", None)
        )
        self.checkBox_3.setText(
            QCoreApplication.translate("MainWindow", "Export (Bayer as MAT)", None)
        )
        self.tbtn_ref_spectrum_config.setText(
            QCoreApplication.translate("MainWindow", "Plot Config (Ctrl+P)", None)
        )
        self.checkBox_5.setText(
            QCoreApplication.translate("MainWindow", "Export Plot (PNG)", None)
        )
        self.limg_ref_spectrum.setText(
            QCoreApplication.translate("MainWindow", "....", None)
        )
        self.limg_raw_spectrum.setText(
            QCoreApplication.translate("MainWindow", "....", None)
        )
        self.cb_bayer_show_geometry.setText(
            QCoreApplication.translate("MainWindow", "Draw Geometry", None)
        )
        self.menuFile.setTitle(
            QCoreApplication.translate("MainWindow", "Operation", None)
        )
        self.menuDirectory_operations.setTitle(
            QCoreApplication.translate("MainWindow", "Directory Movements", None)
        )
        self.menuType_Here.setTitle(
            QCoreApplication.translate("MainWindow", "Type Here", None)
        )
        self.menuFile_Operations_on_selected_file.setTitle(
            QCoreApplication.translate(
                "MainWindow", "File Operations (on selected file)", None
            )
        )
        self.menuGeometry_Settings.setTitle(
            QCoreApplication.translate("MainWindow", "Geometry Settings", None)
        )
        self.menuTutorial.setTitle(
            QCoreApplication.translate("MainWindow", "Help", None)
        )

    # retranslateUi
