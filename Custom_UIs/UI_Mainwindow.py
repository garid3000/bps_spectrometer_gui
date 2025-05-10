# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QFont,
    QPalette,
)
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QCommandLinkButton,
    QDoubleSpinBox,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QSpinBox,
    QSplitter,
    QStatusBar,
    QTabWidget,
    QTextBrowser,
    QTreeView,
    QVBoxLayout,
    QWidget,
)

from pyqtgraph import GraphicsLayoutWidget, ImageView, PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow) -> None:
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(3136, 757)
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
        self.actionSave_geometry_configuration_Ctrl_Shift_L.setObjectName("actionSave_geometry_configuration_Ctrl_Shift_L")
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
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName("label_23")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_23)

        self.clb_0_file2roi_3dist = QCommandLinkButton(self.centralwidget)
        self.clb_0_file2roi_3dist.setObjectName("clb_0_file2roi_3dist")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clb_0_file2roi_3dist.sizePolicy().hasHeightForWidth())
        self.clb_0_file2roi_3dist.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.clb_0_file2roi_3dist)

        self.clb_1_3dist_to_3curv = QCommandLinkButton(self.centralwidget)
        self.clb_1_3dist_to_3curv.setObjectName("clb_1_3dist_to_3curv")
        self.clb_1_3dist_to_3curv.setIconSize(QSize(50, 20))

        self.horizontalLayout_3.addWidget(self.clb_1_3dist_to_3curv)

        self.clb_2_3curv_to_3refl = QCommandLinkButton(self.centralwidget)
        self.clb_2_3curv_to_3refl.setObjectName("clb_2_3curv_to_3refl")

        self.horizontalLayout_3.addWidget(self.clb_2_3curv_to_3refl)

        self.clb_3_3refl_to_1refl = QCommandLinkButton(self.centralwidget)
        self.clb_3_3refl_to_1refl.setObjectName("clb_3_3refl_to_1refl")

        self.horizontalLayout_3.addWidget(self.clb_3_3refl_to_1refl)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.gb_panel_00_file = QGroupBox(self.splitter)
        self.gb_panel_00_file.setObjectName("gb_panel_00_file")
        self.verticalLayout_2 = QVBoxLayout(self.gb_panel_00_file)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb_ft_filter = QCheckBox(self.gb_panel_00_file)
        self.cb_ft_filter.setObjectName("cb_ft_filter")
        self.cb_ft_filter.setChecked(True)
        self.cb_ft_filter.setTristate(False)

        self.verticalLayout_2.addWidget(self.cb_ft_filter)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pb_dir_goto_parent = QPushButton(self.gb_panel_00_file)
        self.pb_dir_goto_parent.setObjectName("pb_dir_goto_parent")

        self.horizontalLayout_4.addWidget(self.pb_dir_goto_parent)

        self.pb_system_file_explorer = QPushButton(self.gb_panel_00_file)
        self.pb_system_file_explorer.setObjectName("pb_system_file_explorer")

        self.horizontalLayout_4.addWidget(self.pb_system_file_explorer)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.tv_dir = QTreeView(self.gb_panel_00_file)
        self.tv_dir.setObjectName("tv_dir")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(10)
        sizePolicy2.setHeightForWidth(self.tv_dir.sizePolicy().hasHeightForWidth())
        self.tv_dir.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies(["Monospace"])
        font.setPointSize(10)
        self.tv_dir.setFont(font)
        self.tv_dir.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.tv_dir)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self._l_14 = QLabel(self.gb_panel_00_file)
        self._l_14.setObjectName("_l_14")

        self.horizontalLayout_5.addWidget(self._l_14)

        self.le_tv_name_narrower = QLineEdit(self.gb_panel_00_file)
        self.le_tv_name_narrower.setObjectName("le_tv_name_narrower")

        self.horizontalLayout_5.addWidget(self.le_tv_name_narrower)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.graph_webcam = ImageView(self.gb_panel_00_file)
        self.graph_webcam.setObjectName("graph_webcam")

        self.verticalLayout_2.addWidget(self.graph_webcam)

        self.tb_meta_json = QLabel(self.gb_panel_00_file)
        self.tb_meta_json.setObjectName("tb_meta_json")

        self.verticalLayout_2.addWidget(self.tb_meta_json)

        self.tabWidget_2 = QTabWidget(self.gb_panel_00_file)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout = QHBoxLayout(self.tab_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l_target_distance = QLabel(self.tab_6)
        self.l_target_distance.setObjectName("l_target_distance")

        self.horizontalLayout.addWidget(self.l_target_distance)

        self.hs_target_distance = QSlider(self.tab_6)
        self.hs_target_distance.setObjectName("hs_target_distance")
        self.hs_target_distance.setMinimum(1)
        self.hs_target_distance.setMaximum(400)
        self.hs_target_distance.setSingleStep(10)
        self.hs_target_distance.setSliderPosition(100)
        self.hs_target_distance.setTickPosition(QSlider.TickPosition.NoTicks)
        self.hs_target_distance.setTickInterval(20)

        self.horizontalLayout.addWidget(self.hs_target_distance)

        _ = self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_3 = QGridLayout(self.tab_7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.l_physical_height = QLabel(self.tab_7)
        self.l_physical_height.setObjectName("l_physical_height")

        self.gridLayout_3.addWidget(self.l_physical_height, 1, 0, 1, 1)

        self.graph_physical_orientation = GraphicsLayoutWidget(self.tab_7)
        self.graph_physical_orientation.setObjectName("graph_physical_orientation")

        self.gridLayout_3.addWidget(self.graph_physical_orientation, 0, 0, 1, 2)

        self.hs_physical_elv = QSlider(self.tab_7)
        self.hs_physical_elv.setObjectName("hs_physical_elv")
        self.hs_physical_elv.setMinimum(-90)
        self.hs_physical_elv.setMaximum(0)
        self.hs_physical_elv.setValue(-45)

        self.gridLayout_3.addWidget(self.hs_physical_elv, 2, 1, 1, 1)

        self.hs_physical_height = QSlider(self.tab_7)
        self.hs_physical_height.setObjectName("hs_physical_height")
        self.hs_physical_height.setMaximum(300)
        self.hs_physical_height.setValue(150)

        self.gridLayout_3.addWidget(self.hs_physical_height, 1, 1, 1, 1)

        self.l_physical_elv = QLabel(self.tab_7)
        self.l_physical_elv.setObjectName("l_physical_elv")

        self.gridLayout_3.addWidget(self.l_physical_elv, 2, 0, 1, 1)

        self.l_physical_distance = QLabel(self.tab_7)
        self.l_physical_distance.setObjectName("l_physical_distance")
        sizePolicy.setHeightForWidth(self.l_physical_distance.sizePolicy().hasHeightForWidth())
        self.l_physical_distance.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.l_physical_distance, 3, 0, 1, 2)

        _ = self.tabWidget_2.addTab(self.tab_7, "")

        self.verticalLayout_2.addWidget(self.tabWidget_2)

        self.splitter.addWidget(self.gb_panel_00_file)
        self.gp_panel_05_jpeg_load = QGroupBox(self.splitter)
        self.gp_panel_05_jpeg_load.setObjectName("gp_panel_05_jpeg_load")
        self.gridLayout_24 = QGridLayout(self.gp_panel_05_jpeg_load)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.pb_loading_file = QCommandLinkButton(self.gp_panel_05_jpeg_load)
        self.pb_loading_file.setObjectName("pb_loading_file")

        self.gridLayout_24.addWidget(self.pb_loading_file, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.pbar_loading_file = QProgressBar(self.gp_panel_05_jpeg_load)
        self.pbar_loading_file.setObjectName("pbar_loading_file")
        self.pbar_loading_file.setValue(24)

        self.gridLayout_24.addWidget(self.pbar_loading_file, 1, 0, 1, 1)

        self.splitter.addWidget(self.gp_panel_05_jpeg_load)
        self.gp_panel_10_rawbayer = QGroupBox(self.splitter)
        self.gp_panel_10_rawbayer.setObjectName("gp_panel_10_rawbayer")
        self.verticalLayout = QVBoxLayout(self.gp_panel_10_rawbayer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QScrollArea(self.gp_panel_10_rawbayer)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 422, 248))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cb_2dimg_key = QComboBox(self.scrollAreaWidgetContents_2)
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.addItem("")
        self.cb_2dimg_key.setObjectName("cb_2dimg_key")

        self.horizontalLayout_2.addWidget(self.cb_2dimg_key)

        self.cb_invert_y_axis_of_rawbayer = QCheckBox(self.scrollAreaWidgetContents_2)
        self.cb_invert_y_axis_of_rawbayer.setObjectName("cb_invert_y_axis_of_rawbayer")
        self.cb_invert_y_axis_of_rawbayer.setChecked(True)

        self.horizontalLayout_2.addWidget(self.cb_invert_y_axis_of_rawbayer)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.graph_2dimg = ImageView(self.scrollAreaWidgetContents_2)
        self.graph_2dimg.setObjectName("graph_2dimg")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(200)
        sizePolicy3.setVerticalStretch(200)
        sizePolicy3.setHeightForWidth(self.graph_2dimg.sizePolicy().hasHeightForWidth())
        self.graph_2dimg.setSizePolicy(sizePolicy3)
        self.graph_2dimg.setMinimumSize(QSize(400, 200))

        self.verticalLayout_4.addWidget(self.graph_2dimg)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea_2)

        self.tw_midcol = QTabWidget(self.gp_panel_10_rawbayer)
        self.tw_midcol.setObjectName("tw_midcol")
        self.midcol_tab1_wave = QWidget()
        self.midcol_tab1_wave.setObjectName("midcol_tab1_wave")
        self.gridLayout_11 = QGridLayout(self.midcol_tab1_wave)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cb_shows_calibrated_wl = QCheckBox(self.midcol_tab1_wave)
        self.cb_shows_calibrated_wl.setObjectName("cb_shows_calibrated_wl")

        self.gridLayout_4.addWidget(self.cb_shows_calibrated_wl, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.midcol_tab1_wave)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 0, 2, 1, 1)

        self.sp_wv_shower = QDoubleSpinBox(self.midcol_tab1_wave)
        self.sp_wv_shower.setObjectName("sp_wv_shower")
        self.sp_wv_shower.setMaximum(1000.000000000000000)
        self.sp_wv_shower.setValue(759.370000000000005)

        self.gridLayout_4.addWidget(self.sp_wv_shower, 0, 1, 1, 1)

        self.gridLayout_11.addLayout(self.gridLayout_4, 4, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cb_759_channel = QComboBox(self.midcol_tab1_wave)
        self.cb_759_channel.addItem("")
        self.cb_759_channel.addItem("")
        self.cb_759_channel.addItem("")
        self.cb_759_channel.addItem("")
        self.cb_759_channel.setObjectName("cb_759_channel")

        self.verticalLayout_3.addWidget(self.cb_759_channel)

        self.label_8 = QLabel(self.midcol_tab1_wave)
        self.label_8.setObjectName("label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.graph_759_roi = ImageView(self.midcol_tab1_wave)
        self.graph_759_roi.setObjectName("graph_759_roi")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.graph_759_roi.sizePolicy().hasHeightForWidth())
        self.graph_759_roi.setSizePolicy(sizePolicy4)
        self.graph_759_roi.setMinimumSize(QSize(1, 1))

        self.verticalLayout_3.addWidget(self.graph_759_roi)

        self.gridLayout_11.addLayout(self.verticalLayout_3, 0, 0, 5, 1)

        self.label_3 = QLabel(self.midcol_tab1_wave)
        self.label_3.setObjectName("label_3")

        self.gridLayout_11.addWidget(self.label_3, 5, 1, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.graph_759_plot_fit = PlotWidget(self.midcol_tab1_wave)
        self.graph_759_plot_fit.setObjectName("graph_759_plot_fit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.graph_759_plot_fit.sizePolicy().hasHeightForWidth())
        self.graph_759_plot_fit.setSizePolicy(sizePolicy5)
        self.graph_759_plot_fit.setMinimumSize(QSize(1, 1))

        self.gridLayout_9.addWidget(self.graph_759_plot_fit, 1, 3, 1, 1)

        self.graph_759_plot = PlotWidget(self.midcol_tab1_wave)
        self.graph_759_plot.setObjectName("graph_759_plot")
        sizePolicy5.setHeightForWidth(self.graph_759_plot.sizePolicy().hasHeightForWidth())
        self.graph_759_plot.setSizePolicy(sizePolicy5)
        self.graph_759_plot.setMinimumSize(QSize(1, 1))

        self.gridLayout_9.addWidget(self.graph_759_plot, 1, 2, 1, 1)

        self.pbar_759_rows = QProgressBar(self.midcol_tab1_wave)
        self.pbar_759_rows.setObjectName("pbar_759_rows")
        self.pbar_759_rows.setValue(24)
        self.pbar_759_rows.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_9.addWidget(self.pbar_759_rows, 1, 1, 1, 1)

        self.gridLayout_11.addLayout(self.gridLayout_9, 3, 1, 1, 1)

        self.pb_wave_calib = QPushButton(self.midcol_tab1_wave)
        self.pb_wave_calib.setObjectName("pb_wave_calib")

        self.gridLayout_11.addWidget(self.pb_wave_calib, 2, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self._l = QLabel(self.midcol_tab1_wave)
        self._l.setObjectName("_l")

        self.gridLayout_8.addWidget(self._l, 0, 0, 1, 1)

        self.sb_waveperpixel = QDoubleSpinBox(self.midcol_tab1_wave)
        self.sb_waveperpixel.setObjectName("sb_waveperpixel")
        self.sb_waveperpixel.setDecimals(4)
        self.sb_waveperpixel.setMinimum(1.500000000000000)
        self.sb_waveperpixel.setMaximum(2.500000000000000)
        self.sb_waveperpixel.setSingleStep(2.000000000000000)
        self.sb_waveperpixel.setValue(1.858300000000000)

        self.gridLayout_8.addWidget(self.sb_waveperpixel, 0, 1, 1, 1)

        self.pb_waveperpixel_reset = QPushButton(self.midcol_tab1_wave)
        self.pb_waveperpixel_reset.setObjectName("pb_waveperpixel_reset")

        self.gridLayout_8.addWidget(self.pb_waveperpixel_reset, 0, 2, 1, 1)

        self.gridLayout_11.addLayout(self.gridLayout_8, 1, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_6 = QLabel(self.midcol_tab1_wave)
        self.label_6.setObjectName("label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_7 = QLabel(self.midcol_tab1_wave)
        self.label_7.setObjectName("label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_4 = QLabel(self.midcol_tab1_wave)
        self.label_4.setObjectName("label_4")

        self.gridLayout_7.addWidget(self.label_4, 1, 0, 1, 1)

        self.sb_roi759_posx = QSpinBox(self.midcol_tab1_wave)
        self.sb_roi759_posx.setObjectName("sb_roi759_posx")
        self.sb_roi759_posx.setMaximum(4000)
        self.sb_roi759_posx.setSingleStep(2)
        self.sb_roi759_posx.setValue(1850)

        self.gridLayout_7.addWidget(self.sb_roi759_posx, 1, 1, 1, 1)

        self.sb_roi759_posy = QSpinBox(self.midcol_tab1_wave)
        self.sb_roi759_posy.setObjectName("sb_roi759_posy")
        self.sb_roi759_posy.setMaximum(4000)
        self.sb_roi759_posy.setSingleStep(2)
        self.sb_roi759_posy.setValue(1156)

        self.gridLayout_7.addWidget(self.sb_roi759_posy, 1, 2, 1, 1)

        self.label_5 = QLabel(self.midcol_tab1_wave)
        self.label_5.setObjectName("label_5")

        self.gridLayout_7.addWidget(self.label_5, 2, 0, 1, 1)

        self.sb_roi759_sizx = QSpinBox(self.midcol_tab1_wave)
        self.sb_roi759_sizx.setObjectName("sb_roi759_sizx")
        self.sb_roi759_sizx.setMaximum(100)
        self.sb_roi759_sizx.setSingleStep(2)
        self.sb_roi759_sizx.setValue(26)

        self.gridLayout_7.addWidget(self.sb_roi759_sizx, 2, 1, 1, 1)

        self.sb_roi759_sizy = QSpinBox(self.midcol_tab1_wave)
        self.sb_roi759_sizy.setObjectName("sb_roi759_sizy")
        self.sb_roi759_sizy.setMaximum(4000)
        self.sb_roi759_sizy.setSingleStep(2)
        self.sb_roi759_sizy.setValue(508)

        self.gridLayout_7.addWidget(self.sb_roi759_sizy, 2, 2, 1, 1)

        self.gridLayout_11.addLayout(self.gridLayout_7, 0, 1, 1, 1)

        _ = self.tw_midcol.addTab(self.midcol_tab1_wave, "")
        self.midcol_tab2_bgnd = QWidget()
        self.midcol_tab2_bgnd.setObjectName("midcol_tab2_bgnd")
        self.gridLayout_13 = QGridLayout(self.midcol_tab2_bgnd)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.tabWidget_3 = QTabWidget(self.midcol_tab2_bgnd)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName("tab_13")
        self.verticalLayout_11 = QVBoxLayout(self.tab_13)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_20 = QLabel(self.tab_13)
        self.label_20.setObjectName("label_20")

        self.gridLayout_12.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_21 = QLabel(self.tab_13)
        self.label_21.setObjectName("label_21")

        self.gridLayout_12.addWidget(self.label_21, 1, 1, 1, 1)

        self.label_22 = QLabel(self.tab_13)
        self.label_22.setObjectName("label_22")

        self.gridLayout_12.addWidget(self.label_22, 1, 2, 1, 1)

        self.graph_bg_r = PlotWidget(self.tab_13)
        self.graph_bg_r.setObjectName("graph_bg_r")
        sizePolicy5.setHeightForWidth(self.graph_bg_r.sizePolicy().hasHeightForWidth())
        self.graph_bg_r.setSizePolicy(sizePolicy5)
        self.graph_bg_r.setMinimumSize(QSize(1, 1))

        self.gridLayout_12.addWidget(self.graph_bg_r, 2, 0, 1, 1)

        self.graph_bg_g = PlotWidget(self.tab_13)
        self.graph_bg_g.setObjectName("graph_bg_g")
        sizePolicy5.setHeightForWidth(self.graph_bg_g.sizePolicy().hasHeightForWidth())
        self.graph_bg_g.setSizePolicy(sizePolicy5)
        self.graph_bg_g.setMinimumSize(QSize(1, 1))

        self.gridLayout_12.addWidget(self.graph_bg_g, 2, 1, 1, 1)

        self.graph_bg_b = PlotWidget(self.tab_13)
        self.graph_bg_b.setObjectName("graph_bg_b")
        sizePolicy5.setHeightForWidth(self.graph_bg_b.sizePolicy().hasHeightForWidth())
        self.graph_bg_b.setSizePolicy(sizePolicy5)
        self.graph_bg_b.setMinimumSize(QSize(1, 1))

        self.gridLayout_12.addWidget(self.graph_bg_b, 2, 2, 1, 1)

        self.verticalLayout_11.addLayout(self.gridLayout_12)

        _ = self.tabWidget_3.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName("tab_14")
        self.gridLayout_16 = QGridLayout(self.tab_14)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.graph_bg_param_c = PlotWidget(self.tab_14)
        self.graph_bg_param_c.setObjectName("graph_bg_param_c")
        sizePolicy5.setHeightForWidth(self.graph_bg_param_c.sizePolicy().hasHeightForWidth())
        self.graph_bg_param_c.setSizePolicy(sizePolicy5)
        self.graph_bg_param_c.setMinimumSize(QSize(1, 1))

        self.gridLayout_15.addWidget(self.graph_bg_param_c, 1, 0, 1, 1)

        self.graph_bg_param_b = PlotWidget(self.tab_14)
        self.graph_bg_param_b.setObjectName("graph_bg_param_b")
        sizePolicy5.setHeightForWidth(self.graph_bg_param_b.sizePolicy().hasHeightForWidth())
        self.graph_bg_param_b.setSizePolicy(sizePolicy5)
        self.graph_bg_param_b.setMinimumSize(QSize(1, 1))

        self.gridLayout_15.addWidget(self.graph_bg_param_b, 0, 0, 1, 1)

        self.graph_bg_param_k = PlotWidget(self.tab_14)
        self.graph_bg_param_k.setObjectName("graph_bg_param_k")
        sizePolicy5.setHeightForWidth(self.graph_bg_param_k.sizePolicy().hasHeightForWidth())
        self.graph_bg_param_k.setSizePolicy(sizePolicy5)
        self.graph_bg_param_k.setMinimumSize(QSize(1, 1))

        self.gridLayout_15.addWidget(self.graph_bg_param_k, 0, 1, 1, 1)

        self.graph_bg_param_a = PlotWidget(self.tab_14)
        self.graph_bg_param_a.setObjectName("graph_bg_param_a")
        sizePolicy5.setHeightForWidth(self.graph_bg_param_a.sizePolicy().hasHeightForWidth())
        self.graph_bg_param_a.setSizePolicy(sizePolicy5)
        self.graph_bg_param_a.setMinimumSize(QSize(1, 1))

        self.gridLayout_15.addWidget(self.graph_bg_param_a, 1, 1, 1, 1)

        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)

        _ = self.tabWidget_3.addTab(self.tab_14, "")

        self.gridLayout_13.addWidget(self.tabWidget_3, 2, 1, 1, 1)

        self.pbar_bg_on_row = QProgressBar(self.midcol_tab2_bgnd)
        self.pbar_bg_on_row.setObjectName("pbar_bg_on_row")
        self.pbar_bg_on_row.setValue(0)
        self.pbar_bg_on_row.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_13.addWidget(self.pbar_bg_on_row, 2, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.sb_bg_0_posx = QSpinBox(self.midcol_tab2_bgnd)
        self.sb_bg_0_posx.setObjectName("sb_bg_0_posx")
        self.sb_bg_0_posx.setMaximum(4000)
        self.sb_bg_0_posx.setSingleStep(2)
        self.sb_bg_0_posx.setValue(1000)

        self.gridLayout_10.addWidget(self.sb_bg_0_posx, 1, 1, 1, 1)

        self.label_12 = QLabel(self.midcol_tab2_bgnd)
        self.label_12.setObjectName("label_12")

        self.gridLayout_10.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_10 = QLabel(self.midcol_tab2_bgnd)
        self.label_10.setObjectName("label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.label_10, 0, 4, 1, 1)

        self.sb_bg_1_sizx = QSpinBox(self.midcol_tab2_bgnd)
        self.sb_bg_1_sizx.setObjectName("sb_bg_1_sizx")
        self.sb_bg_1_sizx.setMaximum(400)
        self.sb_bg_1_sizx.setSingleStep(2)
        self.sb_bg_1_sizx.setValue(300)

        self.gridLayout_10.addWidget(self.sb_bg_1_sizx, 2, 2, 1, 1)

        self.sb_bg_0_sizx = QSpinBox(self.midcol_tab2_bgnd)
        self.sb_bg_0_sizx.setObjectName("sb_bg_0_sizx")
        self.sb_bg_0_sizx.setMaximum(400)
        self.sb_bg_0_sizx.setSingleStep(2)
        self.sb_bg_0_sizx.setValue(300)

        self.gridLayout_10.addWidget(self.sb_bg_0_sizx, 2, 1, 1, 1)

        self.sb_bg___sizy = QSpinBox(self.midcol_tab2_bgnd)
        self.sb_bg___sizy.setObjectName("sb_bg___sizy")
        self.sb_bg___sizy.setMaximum(4000)
        self.sb_bg___sizy.setSingleStep(2)
        self.sb_bg___sizy.setValue(508)

        self.gridLayout_10.addWidget(self.sb_bg___sizy, 2, 4, 1, 1)

        self.sb_bg_1_posx = QSpinBox(self.midcol_tab2_bgnd)
        self.sb_bg_1_posx.setObjectName("sb_bg_1_posx")
        self.sb_bg_1_posx.setMaximum(4000)
        self.sb_bg_1_posx.setSingleStep(2)
        self.sb_bg_1_posx.setValue(2200)

        self.gridLayout_10.addWidget(self.sb_bg_1_posx, 1, 2, 1, 1)

        self.sb_bg___posy = QSpinBox(self.midcol_tab2_bgnd)
        self.sb_bg___posy.setObjectName("sb_bg___posy")
        self.sb_bg___posy.setMaximum(4000)
        self.sb_bg___posy.setSingleStep(2)
        self.sb_bg___posy.setValue(1156)

        self.gridLayout_10.addWidget(self.sb_bg___posy, 1, 4, 1, 1)

        self.label_13 = QLabel(self.midcol_tab2_bgnd)
        self.label_13.setObjectName("label_13")

        self.gridLayout_10.addWidget(self.label_13, 0, 2, 1, 1)

        self.label_9 = QLabel(self.midcol_tab2_bgnd)
        self.label_9.setObjectName("label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.label_9, 0, 1, 1, 1)

        self.label_11 = QLabel(self.midcol_tab2_bgnd)
        self.label_11.setObjectName("label_11")

        self.gridLayout_10.addWidget(self.label_11, 1, 0, 1, 1)

        self.sb_bg_2_posx = QSpinBox(self.midcol_tab2_bgnd)
        self.sb_bg_2_posx.setObjectName("sb_bg_2_posx")
        self.sb_bg_2_posx.setMaximum(4000)
        self.sb_bg_2_posx.setSingleStep(2)
        self.sb_bg_2_posx.setValue(2200)

        self.gridLayout_10.addWidget(self.sb_bg_2_posx, 1, 3, 1, 1)

        self.sb_bg_2_sizx = QSpinBox(self.midcol_tab2_bgnd)
        self.sb_bg_2_sizx.setObjectName("sb_bg_2_sizx")
        self.sb_bg_2_sizx.setMaximum(400)
        self.sb_bg_2_sizx.setSingleStep(2)
        self.sb_bg_2_sizx.setValue(300)

        self.gridLayout_10.addWidget(self.sb_bg_2_sizx, 2, 3, 1, 1)

        self.label_29 = QLabel(self.midcol_tab2_bgnd)
        self.label_29.setObjectName("label_29")

        self.gridLayout_10.addWidget(self.label_29, 0, 3, 1, 1)

        self.gridLayout_13.addLayout(self.gridLayout_10, 0, 1, 1, 1)

        self.pb_bg_calc = QPushButton(self.midcol_tab2_bgnd)
        self.pb_bg_calc.setObjectName("pb_bg_calc")

        self.gridLayout_13.addWidget(self.pb_bg_calc, 1, 1, 1, 1)

        _ = self.tw_midcol.addTab(self.midcol_tab2_bgnd, "")
        self.midcol_tab3_rois = QWidget()
        self.midcol_tab3_rois.setObjectName("midcol_tab3_rois")
        self.gridLayout_6 = QGridLayout(self.midcol_tab3_rois)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.graph_raw = PlotWidget(self.midcol_tab3_rois)
        self.graph_raw.setObjectName("graph_raw")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(200)
        sizePolicy6.setHeightForWidth(self.graph_raw.sizePolicy().hasHeightForWidth())
        self.graph_raw.setSizePolicy(sizePolicy6)
        self.graph_raw.setMinimumSize(QSize(400, 200))

        self.gridLayout_6.addWidget(self.graph_raw, 0, 0, 1, 1)

        self.gb_control_panel = QGroupBox(self.midcol_tab3_rois)
        self.gb_control_panel.setObjectName("gb_control_panel")
        self.gridLayout_2 = QGridLayout(self.gb_control_panel)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self._l_1 = QLabel(self.gb_control_panel)
        self._l_1.setObjectName("_l_1")
        sizePolicy.setHeightForWidth(self._l_1.sizePolicy().hasHeightForWidth())
        self._l_1.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(190, 190, 190, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self._l_1.setPalette(palette)

        self.gridLayout_2.addWidget(self._l_1, 2, 0, 1, 1)

        self.sb_midx_size = QSpinBox(self.gb_control_panel)
        self.sb_midx_size.setObjectName("sb_midx_size")
        self.sb_midx_size.setEnabled(False)
        self.sb_midx_size.setMaximum(9999)
        self.sb_midx_size.setValue(700)

        self.gridLayout_2.addWidget(self.sb_midx_size, 2, 2, 1, 1)

        self._line = QFrame(self.gb_control_panel)
        self._line.setObjectName("_line")
        self._line.setFrameShape(QFrame.Shape.VLine)
        self._line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self._line, 3, 0, 1, 3)

        self.sb_obje_posy = QSpinBox(self.gb_control_panel)
        self.sb_obje_posy.setObjectName("sb_obje_posy")
        self.sb_obje_posy.setMinimum(0)
        self.sb_obje_posy.setMaximum(20000)
        self.sb_obje_posy.setSingleStep(2)
        self.sb_obje_posy.setValue(1200)

        self.gridLayout_2.addWidget(self.sb_obje_posy, 8, 1, 1, 1)

        self.sb_obje_sizy = QSpinBox(self.gb_control_panel)
        self.sb_obje_sizy.setObjectName("sb_obje_sizy")
        self.sb_obje_sizy.setMinimum(0)
        self.sb_obje_sizy.setMaximum(20000)
        self.sb_obje_sizy.setSingleStep(2)
        self.sb_obje_sizy.setValue(50)

        self.gridLayout_2.addWidget(self.sb_obje_sizy, 8, 2, 1, 1)

        self.sb_gray_posy = QSpinBox(self.gb_control_panel)
        self.sb_gray_posy.setObjectName("sb_gray_posy")
        self.sb_gray_posy.setMinimum(0)
        self.sb_gray_posy.setMaximum(20000)
        self.sb_gray_posy.setSingleStep(2)
        self.sb_gray_posy.setValue(1050)

        self.gridLayout_2.addWidget(self.sb_gray_posy, 5, 1, 1, 1)

        self.sb_gray_sizy = QSpinBox(self.gb_control_panel)
        self.sb_gray_sizy.setObjectName("sb_gray_sizy")
        self.sb_gray_sizy.setMinimum(0)
        self.sb_gray_sizy.setMaximum(20000)
        self.sb_gray_sizy.setSingleStep(2)
        self.sb_gray_sizy.setValue(50)

        self.gridLayout_2.addWidget(self.sb_gray_sizy, 5, 2, 1, 1)

        self._l_11 = QLabel(self.gb_control_panel)
        self._l_11.setObjectName("_l_11")
        sizePolicy.setHeightForWidth(self._l_11.sizePolicy().hasHeightForWidth())
        self._l_11.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self._l_11, 4, 1, 1, 1)

        self._l_3 = QLabel(self.gb_control_panel)
        self._l_3.setObjectName("_l_3")
        palette1 = QPalette()
        brush2 = QBrush(QColor(0, 0, 255, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self._l_3.setPalette(palette1)

        self.gridLayout_2.addWidget(self._l_3, 8, 0, 1, 1)

        self._l_8 = QLabel(self.gb_control_panel)
        self._l_8.setObjectName("_l_8")
        sizePolicy.setHeightForWidth(self._l_8.sizePolicy().hasHeightForWidth())
        self._l_8.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self._l_8, 1, 1, 1, 1)

        self._l_2 = QLabel(self.gb_control_panel)
        self._l_2.setObjectName("_l_2")
        palette2 = QPalette()
        brush3 = QBrush(QColor(255, 0, 0, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush3)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush3)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        self._l_2.setPalette(palette2)

        self.gridLayout_2.addWidget(self._l_2, 5, 0, 1, 1)

        self.line_3 = QFrame(self.gb_control_panel)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 9, 0, 1, 3)

        self._l_4 = QLabel(self.gb_control_panel)
        self._l_4.setObjectName("_l_4")
        sizePolicy.setHeightForWidth(self._l_4.sizePolicy().hasHeightForWidth())
        self._l_4.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self._l_4, 4, 2, 1, 1)

        self._l_9 = QLabel(self.gb_control_panel)
        self._l_9.setObjectName("_l_9")
        sizePolicy.setHeightForWidth(self._l_9.sizePolicy().hasHeightForWidth())
        self._l_9.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self._l_9, 1, 2, 1, 1)

        self.sb_midx_init = QSpinBox(self.gb_control_panel)
        self.sb_midx_init.setObjectName("sb_midx_init")
        self.sb_midx_init.setMinimum(0)
        self.sb_midx_init.setMaximum(17000)
        self.sb_midx_init.setSingleStep(2)
        self.sb_midx_init.setValue(1350)

        self.gridLayout_2.addWidget(self.sb_midx_init, 2, 1, 1, 1)

        self.gridLayout_6.addWidget(self.gb_control_panel, 1, 0, 1, 1)

        _ = self.tw_midcol.addTab(self.midcol_tab3_rois, "")

        self.verticalLayout.addWidget(self.tw_midcol)

        self.splitter.addWidget(self.gp_panel_10_rawbayer)
        self.gp_panel_15_roiselect = QGroupBox(self.splitter)
        self.gp_panel_15_roiselect.setObjectName("gp_panel_15_roiselect")
        self.gridLayout_23 = QGridLayout(self.gp_panel_15_roiselect)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.pb_select_gray_roi = QCommandLinkButton(self.gp_panel_15_roiselect)
        self.pb_select_gray_roi.setObjectName("pb_select_gray_roi")

        self.gridLayout_23.addWidget(self.pb_select_gray_roi, 1, 0, 1, 1)

        self.pb_select_obje_roi = QCommandLinkButton(self.gp_panel_15_roiselect)
        self.pb_select_obje_roi.setObjectName("pb_select_obje_roi")

        self.gridLayout_23.addWidget(self.pb_select_obje_roi, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.splitter.addWidget(self.gp_panel_15_roiselect)
        self.gp_panel_20_3roi_dist = QGroupBox(self.splitter)
        self.gp_panel_20_3roi_dist.setObjectName("gp_panel_20_3roi_dist")
        self.gridLayout_21 = QGridLayout(self.gp_panel_20_3roi_dist)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.graph_gray_roi_spectra = PlotWidget(self.gp_panel_20_3roi_dist)
        self.graph_gray_roi_spectra.setObjectName("graph_gray_roi_spectra")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(200)
        sizePolicy7.setHeightForWidth(self.graph_gray_roi_spectra.sizePolicy().hasHeightForWidth())
        self.graph_gray_roi_spectra.setSizePolicy(sizePolicy7)
        self.graph_gray_roi_spectra.setMinimumSize(QSize(300, 200))

        self.gridLayout_17.addWidget(self.graph_gray_roi_spectra, 3, 0, 1, 1)

        self.graph_obje_roi_spectra = PlotWidget(self.gp_panel_20_3roi_dist)
        self.graph_obje_roi_spectra.setObjectName("graph_obje_roi_spectra")
        sizePolicy7.setHeightForWidth(self.graph_obje_roi_spectra.sizePolicy().hasHeightForWidth())
        self.graph_obje_roi_spectra.setSizePolicy(sizePolicy7)
        self.graph_obje_roi_spectra.setMinimumSize(QSize(300, 200))

        self.gridLayout_17.addWidget(self.graph_obje_roi_spectra, 1, 0, 1, 1)

        self.gridLayout_21.addLayout(self.gridLayout_17, 1, 0, 1, 1)

        self.splitter.addWidget(self.gp_panel_20_3roi_dist)
        self.gp_panel_25_savgol = QGroupBox(self.splitter)
        self.gp_panel_25_savgol.setObjectName("gp_panel_25_savgol")
        self.gridLayout_20 = QGridLayout(self.gp_panel_25_savgol)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_8, 0, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_15 = QLabel(self.gp_panel_25_savgol)
        self.label_15.setObjectName("label_15")

        self.gridLayout_18.addWidget(self.label_15, 5, 0, 1, 1)

        self.sb_savgol_poly_degree = QSpinBox(self.gp_panel_25_savgol)
        self.sb_savgol_poly_degree.setObjectName("sb_savgol_poly_degree")
        self.sb_savgol_poly_degree.setValue(5)

        self.gridLayout_18.addWidget(self.sb_savgol_poly_degree, 4, 1, 1, 1)

        self.pbar_savgol_channel = QProgressBar(self.gp_panel_25_savgol)
        self.pbar_savgol_channel.setObjectName("pbar_savgol_channel")
        self.pbar_savgol_channel.setValue(0)

        self.gridLayout_18.addWidget(self.pbar_savgol_channel, 6, 1, 1, 1)

        self.pbar_savgol_iteration = QProgressBar(self.gp_panel_25_savgol)
        self.pbar_savgol_iteration.setObjectName("pbar_savgol_iteration")
        self.pbar_savgol_iteration.setValue(0)

        self.gridLayout_18.addWidget(self.pbar_savgol_iteration, 7, 1, 1, 1)

        self.label_14 = QLabel(self.gp_panel_25_savgol)
        self.label_14.setObjectName("label_14")

        self.gridLayout_18.addWidget(self.label_14, 4, 0, 1, 1)

        self.sb_savgol_wv0 = QDoubleSpinBox(self.gp_panel_25_savgol)
        self.sb_savgol_wv0.setObjectName("sb_savgol_wv0")
        self.sb_savgol_wv0.setMinimum(200.000000000000000)
        self.sb_savgol_wv0.setMaximum(2000.000000000000000)
        self.sb_savgol_wv0.setValue(400.000000000000000)

        self.gridLayout_18.addWidget(self.sb_savgol_wv0, 0, 1, 1, 1)

        self.sb_savgol_poly_wv_window = QDoubleSpinBox(self.gp_panel_25_savgol)
        self.sb_savgol_poly_wv_window.setObjectName("sb_savgol_poly_wv_window")
        self.sb_savgol_poly_wv_window.setValue(10.000000000000000)

        self.gridLayout_18.addWidget(self.sb_savgol_poly_wv_window, 5, 1, 1, 1)

        self.sb_savgol_wv1 = QDoubleSpinBox(self.gp_panel_25_savgol)
        self.sb_savgol_wv1.setObjectName("sb_savgol_wv1")
        self.sb_savgol_wv1.setMinimum(200.000000000000000)
        self.sb_savgol_wv1.setMaximum(2000.000000000000000)
        self.sb_savgol_wv1.setValue(900.000000000000000)

        self.gridLayout_18.addWidget(self.sb_savgol_wv1, 1, 1, 1, 1)

        self.sb_savgol_wv_num = QSpinBox(self.gp_panel_25_savgol)
        self.sb_savgol_wv_num.setObjectName("sb_savgol_wv_num")
        self.sb_savgol_wv_num.setMaximum(2000)
        self.sb_savgol_wv_num.setValue(1001)

        self.gridLayout_18.addWidget(self.sb_savgol_wv_num, 3, 1, 1, 1)

        self.label_17 = QLabel(self.gp_panel_25_savgol)
        self.label_17.setObjectName("label_17")

        self.gridLayout_18.addWidget(self.label_17, 3, 0, 1, 1)

        self.label_18 = QLabel(self.gp_panel_25_savgol)
        self.label_18.setObjectName("label_18")

        self.gridLayout_18.addWidget(self.label_18, 2, 0, 1, 1)

        self.label_19 = QLabel(self.gp_panel_25_savgol)
        self.label_19.setObjectName("label_19")

        self.gridLayout_18.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_16 = QLabel(self.gp_panel_25_savgol)
        self.label_16.setObjectName("label_16")

        self.gridLayout_18.addWidget(self.label_16, 0, 0, 1, 1)

        self.sb_savgol_wv_step = QDoubleSpinBox(self.gp_panel_25_savgol)
        self.sb_savgol_wv_step.setObjectName("sb_savgol_wv_step")
        self.sb_savgol_wv_step.setMaximum(100.000000000000000)
        self.sb_savgol_wv_step.setSingleStep(0.100000000000000)
        self.sb_savgol_wv_step.setValue(0.500000000000000)

        self.gridLayout_18.addWidget(self.sb_savgol_wv_step, 2, 1, 1, 1)

        self.pb_savgol_calc = QCommandLinkButton(self.gp_panel_25_savgol)
        self.pb_savgol_calc.setObjectName("pb_savgol_calc")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pb_savgol_calc.sizePolicy().hasHeightForWidth())
        self.pb_savgol_calc.setSizePolicy(sizePolicy8)

        self.gridLayout_18.addWidget(self.pb_savgol_calc, 6, 0, 2, 1)

        self.gridLayout_20.addLayout(self.gridLayout_18, 1, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_9, 2, 0, 1, 1)

        self.splitter.addWidget(self.gp_panel_25_savgol)
        self.gp_panel_30_rgb_curves = QGroupBox(self.splitter)
        self.gp_panel_30_rgb_curves.setObjectName("gp_panel_30_rgb_curves")
        self.verticalLayout_7 = QVBoxLayout(self.gp_panel_30_rgb_curves)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.graph_obje_curve_rgb = PlotWidget(self.gp_panel_30_rgb_curves)
        self.graph_obje_curve_rgb.setObjectName("graph_obje_curve_rgb")
        sizePolicy7.setHeightForWidth(self.graph_obje_curve_rgb.sizePolicy().hasHeightForWidth())
        self.graph_obje_curve_rgb.setSizePolicy(sizePolicy7)
        self.graph_obje_curve_rgb.setMinimumSize(QSize(300, 200))

        self.verticalLayout_7.addWidget(self.graph_obje_curve_rgb)

        self.graph_gray_curve_rgb = PlotWidget(self.gp_panel_30_rgb_curves)
        self.graph_gray_curve_rgb.setObjectName("graph_gray_curve_rgb")
        sizePolicy7.setHeightForWidth(self.graph_gray_curve_rgb.sizePolicy().hasHeightForWidth())
        self.graph_gray_curve_rgb.setSizePolicy(sizePolicy7)
        self.graph_gray_curve_rgb.setMinimumSize(QSize(300, 200))

        self.verticalLayout_7.addWidget(self.graph_gray_curve_rgb)

        self.graph_refl_curve_rgb = PlotWidget(self.gp_panel_30_rgb_curves)
        self.graph_refl_curve_rgb.setObjectName("graph_refl_curve_rgb")
        sizePolicy7.setHeightForWidth(self.graph_refl_curve_rgb.sizePolicy().hasHeightForWidth())
        self.graph_refl_curve_rgb.setSizePolicy(sizePolicy7)
        self.graph_refl_curve_rgb.setMinimumSize(QSize(300, 200))

        self.verticalLayout_7.addWidget(self.graph_refl_curve_rgb)

        self.splitter.addWidget(self.gp_panel_30_rgb_curves)
        self.gp_panel_35_refl_calculate = QGroupBox(self.splitter)
        self.gp_panel_35_refl_calculate.setObjectName("gp_panel_35_refl_calculate")
        self.verticalLayout_6 = QVBoxLayout(self.gp_panel_35_refl_calculate)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.graph_3to1_weight = PlotWidget(self.gp_panel_35_refl_calculate)
        self.graph_3to1_weight.setObjectName("graph_3to1_weight")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(200)
        sizePolicy9.setHeightForWidth(self.graph_3to1_weight.sizePolicy().hasHeightForWidth())
        self.graph_3to1_weight.setSizePolicy(sizePolicy9)
        self.graph_3to1_weight.setMinimumSize(QSize(50, 50))

        self.verticalLayout_6.addWidget(self.graph_3to1_weight)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.sb_3to1_a1 = QDoubleSpinBox(self.gp_panel_35_refl_calculate)
        self.sb_3to1_a1.setObjectName("sb_3to1_a1")
        self.sb_3to1_a1.setMaximum(999.899999999999977)
        self.sb_3to1_a1.setSingleStep(0.050000000000000)
        self.sb_3to1_a1.setValue(1.000000000000000)

        self.gridLayout_19.addWidget(self.sb_3to1_a1, 1, 3, 1, 1)

        self.label = QLabel(self.gp_panel_35_refl_calculate)
        self.label.setObjectName("label")

        self.gridLayout_19.addWidget(self.label, 1, 0, 1, 1)

        self.sb_3to1_a3 = QDoubleSpinBox(self.gp_panel_35_refl_calculate)
        self.sb_3to1_a3.setObjectName("sb_3to1_a3")
        self.sb_3to1_a3.setMaximum(999.899999999999977)
        self.sb_3to1_a3.setSingleStep(0.050000000000000)
        self.sb_3to1_a3.setValue(1.000000000000000)

        self.gridLayout_19.addWidget(self.sb_3to1_a3, 3, 3, 1, 1)

        self.sb_3to1_w1 = QDoubleSpinBox(self.gp_panel_35_refl_calculate)
        self.sb_3to1_w1.setObjectName("sb_3to1_w1")
        self.sb_3to1_w1.setMinimum(200.000000000000000)
        self.sb_3to1_w1.setMaximum(1000.000000000000000)
        self.sb_3to1_w1.setValue(500.000000000000000)

        self.gridLayout_19.addWidget(self.sb_3to1_w1, 1, 1, 1, 1)

        self.sb_3to1_a2 = QDoubleSpinBox(self.gp_panel_35_refl_calculate)
        self.sb_3to1_a2.setObjectName("sb_3to1_a2")
        self.sb_3to1_a2.setMaximum(999.899999999999977)
        self.sb_3to1_a2.setSingleStep(0.050000000000000)
        self.sb_3to1_a2.setValue(1.000000000000000)

        self.gridLayout_19.addWidget(self.sb_3to1_a2, 2, 3, 1, 1)

        self.sb_3to1_w2 = QDoubleSpinBox(self.gp_panel_35_refl_calculate)
        self.sb_3to1_w2.setObjectName("sb_3to1_w2")
        self.sb_3to1_w2.setMinimum(200.000000000000000)
        self.sb_3to1_w2.setMaximum(1000.000000000000000)
        self.sb_3to1_w2.setValue(612.000000000000000)

        self.gridLayout_19.addWidget(self.sb_3to1_w2, 2, 1, 1, 1)

        self.label_24 = QLabel(self.gp_panel_35_refl_calculate)
        self.label_24.setObjectName("label_24")

        self.gridLayout_19.addWidget(self.label_24, 2, 0, 1, 1)

        self.label_26 = QLabel(self.gp_panel_35_refl_calculate)
        self.label_26.setObjectName("label_26")

        self.gridLayout_19.addWidget(self.label_26, 1, 2, 1, 1)

        self.label_25 = QLabel(self.gp_panel_35_refl_calculate)
        self.label_25.setObjectName("label_25")

        self.gridLayout_19.addWidget(self.label_25, 3, 0, 1, 1)

        self.sb_3to1_w3 = QDoubleSpinBox(self.gp_panel_35_refl_calculate)
        self.sb_3to1_w3.setObjectName("sb_3to1_w3")
        self.sb_3to1_w3.setMinimum(200.000000000000000)
        self.sb_3to1_w3.setMaximum(1000.000000000000000)
        self.sb_3to1_w3.setValue(800.000000000000000)

        self.gridLayout_19.addWidget(self.sb_3to1_w3, 3, 1, 1, 1)

        self.label_27 = QLabel(self.gp_panel_35_refl_calculate)
        self.label_27.setObjectName("label_27")

        self.gridLayout_19.addWidget(self.label_27, 2, 2, 1, 1)

        self.label_28 = QLabel(self.gp_panel_35_refl_calculate)
        self.label_28.setObjectName("label_28")

        self.gridLayout_19.addWidget(self.label_28, 3, 2, 1, 1)

        self.verticalLayout_6.addLayout(self.gridLayout_19)

        self.pb_select_obje_roi_3 = QPushButton(self.gp_panel_35_refl_calculate)
        self.pb_select_obje_roi_3.setObjectName("pb_select_obje_roi_3")

        self.verticalLayout_6.addWidget(self.pb_select_obje_roi_3)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)

        self.splitter.addWidget(self.gp_panel_35_refl_calculate)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.graph_refl_curve_weighted = PlotWidget(self.groupBox)
        self.graph_refl_curve_weighted.setObjectName("graph_refl_curve_weighted")
        sizePolicy7.setHeightForWidth(self.graph_refl_curve_weighted.sizePolicy().hasHeightForWidth())
        self.graph_refl_curve_weighted.setSizePolicy(sizePolicy7)
        self.graph_refl_curve_weighted.setMinimumSize(QSize(300, 200))

        self.verticalLayout_10.addWidget(self.graph_refl_curve_weighted)

        self.splitter.addWidget(self.groupBox)
        self.gp_panel_40_3refl_to_1refl = QGroupBox(self.splitter)
        self.gp_panel_40_3refl_to_1refl.setObjectName("gp_panel_40_3refl_to_1refl")
        self.formLayout = QFormLayout(self.gp_panel_40_3refl_to_1refl)
        self.formLayout.setObjectName("formLayout")
        self.pb_calibrate_calculate = QPushButton(self.gp_panel_40_3refl_to_1refl)
        self.pb_calibrate_calculate.setObjectName("pb_calibrate_calculate")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.pb_calibrate_calculate.sizePolicy().hasHeightForWidth())
        self.pb_calibrate_calculate.setSizePolicy(sizePolicy10)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pb_calibrate_calculate)

        self.pbar_calc = QProgressBar(self.gp_panel_40_3refl_to_1refl)
        self.pbar_calc.setObjectName("pbar_calc")
        self.pbar_calc.setMaximum(100)
        self.pbar_calc.setValue(0)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.pbar_calc)

        self.scrollArea = QScrollArea(self.gp_panel_40_3refl_to_1refl)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 340, 525))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_5 = QGridLayout(self.tab_8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.graph_gray2white = PlotWidget(self.tab_8)
        self.graph_gray2white.setObjectName("graph_gray2white")

        self.gridLayout_5.addWidget(self.graph_gray2white, 0, 0, 1, 1)

        _ = self.tabWidget.addTab(self.tab_8, "")
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

        _ = self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.formLayout_2 = QFormLayout(self.tab_5)
        self.formLayout_2.setObjectName("formLayout_2")
        self._l_12 = QLabel(self.tab_5)
        self._l_12.setObjectName("_l_12")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self._l_12)

        self.sb_calc5_norm_zero = QDoubleSpinBox(self.tab_5)
        self.sb_calc5_norm_zero.setObjectName("sb_calc5_norm_zero")
        self.sb_calc5_norm_zero.setEnabled(False)
        self.sb_calc5_norm_zero.setDecimals(1)
        self.sb_calc5_norm_zero.setMinimum(400.000000000000000)
        self.sb_calc5_norm_zero.setMaximum(900.000000000000000)
        self.sb_calc5_norm_zero.setSingleStep(0.500000000000000)
        self.sb_calc5_norm_zero.setValue(440.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.sb_calc5_norm_zero)

        self.sb_calc5_norm_one = QDoubleSpinBox(self.tab_5)
        self.sb_calc5_norm_one.setObjectName("sb_calc5_norm_one")
        self.sb_calc5_norm_one.setEnabled(False)
        self.sb_calc5_norm_one.setDecimals(1)
        self.sb_calc5_norm_one.setMinimum(400.000000000000000)
        self.sb_calc5_norm_one.setMaximum(900.000000000000000)
        self.sb_calc5_norm_one.setSingleStep(0.500000000000000)
        self.sb_calc5_norm_one.setValue(760.000000000000000)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.sb_calc5_norm_one)

        self.graph_calc5_refl_final = PlotWidget(self.tab_5)
        self.graph_calc5_refl_final.setObjectName("graph_calc5_refl_final")
        self.graph_calc5_refl_final.setMinimumSize(QSize(300, 300))

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.graph_calc5_refl_final)

        self._l_13 = QLabel(self.tab_5)
        self._l_13.setObjectName("_l_13")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self._l_13)

        self.cb_calc5_norm = QCheckBox(self.tab_5)
        self.cb_calc5_norm.setObjectName("cb_calc5_norm")
        self.cb_calc5_norm.setChecked(False)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.cb_calc5_norm)

        self.txt_calc5_refl_final = QTextBrowser(self.tab_5)
        self.txt_calc5_refl_final.setObjectName("txt_calc5_refl_final")
        self.txt_calc5_refl_final.setMaximumSize(QSize(16777215, 80))

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.txt_calc5_refl_final)

        _ = self.tabWidget.addTab(self.tab_5, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.scrollArea)

        self.cb_export_bayer_as_npy = QCheckBox(self.gp_panel_40_3refl_to_1refl)
        self.cb_export_bayer_as_npy.setObjectName("cb_export_bayer_as_npy")
        self.cb_export_bayer_as_npy.setEnabled(True)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.cb_export_bayer_as_npy)

        self.cb_export_bayer_as_mat = QCheckBox(self.gp_panel_40_3refl_to_1refl)
        self.cb_export_bayer_as_mat.setObjectName("cb_export_bayer_as_mat")
        self.cb_export_bayer_as_mat.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cb_export_bayer_as_mat)

        self.cb_export_ref_CSV_simple = QCheckBox(self.gp_panel_40_3refl_to_1refl)
        self.cb_export_ref_CSV_simple.setObjectName("cb_export_ref_CSV_simple")
        self.cb_export_ref_CSV_simple.setChecked(True)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.cb_export_ref_CSV_simple)

        self.cb_export_ref_CSV_full = QCheckBox(self.gp_panel_40_3refl_to_1refl)
        self.cb_export_ref_CSV_full.setObjectName("cb_export_ref_CSV_full")
        self.cb_export_ref_CSV_full.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cb_export_ref_CSV_full)

        self.pb_export = QPushButton(self.gp_panel_40_3refl_to_1refl)
        self.pb_export.setObjectName("pb_export")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.pb_export)

        self.pbar_export = QProgressBar(self.gp_panel_40_3refl_to_1refl)
        self.pbar_export.setObjectName("pbar_export")
        self.pbar_export.setValue(0)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.pbar_export)

        self.label_2 = QLabel(self.gp_panel_40_3refl_to_1refl)
        self.label_2.setObjectName("label_2")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.cb_parameter_history = QComboBox(self.gp_panel_40_3refl_to_1refl)
        self.cb_parameter_history.setObjectName("cb_parameter_history")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.cb_parameter_history)

        self.line_2 = QFrame(self.gp_panel_40_3refl_to_1refl)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.SpanningRole, self.line_2)

        self.spinBox = QSpinBox(self.gp_panel_40_3refl_to_1refl)
        self.spinBox.setObjectName("spinBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.spinBox)

        self.splitter.addWidget(self.gp_panel_40_3refl_to_1refl)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.splitter.addWidget(self.groupBox_2)

        self.verticalLayout_5.addWidget(self.splitter)

        self.verticalLayout_5.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 3136, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDirectory_operations = QMenu(self.menuFile)
        self.menuDirectory_operations.setObjectName("menuDirectory_operations")
        self.menuType_Here = QMenu(self.menuFile)
        self.menuType_Here.setObjectName("menuType_Here")
        self.menuFile_Operations_on_selected_file = QMenu(self.menuFile)
        self.menuFile_Operations_on_selected_file.setObjectName("menuFile_Operations_on_selected_file")
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
        self.menuFile_Operations_on_selected_file.addAction(self.action_cur_jpeg_preview)
        self.menuFile_Operations_on_selected_file.addAction(self.action_cur_jpeg_export)
        self.menuFile_Operations_on_selected_file.addAction(self.action_cur_file_open)
        self.menuGeometry_Settings.addAction(self.action_geometry_load)
        self.menuGeometry_Settings.addAction(self.actionSave_geometry_configuration_Ctrl_Shift_L)
        _ = self.menuTutorial.addSeparator()
        self.menuTutorial.addAction(self.action_help)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(0)
        self.tw_midcol.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow: QMainWindow) -> None:
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.actionOpen_Directory.setText(QCoreApplication.translate("MainWindow", "Open Directory", None))
        self.action_cur_jpeg_export.setText(QCoreApplication.translate("MainWindow", "Export (Ctlr-E)", None))
        self.action_geometry_load.setText(QCoreApplication.translate("MainWindow", "Load geometry configuration (Ctrl + L)", None))
        self.action_help.setText(QCoreApplication.translate("MainWindow", "Help (Ctrl+H)", None))
        self.actionRead_Dependencies.setText(QCoreApplication.translate("MainWindow", "Read Dependencies", None))
        self.actionContact_information.setText(QCoreApplication.translate("MainWindow", "Contact information", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", "About (Ctrl+A)", None))
        self.actionContact.setText(QCoreApplication.translate("MainWindow", "Contact", None))
        self.action_cur_jpeg_preview.setText(QCoreApplication.translate("MainWindow", "Preview (Space)", None))
        self.action_dir_goto_parent.setText(QCoreApplication.translate("MainWindow", "Go to Parent Directory (Backspace)", None))
        self.action_dir_goto_cur_child.setText(QCoreApplication.translate("MainWindow", "Go inside Selected Directory (Enter)", None))
        self.action_dir_cur_child_fold.setText(QCoreApplication.translate("MainWindow", "Fold Selected Directory (Left Arrow)", None))
        self.action_dir_cur_child_unfold.setText(QCoreApplication.translate("MainWindow", "Unfold Selected Directory (Right Arrow)", None))
        self.action_cur_file_open.setText(QCoreApplication.translate("MainWindow", "Open with an external app (Ctrl+O)", None))
        self.actionsdf.setText(QCoreApplication.translate("MainWindow", "sdf", None))
        self.actionSave_geometry_configuration_Ctrl_Shift_L.setText(QCoreApplication.translate("MainWindow", "Save geometry configuration (Ctrl + Shift + L)", None))
        self.action_dir_ft_filter_toggle.setText(QCoreApplication.translate("MainWindow", "File type filter toggle (Ctrl+F)", None))
        self.action_tabs_show_tab1.setText(QCoreApplication.translate("MainWindow", "Raw Bayer Tab (Ctrl+1) or (Alt+1)", None))
        self.action_tabs_show_tab2.setText(QCoreApplication.translate("MainWindow", "Spectrum-Raw Tab (Ctrl+2) or (Alt+2)", None))
        self.action_tabs_show_tab3.setText(QCoreApplication.translate("MainWindow", "Spectrum-Reflectance Tab (Ctrl+3) or (Alt+3)", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", "Stages", None))
        self.clb_0_file2roi_3dist.setText(QCoreApplication.translate("MainWindow", "1. FIle and ROI selection", None))
        self.clb_1_3dist_to_3curv.setText(QCoreApplication.translate("MainWindow", "2. Spectral Curves creation", None))
        self.clb_2_3curv_to_3refl.setText(QCoreApplication.translate("MainWindow", "3. Refl calculation", None))
        self.clb_3_3refl_to_1refl.setText(QCoreApplication.translate("MainWindow", "Joining 3 curves", None))
        self.gb_panel_00_file.setTitle(QCoreApplication.translate("MainWindow", "GroupBox", None))
        # if QT_CONFIG(tooltip)
        self.cb_ft_filter.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Visually filter files by extension. (e.g. JPEG etc)<br/>Useful for <span style=" text-decoration: underline;">identifying</span> the <span style=" text-decoration: underline;">spectral image</span>.</p><p>- JPEG<br/>- JPEG + JPG + JSON<br/>- All</p><p>-------------------------------------------------------------------------<br/>Keyboard shortcut = (CTRL + F)</p><p><br/></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.cb_ft_filter.setWhatsThis(QCoreApplication.translate("MainWindow", "<html><head/><body><p>this is what is this?</p></body></html>", None))
        # endif // QT_CONFIG(whatsthis)
        self.cb_ft_filter.setText(QCoreApplication.translate("MainWindow", "Filter File Type (Ctrl+F)", None))
        # if QT_CONFIG(tooltip)
        self.pb_dir_goto_parent.setToolTip(QCoreApplication.translate("MainWindow", "<html><head/><body><p>Go to parent folder</p></body></html>", None))
        # endif // QT_CONFIG(tooltip)
        self.pb_dir_goto_parent.setText(QCoreApplication.translate("MainWindow", "Go to parent (Backspace)", None))
        self.pb_system_file_explorer.setText(QCoreApplication.translate("MainWindow", "Open Sys. file-explorer", None))
        # if QT_CONFIG(tooltip)
        self._l_14.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>- Narrows file/directory names by given &quot;string&quot;.</p><p>- Helpful when you have too many files/directories</p><p><br/></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self._l_14.setText(QCoreApplication.translate("MainWindow", "Narrow by name (Alf+f)", None))
        self.tb_meta_json.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.l_target_distance.setText(QCoreApplication.translate("MainWindow", "Distance:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", "Tab 1", None))
        self.l_physical_height.setText(QCoreApplication.translate("MainWindow", "Height: ", None))
        self.l_physical_elv.setText(QCoreApplication.translate("MainWindow", "Pitch:", None))
        self.l_physical_distance.setText(QCoreApplication.translate("MainWindow", "Distance:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", "Tab 2", None))
        self.gp_panel_05_jpeg_load.setTitle(QCoreApplication.translate("MainWindow", "GroupBox", None))
        self.pb_loading_file.setText(QCoreApplication.translate("MainWindow", "Load", None))
        self.gp_panel_10_rawbayer.setTitle(QCoreApplication.translate("MainWindow", "Raw-Bayer Image: ROI (Region of Interest) selection", None))
        self.cb_2dimg_key.setItemText(0, QCoreApplication.translate("MainWindow", "Raw bayer", None))
        self.cb_2dimg_key.setItemText(1, QCoreApplication.translate("MainWindow", "Raw bayer (Noise Filter)", None))
        self.cb_2dimg_key.setItemText(2, QCoreApplication.translate("MainWindow", "Raw bayer (RGB)", None))
        self.cb_2dimg_key.setItemText(3, QCoreApplication.translate("MainWindow", "Raw bayer (RGB + Demosiac)", None))
        self.cb_2dimg_key.setItemText(4, QCoreApplication.translate("MainWindow", "Raw bayer (RGB + Demosiac + Filter)", None))
        self.cb_2dimg_key.setItemText(5, QCoreApplication.translate("MainWindow", "Red", None))
        self.cb_2dimg_key.setItemText(6, QCoreApplication.translate("MainWindow", "Green", None))
        self.cb_2dimg_key.setItemText(7, QCoreApplication.translate("MainWindow", "Blue", None))
        self.cb_2dimg_key.setItemText(8, QCoreApplication.translate("MainWindow", "Mask red", None))
        self.cb_2dimg_key.setItemText(9, QCoreApplication.translate("MainWindow", "Mask green", None))
        self.cb_2dimg_key.setItemText(10, QCoreApplication.translate("MainWindow", "Mask blue", None))
        self.cb_2dimg_key.setItemText(11, QCoreApplication.translate("MainWindow", "Wavelength", None))
        self.cb_2dimg_key.setItemText(12, QCoreApplication.translate("MainWindow", "Background Est.", None))

        self.cb_invert_y_axis_of_rawbayer.setText(QCoreApplication.translate("MainWindow", "Invert Y axis", None))
        self.cb_shows_calibrated_wl.setText(QCoreApplication.translate("MainWindow", "Show", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", "_", None))
        self.cb_759_channel.setItemText(0, QCoreApplication.translate("MainWindow", "red", None))
        self.cb_759_channel.setItemText(1, QCoreApplication.translate("MainWindow", "green", None))
        self.cb_759_channel.setItemText(2, QCoreApplication.translate("MainWindow", "green2", None))
        self.cb_759_channel.setItemText(3, QCoreApplication.translate("MainWindow", "blue", None))

        self.label_8.setText("")
        self.label_3.setText("")
        self.pb_wave_calib.setText(QCoreApplication.translate("MainWindow", "Calc", None))
        self._l.setText(QCoreApplication.translate("MainWindow", "Wavelength per pixel (nm/px)", None))
        self.pb_waveperpixel_reset.setText(QCoreApplication.translate("MainWindow", "<== Reset Value", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "x", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", "y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "pos", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "size", None))
        self.tw_midcol.setTabText(self.tw_midcol.indexOf(self.midcol_tab1_wave), QCoreApplication.translate("MainWindow", "Wavelength Calibration", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", "Red", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", "Green", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", "Blue", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", "Tab 1", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", "Tab 2", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", "size", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", "Y", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", "X (Right)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", "X (Left)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", "pos", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", "X (Right)", None))
        self.pb_bg_calc.setText(QCoreApplication.translate("MainWindow", "Calc", None))
        self.tw_midcol.setTabText(self.tw_midcol.indexOf(self.midcol_tab2_bgnd), QCoreApplication.translate("MainWindow", "Background Est", None))
        self.gb_control_panel.setTitle("")
        self._l_1.setText(QCoreApplication.translate("MainWindow", "Hor. (center)", None))
        # if QT_CONFIG(tooltip)
        self.sb_obje_posy.setToolTip(QCoreApplication.translate("MainWindow", '<html><head/><body><p><img src=":/newPrefix/raw_bayer_base_vert_obje_top.png"/></p></body></html>', None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.sb_obje_sizy.setToolTip(QCoreApplication.translate("MainWindow", '<html><head/><body><p><img src=":/newPrefix/raw_bayer_base_vert_obje_height.png"/></p></body></html>', None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.sb_gray_posy.setToolTip(QCoreApplication.translate("MainWindow", '<html><head/><body><p><img src=":/newPrefix/raw_bayer_base_vert_gray_top.png"/></p></body></html>', None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.sb_gray_sizy.setToolTip(QCoreApplication.translate("MainWindow", '<html><head/><body><p><img src=":/newPrefix/raw_bayer_base_vert_gray_height.png"/></p></body></html>', None))
        # endif // QT_CONFIG(tooltip)
        self._l_11.setText(QCoreApplication.translate("MainWindow", "Top (pixel)", None))
        self._l_3.setText(QCoreApplication.translate("MainWindow", "Vert. Object Pixel Range", None))
        self._l_8.setText(QCoreApplication.translate("MainWindow", "Start (pixel)", None))
        self._l_2.setText(QCoreApplication.translate("MainWindow", "Vert. Gray Pixel Range", None))
        self._l_4.setText(QCoreApplication.translate("MainWindow", "Height (in pixel)", None))
        self._l_9.setText(QCoreApplication.translate("MainWindow", "Width (in pixel)", None))
        # if QT_CONFIG(tooltip)
        self.sb_midx_init.setToolTip(QCoreApplication.translate("MainWindow", '<html><head/><body><p><img src=":/newPrefix/raw_bayer_horizontal_center_start.png"/></p></body></html>', None))
        # endif // QT_CONFIG(tooltip)
        self.tw_midcol.setTabText(self.tw_midcol.indexOf(self.midcol_tab3_rois), QCoreApplication.translate("MainWindow", "ROI geometry", None))
        self.gp_panel_15_roiselect.setTitle(QCoreApplication.translate("MainWindow", "GroupBox", None))
        self.pb_select_gray_roi.setText(QCoreApplication.translate("MainWindow", "Take Gray", None))
        self.pb_select_obje_roi.setText(QCoreApplication.translate("MainWindow", "Take Object", None))
        self.gp_panel_20_3roi_dist.setTitle(QCoreApplication.translate("MainWindow", "Spectrum (Scatter-plot)", None))
        self.gp_panel_25_savgol.setTitle(QCoreApplication.translate("MainWindow", "GroupBox", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", "SavGol Window (nm)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", "SavGol Degree", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", "Number", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", "Wavelength step (nm)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", "Wavelength (end)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", "Wavelength (init)", None))
        self.pb_savgol_calc.setText(QCoreApplication.translate("MainWindow", "Savgol", None))
        self.gp_panel_30_rgb_curves.setTitle(QCoreApplication.translate("MainWindow", "Spectrum (Curves)", None))
        self.gp_panel_35_refl_calculate.setTitle(QCoreApplication.translate("MainWindow", "GroupBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "\u03bb\u2081", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", "\u03bb\u2082", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", "\u03b1\u2081", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", "\u03bb\u2083", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", "\u03b1\u2082", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", "\u03b1\u2083", None))
        self.pb_select_obje_roi_3.setText(QCoreApplication.translate("MainWindow", "Take Object", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", "GroupBox", None))
        self.gp_panel_40_3refl_to_1refl.setTitle(QCoreApplication.translate("MainWindow", "Spectral Reflection Calculation", None))
        self.pb_calibrate_calculate.setText(QCoreApplication.translate("MainWindow", "Calculate (Ctrl+R)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", "gray-to-white", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", "Refl. (RGB)", None))
        self._l_12.setText(QCoreApplication.translate("MainWindow", "0 ~ Wavelenght (nm)", None))
        self._l_13.setText(QCoreApplication.translate("MainWindow", "1 ~ Wavelenght (nm)", None))
        self.cb_calc5_norm.setText(QCoreApplication.translate("MainWindow", "Normalize it", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", "Refl. (Final)", None))
        self.cb_export_bayer_as_npy.setText(QCoreApplication.translate("MainWindow", "Export (Bayer as NPY)", None))
        self.cb_export_bayer_as_mat.setText(QCoreApplication.translate("MainWindow", "Export (Bayer as MAT)", None))
        self.cb_export_ref_CSV_simple.setText(QCoreApplication.translate("MainWindow", "Export CSV (only reflection)", None))
        self.cb_export_ref_CSV_full.setText(QCoreApplication.translate("MainWindow", "Export CSV (FULL)", None))
        # if QT_CONFIG(tooltip)
        self.pb_export.setToolTip(QCoreApplication.translate("MainWindow", '<html><head/><body><p><img src=":/newPrefix/Howto-export.png"/></p></body></html>', None))
        # endif // QT_CONFIG(tooltip)
        self.pb_export.setText(QCoreApplication.translate("MainWindow", "Export (Ctrl+E)", None))
        # if QT_CONFIG(tooltip)
        self.label_2.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>History of Geometrical Parameters of Previous usages on this data</p><p>(ie. you can get exact geometrical parameter when you calculated in the past)</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Export Parameter History:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", "GroupBox", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "Operation", None))
        self.menuDirectory_operations.setTitle(QCoreApplication.translate("MainWindow", "Directory Movements", None))
        self.menuType_Here.setTitle(QCoreApplication.translate("MainWindow", "Type Here", None))
        self.menuFile_Operations_on_selected_file.setTitle(QCoreApplication.translate("MainWindow", "File Operations (on selected file)", None))
        self.menuGeometry_Settings.setTitle(QCoreApplication.translate("MainWindow", "Geometry Settings", None))
        self.menuTutorial.setTitle(QCoreApplication.translate("MainWindow", "Help", None))

    # retranslateUi
