# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
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
    QDoubleSpinBox,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpinBox,
    QSplitter,
    QStatusBar,
    QTabWidget,
    QTextBrowser,
    QTreeView,
    QVBoxLayout,
    QWidget,
)

from Custom_Libs.Lib_QLabelClick_Widget_NoUI import QLabelClick
from pyqtgraph import ImageView, PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow) -> None:
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1229, 748)
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
        self.gridLayout = QGridLayout(self.gb_dir_panel)
        self.gridLayout.setObjectName("gridLayout")
        self.pb_dir_goto_parent = QPushButton(self.gb_dir_panel)
        self.pb_dir_goto_parent.setObjectName("pb_dir_goto_parent")

        self.gridLayout.addWidget(self.pb_dir_goto_parent, 1, 0, 1, 1)

        self.tv_dir = QTreeView(self.gb_dir_panel)
        self.tv_dir.setObjectName("tv_dir")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.tv_dir.sizePolicy().hasHeightForWidth())
        self.tv_dir.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies(["Monospace"])
        font.setPointSize(10)
        self.tv_dir.setFont(font)
        self.tv_dir.setSortingEnabled(True)

        self.gridLayout.addWidget(self.tv_dir, 2, 0, 1, 2)

        self.cb_ft_filter = QCheckBox(self.gb_dir_panel)
        self.cb_ft_filter.setObjectName("cb_ft_filter")
        self.cb_ft_filter.setChecked(True)

        self.gridLayout.addWidget(self.cb_ft_filter, 0, 0, 1, 2)

        self.limg_webcam = QLabelClick(self.gb_dir_panel)
        self.limg_webcam.setObjectName("limg_webcam")

        self.gridLayout.addWidget(self.limg_webcam, 3, 0, 1, 2)

        self.tb_meta_json = QTextBrowser(self.gb_dir_panel)
        self.tb_meta_json.setObjectName("tb_meta_json")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.tb_meta_json.sizePolicy().hasHeightForWidth()
        )
        self.tb_meta_json.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies(["Monospace"])
        self.tb_meta_json.setFont(font1)

        self.gridLayout.addWidget(self.tb_meta_json, 4, 0, 1, 2)

        self.verticalLayout_2.addWidget(self.gb_dir_panel)

        self.splitter.addWidget(self.layoutWidget)
        self.gp_webcam_meta = QGroupBox(self.splitter)
        self.gp_webcam_meta.setObjectName("gp_webcam_meta")
        self.verticalLayout = QVBoxLayout(self.gp_webcam_meta)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QScrollArea(self.gp_webcam_meta)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 458, 424))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graph_2dimg = ImageView(self.scrollAreaWidgetContents_2)
        self.graph_2dimg.setObjectName("graph_2dimg")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy2.setHorizontalStretch(200)
        sizePolicy2.setVerticalStretch(200)
        sizePolicy2.setHeightForWidth(self.graph_2dimg.sizePolicy().hasHeightForWidth())
        self.graph_2dimg.setSizePolicy(sizePolicy2)
        self.graph_2dimg.setMinimumSize(QSize(400, 200))

        self.verticalLayout_4.addWidget(self.graph_2dimg)

        self.graph_raw = PlotWidget(self.scrollAreaWidgetContents_2)
        self.graph_raw.setObjectName("graph_raw")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(200)
        sizePolicy3.setHeightForWidth(self.graph_raw.sizePolicy().hasHeightForWidth())
        self.graph_raw.setSizePolicy(sizePolicy3)
        self.graph_raw.setMinimumSize(QSize(400, 200))

        self.verticalLayout_4.addWidget(self.graph_raw)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea_2)

        self.gb_control_panel = QGroupBox(self.gp_webcam_meta)
        self.gb_control_panel.setObjectName("gb_control_panel")
        self.gridLayout_2 = QGridLayout(self.gb_control_panel)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sb_waveperpixel = QDoubleSpinBox(self.gb_control_panel)
        self.sb_waveperpixel.setObjectName("sb_waveperpixel")
        self.sb_waveperpixel.setDecimals(4)
        self.sb_waveperpixel.setMinimum(1.500000000000000)
        self.sb_waveperpixel.setMaximum(2.500000000000000)
        self.sb_waveperpixel.setSingleStep(2.000000000000000)
        self.sb_waveperpixel.setValue(1.858300000000000)

        self.gridLayout_2.addWidget(self.sb_waveperpixel, 11, 1, 1, 1)

        self._l_5 = QLabel(self.gb_control_panel)
        self._l_5.setObjectName("_l_5")

        self.gridLayout_2.addWidget(self._l_5, 5, 3, 1, 1)

        self._l_11 = QLabel(self.gb_control_panel)
        self._l_11.setObjectName("_l_11")

        self.gridLayout_2.addWidget(self._l_11, 5, 1, 1, 1)

        self._l_1 = QLabel(self.gb_control_panel)
        self._l_1.setObjectName("_l_1")
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self._l_1.setPalette(palette)

        self.gridLayout_2.addWidget(self._l_1, 1, 0, 1, 1)

        self.sb_midx_init = QSpinBox(self.gb_control_panel)
        self.sb_midx_init.setObjectName("sb_midx_init")
        self.sb_midx_init.setMinimum(0)
        self.sb_midx_init.setMaximum(17000)
        self.sb_midx_init.setSingleStep(2)
        self.sb_midx_init.setValue(1350)

        self.gridLayout_2.addWidget(self.sb_midx_init, 1, 1, 1, 1)

        self.sb_midx_size = QSpinBox(self.gb_control_panel)
        self.sb_midx_size.setObjectName("sb_midx_size")
        self.sb_midx_size.setEnabled(False)
        self.sb_midx_size.setMaximum(9999)
        self.sb_midx_size.setValue(700)

        self.gridLayout_2.addWidget(self.sb_midx_size, 1, 2, 1, 1)

        self._l_4 = QLabel(self.gb_control_panel)
        self._l_4.setObjectName("_l_4")

        self.gridLayout_2.addWidget(self._l_4, 5, 2, 1, 1)

        self._line = QFrame(self.gb_control_panel)
        self._line.setObjectName("_line")
        self._line.setFrameShape(QFrame.Shape.HLine)
        self._line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self._line, 4, 0, 1, 4)

        self.sb_rigx_init_rel = QSpinBox(self.gb_control_panel)
        self.sb_rigx_init_rel.setObjectName("sb_rigx_init_rel")
        self.sb_rigx_init_rel.setMinimum(700)
        self.sb_rigx_init_rel.setMaximum(9999)
        self.sb_rigx_init_rel.setSingleStep(2)
        self.sb_rigx_init_rel.setValue(710)

        self.gridLayout_2.addWidget(self.sb_rigx_init_rel, 3, 1, 1, 1)

        self.sb_rigx_size = QSpinBox(self.gb_control_panel)
        self.sb_rigx_size.setObjectName("sb_rigx_size")
        self.sb_rigx_size.setMaximum(200)
        self.sb_rigx_size.setSingleStep(2)
        self.sb_rigx_size.setValue(40)

        self.gridLayout_2.addWidget(self.sb_rigx_size, 3, 2, 1, 1)

        self._l_2 = QLabel(self.gb_control_panel)
        self._l_2.setObjectName("_l_2")
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        self._l_2.setPalette(palette1)

        self.gridLayout_2.addWidget(self._l_2, 6, 0, 1, 1)

        self._l_9 = QLabel(self.gb_control_panel)
        self._l_9.setObjectName("_l_9")

        self.gridLayout_2.addWidget(self._l_9, 0, 2, 1, 1)

        self.sb_gray_y_init = QSpinBox(self.gb_control_panel)
        self.sb_gray_y_init.setObjectName("sb_gray_y_init")
        self.sb_gray_y_init.setMinimum(0)
        self.sb_gray_y_init.setMaximum(20000)
        self.sb_gray_y_init.setSingleStep(2)
        self.sb_gray_y_init.setValue(1050)

        self.gridLayout_2.addWidget(self.sb_gray_y_init, 6, 1, 1, 1)

        self._l_7 = QLabel(self.gb_control_panel)
        self._l_7.setObjectName("_l_7")

        self.gridLayout_2.addWidget(self._l_7, 3, 0, 1, 1)

        self.sb_rigx_ends = QSpinBox(self.gb_control_panel)
        self.sb_rigx_ends.setObjectName("sb_rigx_ends")
        self.sb_rigx_ends.setEnabled(False)
        self.sb_rigx_ends.setMaximum(9999)

        self.gridLayout_2.addWidget(self.sb_rigx_ends, 3, 3, 1, 1)

        self.sb_lefx_init_rel = QSpinBox(self.gb_control_panel)
        self.sb_lefx_init_rel.setObjectName("sb_lefx_init_rel")
        self.sb_lefx_init_rel.setMinimum(-250)
        self.sb_lefx_init_rel.setMaximum(-200)
        self.sb_lefx_init_rel.setSingleStep(2)
        self.sb_lefx_init_rel.setValue(-200)

        self.gridLayout_2.addWidget(self.sb_lefx_init_rel, 2, 1, 1, 1)

        self._l_8 = QLabel(self.gb_control_panel)
        self._l_8.setObjectName("_l_8")

        self.gridLayout_2.addWidget(self._l_8, 0, 1, 1, 1)

        self.sb_lefx_size = QSpinBox(self.gb_control_panel)
        self.sb_lefx_size.setObjectName("sb_lefx_size")
        self.sb_lefx_size.setMaximum(200)
        self.sb_lefx_size.setSingleStep(2)
        self.sb_lefx_size.setValue(100)

        self.gridLayout_2.addWidget(self.sb_lefx_size, 2, 2, 1, 1)

        self.sb_obje_y_size = QSpinBox(self.gb_control_panel)
        self.sb_obje_y_size.setObjectName("sb_obje_y_size")
        self.sb_obje_y_size.setMinimum(0)
        self.sb_obje_y_size.setMaximum(20000)
        self.sb_obje_y_size.setSingleStep(2)
        self.sb_obje_y_size.setValue(50)

        self.gridLayout_2.addWidget(self.sb_obje_y_size, 9, 2, 1, 1)

        self.sb_gray_y_ends = QSpinBox(self.gb_control_panel)
        self.sb_gray_y_ends.setObjectName("sb_gray_y_ends")
        self.sb_gray_y_ends.setEnabled(False)
        self.sb_gray_y_ends.setMaximum(99999999)

        self.gridLayout_2.addWidget(self.sb_gray_y_ends, 6, 3, 1, 1)

        self._l_3 = QLabel(self.gb_control_panel)
        self._l_3.setObjectName("_l_3")
        palette2 = QPalette()
        brush2 = QBrush(QColor(0, 0, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        self._l_3.setPalette(palette2)

        self.gridLayout_2.addWidget(self._l_3, 9, 0, 1, 1)

        self._l_10 = QLabel(self.gb_control_panel)
        self._l_10.setObjectName("_l_10")
        self._l_10.setProperty("checked", True)

        self.gridLayout_2.addWidget(self._l_10, 0, 3, 1, 1)

        self.sb_lefx_ends = QSpinBox(self.gb_control_panel)
        self.sb_lefx_ends.setObjectName("sb_lefx_ends")
        self.sb_lefx_ends.setEnabled(False)
        self.sb_lefx_ends.setMaximum(9999)

        self.gridLayout_2.addWidget(self.sb_lefx_ends, 2, 3, 1, 1)

        self.sb_midx_ends = QSpinBox(self.gb_control_panel)
        self.sb_midx_ends.setObjectName("sb_midx_ends")
        self.sb_midx_ends.setEnabled(False)
        self.sb_midx_ends.setMaximum(99999)

        self.gridLayout_2.addWidget(self.sb_midx_ends, 1, 3, 1, 1)

        self.sb_obje_y_init = QSpinBox(self.gb_control_panel)
        self.sb_obje_y_init.setObjectName("sb_obje_y_init")
        self.sb_obje_y_init.setMinimum(0)
        self.sb_obje_y_init.setMaximum(20000)
        self.sb_obje_y_init.setSingleStep(2)
        self.sb_obje_y_init.setValue(1200)

        self.gridLayout_2.addWidget(self.sb_obje_y_init, 9, 1, 1, 1)

        self._l_6 = QLabel(self.gb_control_panel)
        self._l_6.setObjectName("_l_6")

        self.gridLayout_2.addWidget(self._l_6, 2, 0, 1, 1)

        self.sb_obje_y_ends = QSpinBox(self.gb_control_panel)
        self.sb_obje_y_ends.setObjectName("sb_obje_y_ends")
        self.sb_obje_y_ends.setEnabled(False)
        self.sb_obje_y_ends.setMaximum(999999999)

        self.gridLayout_2.addWidget(self.sb_obje_y_ends, 9, 3, 1, 1)

        self.sb_gray_y_size = QSpinBox(self.gb_control_panel)
        self.sb_gray_y_size.setObjectName("sb_gray_y_size")
        self.sb_gray_y_size.setMinimum(0)
        self.sb_gray_y_size.setMaximum(20000)
        self.sb_gray_y_size.setSingleStep(2)
        self.sb_gray_y_size.setValue(50)

        self.gridLayout_2.addWidget(self.sb_gray_y_size, 6, 2, 1, 1)

        self.line_3 = QFrame(self.gb_control_panel)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 10, 0, 1, 4)

        self._l = QLabel(self.gb_control_panel)
        self._l.setObjectName("_l")

        self.gridLayout_2.addWidget(self._l, 11, 0, 1, 1)

        self.pb_waveperpixel_reset = QPushButton(self.gb_control_panel)
        self.pb_waveperpixel_reset.setObjectName("pb_waveperpixel_reset")

        self.gridLayout_2.addWidget(self.pb_waveperpixel_reset, 11, 2, 1, 1)

        self.verticalLayout.addWidget(self.gb_control_panel)

        self.splitter.addWidget(self.gp_webcam_meta)
        self.gp_spectral_panel = QGroupBox(self.splitter)
        self.gp_spectral_panel.setObjectName("gp_spectral_panel")
        self.formLayout = QFormLayout(self.gp_spectral_panel)
        self.formLayout.setObjectName("formLayout")
        self.pb_calibrate_calculate = QPushButton(self.gp_spectral_panel)
        self.pb_calibrate_calculate.setObjectName("pb_calibrate_calculate")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.pb_calibrate_calculate.sizePolicy().hasHeightForWidth()
        )
        self.pb_calibrate_calculate.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pb_calibrate_calculate)

        self.pbar_calc = QProgressBar(self.gp_spectral_panel)
        self.pbar_calc.setObjectName("pbar_calc")
        self.pbar_calc.setMaximum(100)
        self.pbar_calc.setValue(0)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pbar_calc)

        self.scrollArea = QScrollArea(self.gp_spectral_panel)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 372, 539))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cb_calc1_desalt = QCheckBox(self.tab)
        self.cb_calc1_desalt.setObjectName("cb_calc1_desalt")
        self.cb_calc1_desalt.setEnabled(False)
        self.cb_calc1_desalt.setCheckable(True)
        self.cb_calc1_desalt.setChecked(True)

        self.verticalLayout_5.addWidget(self.cb_calc1_desalt)

        self.graph_calc1_desalted_roi = ImageView(self.tab)
        self.graph_calc1_desalted_roi.setObjectName("graph_calc1_desalted_roi")
        sizePolicy5 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.graph_calc1_desalted_roi.sizePolicy().hasHeightForWidth()
        )
        self.graph_calc1_desalted_roi.setSizePolicy(sizePolicy5)
        self.graph_calc1_desalted_roi.setMinimumSize(QSize(150, 0))

        self.verticalLayout_5.addWidget(self.graph_calc1_desalted_roi)

        self.txt_calc1_desalt = QTextBrowser(self.tab)
        self.txt_calc1_desalt.setObjectName("txt_calc1_desalt")
        sizePolicy6 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(
            self.txt_calc1_desalt.sizePolicy().hasHeightForWidth()
        )
        self.txt_calc1_desalt.setSizePolicy(sizePolicy6)
        self.txt_calc1_desalt.setMinimumSize(QSize(0, 0))
        self.txt_calc1_desalt.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_5.addWidget(self.txt_calc1_desalt)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cb_calc2_background = QCheckBox(self.tab_2)
        self.cb_calc2_background.setObjectName("cb_calc2_background")
        self.cb_calc2_background.setEnabled(False)
        self.cb_calc2_background.setChecked(True)

        self.verticalLayout_6.addWidget(self.cb_calc2_background)

        self.graph_calc2_bg_gray = PlotWidget(self.tab_2)
        self.graph_calc2_bg_gray.setObjectName("graph_calc2_bg_gray")
        self.graph_calc2_bg_gray.setMinimumSize(QSize(100, 200))

        self.verticalLayout_6.addWidget(self.graph_calc2_bg_gray)

        self.graph_calc2_bg_obje = PlotWidget(self.tab_2)
        self.graph_calc2_bg_obje.setObjectName("graph_calc2_bg_obje")

        self.verticalLayout_6.addWidget(self.graph_calc2_bg_obje)

        self.txt_calc2_bg = QTextBrowser(self.tab_2)
        self.txt_calc2_bg.setObjectName("txt_calc2_bg")
        sizePolicy6.setHeightForWidth(
            self.txt_calc2_bg.sizePolicy().hasHeightForWidth()
        )
        self.txt_calc2_bg.setSizePolicy(sizePolicy6)
        self.txt_calc2_bg.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_6.addWidget(self.txt_calc2_bg)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_7 = QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.cb_calc3_calibrate_759 = QCheckBox(self.tab_3)
        self.cb_calc3_calibrate_759.setObjectName("cb_calc3_calibrate_759")
        self.cb_calc3_calibrate_759.setEnabled(False)
        self.cb_calc3_calibrate_759.setChecked(True)

        self.verticalLayout_7.addWidget(self.cb_calc3_calibrate_759)

        self.graph_calc3_759_calib = PlotWidget(self.tab_3)
        self.graph_calc3_759_calib.setObjectName("graph_calc3_759_calib")
        sizePolicy7 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(200)
        sizePolicy7.setHeightForWidth(
            self.graph_calc3_759_calib.sizePolicy().hasHeightForWidth()
        )
        self.graph_calc3_759_calib.setSizePolicy(sizePolicy7)
        self.graph_calc3_759_calib.setMinimumSize(QSize(300, 200))

        self.verticalLayout_7.addWidget(self.graph_calc3_759_calib)

        self.txt_calc3_cal759 = QTextBrowser(self.tab_3)
        self.txt_calc3_cal759.setObjectName("txt_calc3_cal759")
        self.txt_calc3_cal759.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_7.addWidget(self.txt_calc3_cal759)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_9 = QVBoxLayout(self.tab_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.graph_calc4_refl_rgb = PlotWidget(self.tab_4)
        self.graph_calc4_refl_rgb.setObjectName("graph_calc4_refl_rgb")

        self.verticalLayout_9.addWidget(self.graph_calc4_refl_rgb)

        self.txt_calc4_rgb = QTextBrowser(self.tab_4)
        self.txt_calc4_rgb.setObjectName("txt_calc4_rgb")
        self.txt_calc4_rgb.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_9.addWidget(self.txt_calc4_rgb)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.formLayout_2 = QFormLayout(self.tab_5)
        self.formLayout_2.setObjectName("formLayout_2")
        self._l_12 = QLabel(self.tab_5)
        self._l_12.setObjectName("_l_12")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self._l_12)

        self.sb_calc5_norm_zero = QDoubleSpinBox(self.tab_5)
        self.sb_calc5_norm_zero.setObjectName("sb_calc5_norm_zero")
        self.sb_calc5_norm_zero.setEnabled(False)
        self.sb_calc5_norm_zero.setDecimals(1)
        self.sb_calc5_norm_zero.setMinimum(400.000000000000000)
        self.sb_calc5_norm_zero.setMaximum(900.000000000000000)
        self.sb_calc5_norm_zero.setSingleStep(0.500000000000000)
        self.sb_calc5_norm_zero.setValue(440.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.sb_calc5_norm_zero)

        self.sb_calc5_norm_one = QDoubleSpinBox(self.tab_5)
        self.sb_calc5_norm_one.setObjectName("sb_calc5_norm_one")
        self.sb_calc5_norm_one.setEnabled(False)
        self.sb_calc5_norm_one.setDecimals(1)
        self.sb_calc5_norm_one.setMinimum(400.000000000000000)
        self.sb_calc5_norm_one.setMaximum(900.000000000000000)
        self.sb_calc5_norm_one.setSingleStep(0.500000000000000)
        self.sb_calc5_norm_one.setValue(760.000000000000000)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.sb_calc5_norm_one)

        self.graph_calc5_refl_final = PlotWidget(self.tab_5)
        self.graph_calc5_refl_final.setObjectName("graph_calc5_refl_final")
        self.graph_calc5_refl_final.setMinimumSize(QSize(300, 300))

        self.formLayout_2.setWidget(
            3, QFormLayout.SpanningRole, self.graph_calc5_refl_final
        )

        self._l_13 = QLabel(self.tab_5)
        self._l_13.setObjectName("_l_13")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self._l_13)

        self.cb_calc5_norm = QCheckBox(self.tab_5)
        self.cb_calc5_norm.setObjectName("cb_calc5_norm")
        self.cb_calc5_norm.setChecked(False)

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.cb_calc5_norm)

        self.txt_calc5_refl_final = QTextBrowser(self.tab_5)
        self.txt_calc5_refl_final.setObjectName("txt_calc5_refl_final")
        self.txt_calc5_refl_final.setMaximumSize(QSize(16777215, 80))

        self.formLayout_2.setWidget(
            4, QFormLayout.SpanningRole, self.txt_calc5_refl_final
        )

        self.tabWidget.addTab(self.tab_5, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.scrollArea)

        self.cb_export_bayer_as_npy = QCheckBox(self.gp_spectral_panel)
        self.cb_export_bayer_as_npy.setObjectName("cb_export_bayer_as_npy")
        self.cb_export_bayer_as_npy.setEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.cb_export_bayer_as_npy)

        self.cb_export_bayer_as_mat = QCheckBox(self.gp_spectral_panel)
        self.cb_export_bayer_as_mat.setObjectName("cb_export_bayer_as_mat")
        self.cb_export_bayer_as_mat.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_export_bayer_as_mat)

        self.cb_export_ref_CSV_simple = QCheckBox(self.gp_spectral_panel)
        self.cb_export_ref_CSV_simple.setObjectName("cb_export_ref_CSV_simple")
        self.cb_export_ref_CSV_simple.setChecked(True)

        self.formLayout.setWidget(
            3, QFormLayout.LabelRole, self.cb_export_ref_CSV_simple
        )

        self.cb_export_ref_CSV_full = QCheckBox(self.gp_spectral_panel)
        self.cb_export_ref_CSV_full.setObjectName("cb_export_ref_CSV_full")
        self.cb_export_ref_CSV_full.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.cb_export_ref_CSV_full)

        self.pb_export = QPushButton(self.gp_spectral_panel)
        self.pb_export.setObjectName("pb_export")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.pb_export)

        self.pbar_export = QProgressBar(self.gp_spectral_panel)
        self.pbar_export.setObjectName("pbar_export")
        self.pbar_export.setValue(0)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pbar_export)

        self.splitter.addWidget(self.gp_spectral_panel)

        self.verticalLayout_3.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1229, 19))
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
        self.pb_dir_goto_parent.setText(
            QCoreApplication.translate(
                "MainWindow", "\u2b06 Go to parent (Backspace)", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.cb_ft_filter.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Filter out (CSV, JPEG, JPG) files", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.cb_ft_filter.setText(
            QCoreApplication.translate("MainWindow", "Filter File Type (Ctrl+F)", None)
        )
        self.limg_webcam.setText(QCoreApplication.translate("MainWindow", "....", None))
        self.gp_webcam_meta.setTitle(
            QCoreApplication.translate(
                "MainWindow",
                "Raw-Bayer Image: ROI (Region of Interest) selection",
                None,
            )
        )
        self.gb_control_panel.setTitle("")
        self._l_5.setText(
            QCoreApplication.translate("MainWindow", "Bottom (pixel)", None)
        )
        self._l_11.setText(
            QCoreApplication.translate("MainWindow", "Top (pixel)", None)
        )
        self._l_1.setText(
            QCoreApplication.translate("MainWindow", "Hor. (center)", None)
        )
        self._l_4.setText(
            QCoreApplication.translate("MainWindow", "Height (pixel)", None)
        )
        self._l_2.setText(
            QCoreApplication.translate("MainWindow", "Vert. Gray Pixel Range", None)
        )
        self._l_9.setText(
            QCoreApplication.translate("MainWindow", "Width (pixel)", None)
        )
        self._l_7.setText(
            QCoreApplication.translate(
                "MainWindow", "Hor. (right) relative to center", None
            )
        )
        self._l_8.setText(
            QCoreApplication.translate("MainWindow", "Start (pixel)", None)
        )
        self._l_3.setText(
            QCoreApplication.translate("MainWindow", "Vert. Object Pixel Range", None)
        )
        self._l_10.setText(
            QCoreApplication.translate("MainWindow", "End (pixel)", None)
        )
        # if QT_CONFIG(tooltip)
        self.sb_lefx_ends.setToolTip(
            QCoreApplication.translate("MainWindow", "Fraunhofer line (in pixel)", None)
        )
        # endif // QT_CONFIG(tooltip)
        self._l_6.setText(
            QCoreApplication.translate(
                "MainWindow", "Hor. (left) relative to center", None
            )
        )
        self._l.setText(
            QCoreApplication.translate(
                "MainWindow", "Wavelength per pixel (nm/px)", None
            )
        )
        self.pb_waveperpixel_reset.setText(
            QCoreApplication.translate("MainWindow", "Reset", None)
        )
        self.gp_spectral_panel.setTitle(
            QCoreApplication.translate(
                "MainWindow", "Spectral Reflection Calculation", None
            )
        )
        self.pb_calibrate_calculate.setText(
            QCoreApplication.translate("MainWindow", "Calculate (Ctrl+R)", None)
        )
        self.cb_calc1_desalt.setText(
            QCoreApplication.translate(
                "MainWindow", "Median filtering (3px vertically) for SALT noise", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "De-Salt", None),
        )
        self.cb_calc2_background.setText(
            QCoreApplication.translate(
                "MainWindow", "Estimate and substract Background", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "BG est.", None),
        )
        self.cb_calc3_calibrate_759.setText(
            QCoreApplication.translate(
                "MainWindow", "Calibrate Based on 759.3nm absorption", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "759 calib.", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_4),
            QCoreApplication.translate("MainWindow", "Refl. (RGB)", None),
        )
        self._l_12.setText(
            QCoreApplication.translate("MainWindow", "0 ~ Wavelenght (nm)", None)
        )
        self._l_13.setText(
            QCoreApplication.translate("MainWindow", "1 ~ Wavelenght (nm)", None)
        )
        self.cb_calc5_norm.setText(
            QCoreApplication.translate("MainWindow", "Normalize it", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_5),
            QCoreApplication.translate("MainWindow", "Refl. (Final)", None),
        )
        self.cb_export_bayer_as_npy.setText(
            QCoreApplication.translate("MainWindow", "Export (Bayer as NPY)", None)
        )
        self.cb_export_bayer_as_mat.setText(
            QCoreApplication.translate("MainWindow", "Export (Bayer as MAT)", None)
        )
        self.cb_export_ref_CSV_simple.setText(
            QCoreApplication.translate(
                "MainWindow", "Export CSV (only reflection)", None
            )
        )
        self.cb_export_ref_CSV_full.setText(
            QCoreApplication.translate("MainWindow", "Export CSV (FULL)", None)
        )
        self.pb_export.setText(
            QCoreApplication.translate("MainWindow", "Export (Ctrl+E)", None)
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
