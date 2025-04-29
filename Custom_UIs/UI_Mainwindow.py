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
        self.gridLayout_10 = QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")

        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName("splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
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
        self.cb_ft_filter = QCheckBox(self.gb_dir_panel)
        self.cb_ft_filter.setObjectName("cb_ft_filter")
        self.cb_ft_filter.setChecked(True)
        self.cb_ft_filter.setTristate(False)

        self.gridLayout.addWidget(self.cb_ft_filter, 0, 0, 1, 2)

        self._l_14 = QLabel(self.gb_dir_panel)
        self._l_14.setObjectName("_l_14")

        self.gridLayout.addWidget(self._l_14, 4, 0, 1, 1)

        self.pb_dir_goto_parent = QPushButton(self.gb_dir_panel)
        self.pb_dir_goto_parent.setObjectName("pb_dir_goto_parent")

        self.gridLayout.addWidget(self.pb_dir_goto_parent, 1, 0, 1, 1)

        self.le_tv_name_narrower = QLineEdit(self.gb_dir_panel)
        self.le_tv_name_narrower.setObjectName("le_tv_name_narrower")

        self.gridLayout.addWidget(self.le_tv_name_narrower, 4, 1, 1, 1)

        self.pb_system_file_explorer = QPushButton(self.gb_dir_panel)
        self.pb_system_file_explorer.setObjectName("pb_system_file_explorer")

        self.gridLayout.addWidget(self.pb_system_file_explorer, 1, 1, 1, 1)

        self.tv_dir = QTreeView(self.gb_dir_panel)
        self.tv_dir.setObjectName("tv_dir")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.tv_dir.sizePolicy().hasHeightForWidth())
        self.tv_dir.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies(["Monospace"])
        font.setPointSize(10)
        self.tv_dir.setFont(font)
        self.tv_dir.setSortingEnabled(True)

        self.gridLayout.addWidget(self.tv_dir, 3, 0, 1, 2)

        self.graph_webcam = ImageView(self.gb_dir_panel)
        self.graph_webcam.setObjectName("graph_webcam")

        self.gridLayout.addWidget(self.graph_webcam, 5, 0, 1, 2)

        self.tabWidget_2 = QTabWidget(self.gb_dir_panel)
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
        self.hs_target_distance.setOrientation(Qt.Orientation.Horizontal)
        self.hs_target_distance.setTickPosition(QSlider.TickPosition.TicksBothSides)
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
        self.hs_physical_elv.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.hs_physical_elv, 2, 1, 1, 1)

        self.hs_physical_height = QSlider(self.tab_7)
        self.hs_physical_height.setObjectName("hs_physical_height")
        self.hs_physical_height.setMaximum(300)
        self.hs_physical_height.setValue(150)
        self.hs_physical_height.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.hs_physical_height, 1, 1, 1, 1)

        self.l_physical_elv = QLabel(self.tab_7)
        self.l_physical_elv.setObjectName("l_physical_elv")

        self.gridLayout_3.addWidget(self.l_physical_elv, 2, 0, 1, 1)

        self.l_physical_distance = QLabel(self.tab_7)
        self.l_physical_distance.setObjectName("l_physical_distance")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.l_physical_distance.sizePolicy().hasHeightForWidth())
        self.l_physical_distance.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.l_physical_distance, 3, 0, 1, 2)

        _ = self.tabWidget_2.addTab(self.tab_7, "")

        self.gridLayout.addWidget(self.tabWidget_2, 6, 0, 1, 2)

        self.tb_meta_json = QLabel(self.gb_dir_panel)
        self.tb_meta_json.setObjectName("tb_meta_json")

        self.gridLayout.addWidget(self.tb_meta_json, 7, 0, 1, 2)

        self.gridLayout.setRowStretch(3, 10)
        self.gridLayout.setRowStretch(5, 10)
        self.gridLayout.setRowStretch(6, 10)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 434, 246))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cb_rawbayer_visual_demosiac = QCheckBox(self.scrollAreaWidgetContents_2)
        self.cb_rawbayer_visual_demosiac.setObjectName("cb_rawbayer_visual_demosiac")
        self.cb_rawbayer_visual_demosiac.setChecked(True)

        self.horizontalLayout_2.addWidget(self.cb_rawbayer_visual_demosiac)

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

        self.tw_midcol = QTabWidget(self.gp_webcam_meta)
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

        self.gridLayout_4.addWidget(self.pushButton, 0, 1, 1, 1)

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
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_7 = QLabel(self.midcol_tab1_wave)
        self.label_7.setObjectName("label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

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
        _ = self.tw_midcol.addTab(self.midcol_tab2_bgnd, "")
        self.midcol_tab3_rois = QWidget()
        self.midcol_tab3_rois.setObjectName("midcol_tab3_rois")
        self.gridLayout_6 = QGridLayout(self.midcol_tab3_rois)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gb_control_panel = QGroupBox(self.midcol_tab3_rois)
        self.gb_control_panel.setObjectName("gb_control_panel")
        self.gridLayout_2 = QGridLayout(self.gb_control_panel)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self._l_8 = QLabel(self.gb_control_panel)
        self._l_8.setObjectName("_l_8")
        sizePolicy2.setHeightForWidth(self._l_8.sizePolicy().hasHeightForWidth())
        self._l_8.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self._l_8, 1, 1, 1, 1)

        self._line = QFrame(self.gb_control_panel)
        self._line.setObjectName("_line")
        self._line.setFrameShape(QFrame.Shape.HLine)
        self._line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self._line, 3, 0, 1, 3)

        self._l_4 = QLabel(self.gb_control_panel)
        self._l_4.setObjectName("_l_4")
        sizePolicy2.setHeightForWidth(self._l_4.sizePolicy().hasHeightForWidth())
        self._l_4.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self._l_4, 4, 2, 1, 1)

        self._l_9 = QLabel(self.gb_control_panel)
        self._l_9.setObjectName("_l_9")
        sizePolicy2.setHeightForWidth(self._l_9.sizePolicy().hasHeightForWidth())
        self._l_9.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self._l_9, 1, 2, 1, 1)

        self._l_3 = QLabel(self.gb_control_panel)
        self._l_3.setObjectName("_l_3")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 255, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        self._l_3.setPalette(palette)

        self.gridLayout_2.addWidget(self._l_3, 8, 0, 1, 1)

        self.sb_midx_size = QSpinBox(self.gb_control_panel)
        self.sb_midx_size.setObjectName("sb_midx_size")
        self.sb_midx_size.setEnabled(False)
        self.sb_midx_size.setMaximum(9999)
        self.sb_midx_size.setValue(700)

        self.gridLayout_2.addWidget(self.sb_midx_size, 2, 2, 1, 1)

        self._l_1 = QLabel(self.gb_control_panel)
        self._l_1.setObjectName("_l_1")
        sizePolicy2.setHeightForWidth(self._l_1.sizePolicy().hasHeightForWidth())
        self._l_1.setSizePolicy(sizePolicy2)
        palette1 = QPalette()
        brush1 = QBrush(QColor(0, 170, 0, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush1)
        self._l_1.setPalette(palette1)

        self.gridLayout_2.addWidget(self._l_1, 2, 0, 1, 1)

        self._l_11 = QLabel(self.gb_control_panel)
        self._l_11.setObjectName("_l_11")
        sizePolicy2.setHeightForWidth(self._l_11.sizePolicy().hasHeightForWidth())
        self._l_11.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self._l_11, 4, 1, 1, 1)

        self._l_2 = QLabel(self.gb_control_panel)
        self._l_2.setObjectName("_l_2")
        palette2 = QPalette()
        brush2 = QBrush(QColor(255, 0, 0, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush2)
        self._l_2.setPalette(palette2)

        self.gridLayout_2.addWidget(self._l_2, 5, 0, 1, 1)

        self.sb_obje_posy = QSpinBox(self.gb_control_panel)
        self.sb_obje_posy.setObjectName("sb_obje_posy")
        self.sb_obje_posy.setMinimum(0)
        self.sb_obje_posy.setMaximum(20000)
        self.sb_obje_posy.setSingleStep(2)
        self.sb_obje_posy.setValue(1200)

        self.gridLayout_2.addWidget(self.sb_obje_posy, 8, 1, 1, 1)

        self.sb_gray_posy = QSpinBox(self.gb_control_panel)
        self.sb_gray_posy.setObjectName("sb_gray_posy")
        self.sb_gray_posy.setMinimum(0)
        self.sb_gray_posy.setMaximum(20000)
        self.sb_gray_posy.setSingleStep(2)
        self.sb_gray_posy.setValue(1050)

        self.gridLayout_2.addWidget(self.sb_gray_posy, 5, 1, 1, 1)

        self.sb_obje_sizy = QSpinBox(self.gb_control_panel)
        self.sb_obje_sizy.setObjectName("sb_obje_sizy")
        self.sb_obje_sizy.setMinimum(0)
        self.sb_obje_sizy.setMaximum(20000)
        self.sb_obje_sizy.setSingleStep(2)
        self.sb_obje_sizy.setValue(50)

        self.gridLayout_2.addWidget(self.sb_obje_sizy, 8, 2, 1, 1)

        self.sb_gray_sizy = QSpinBox(self.gb_control_panel)
        self.sb_gray_sizy.setObjectName("sb_gray_sizy")
        self.sb_gray_sizy.setMinimum(0)
        self.sb_gray_sizy.setMaximum(20000)
        self.sb_gray_sizy.setSingleStep(2)
        self.sb_gray_sizy.setValue(50)

        self.gridLayout_2.addWidget(self.sb_gray_sizy, 5, 2, 1, 1)

        self.line_3 = QFrame(self.gb_control_panel)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 9, 0, 1, 3)

        self.sb_midx_init = QSpinBox(self.gb_control_panel)
        self.sb_midx_init.setObjectName("sb_midx_init")
        self.sb_midx_init.setMinimum(0)
        self.sb_midx_init.setMaximum(17000)
        self.sb_midx_init.setSingleStep(2)
        self.sb_midx_init.setValue(1350)

        self.gridLayout_2.addWidget(self.sb_midx_init, 2, 1, 1, 1)

        self.gridLayout_6.addWidget(self.gb_control_panel, 1, 0, 1, 1)

        self.graph_raw = PlotWidget(self.midcol_tab3_rois)
        self.graph_raw.setObjectName("graph_raw")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(200)
        sizePolicy6.setHeightForWidth(self.graph_raw.sizePolicy().hasHeightForWidth())
        self.graph_raw.setSizePolicy(sizePolicy6)
        self.graph_raw.setMinimumSize(QSize(400, 200))

        self.gridLayout_6.addWidget(self.graph_raw, 0, 0, 1, 1)

        _ = self.tw_midcol.addTab(self.midcol_tab3_rois, "")

        self.verticalLayout.addWidget(self.tw_midcol)

        self.splitter.addWidget(self.gp_webcam_meta)
        self.gp_spectral_panel = QGroupBox(self.splitter)
        self.gp_spectral_panel.setObjectName("gp_spectral_panel")
        self.formLayout = QFormLayout(self.gp_spectral_panel)
        self.formLayout.setObjectName("formLayout")
        self.pb_calibrate_calculate = QPushButton(self.gp_spectral_panel)
        self.pb_calibrate_calculate.setObjectName("pb_calibrate_calculate")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pb_calibrate_calculate.sizePolicy().hasHeightForWidth())
        self.pb_calibrate_calculate.setSizePolicy(sizePolicy7)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pb_calibrate_calculate)

        self.pbar_calc = QProgressBar(self.gp_spectral_panel)
        self.pbar_calc.setObjectName("pbar_calc")
        self.pbar_calc.setMaximum(100)
        self.pbar_calc.setValue(0)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.pbar_calc)

        self.scrollArea = QScrollArea(self.gp_spectral_panel)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 349, 525))
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
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.graph_calc1_desalted_roi.sizePolicy().hasHeightForWidth())
        self.graph_calc1_desalted_roi.setSizePolicy(sizePolicy8)
        self.graph_calc1_desalted_roi.setMinimumSize(QSize(150, 0))

        self.verticalLayout_5.addWidget(self.graph_calc1_desalted_roi)

        self.txt_calc1_desalt = QTextBrowser(self.tab)
        self.txt_calc1_desalt.setObjectName("txt_calc1_desalt")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.txt_calc1_desalt.sizePolicy().hasHeightForWidth())
        self.txt_calc1_desalt.setSizePolicy(sizePolicy9)
        self.txt_calc1_desalt.setMinimumSize(QSize(0, 0))
        self.txt_calc1_desalt.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_5.addWidget(self.txt_calc1_desalt)

        _ = self.tabWidget.addTab(self.tab, "")
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
        sizePolicy9.setHeightForWidth(self.txt_calc2_bg.sizePolicy().hasHeightForWidth())
        self.txt_calc2_bg.setSizePolicy(sizePolicy9)
        self.txt_calc2_bg.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_6.addWidget(self.txt_calc2_bg)

        _ = self.tabWidget.addTab(self.tab_2, "")
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
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(200)
        sizePolicy10.setHeightForWidth(self.graph_calc3_759_calib.sizePolicy().hasHeightForWidth())
        self.graph_calc3_759_calib.setSizePolicy(sizePolicy10)
        self.graph_calc3_759_calib.setMinimumSize(QSize(300, 200))

        self.verticalLayout_7.addWidget(self.graph_calc3_759_calib)

        self.txt_calc3_cal759 = QTextBrowser(self.tab_3)
        self.txt_calc3_cal759.setObjectName("txt_calc3_cal759")
        self.txt_calc3_cal759.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_7.addWidget(self.txt_calc3_cal759)

        _ = self.tabWidget.addTab(self.tab_3, "")
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

        self.cb_export_bayer_as_npy = QCheckBox(self.gp_spectral_panel)
        self.cb_export_bayer_as_npy.setObjectName("cb_export_bayer_as_npy")
        self.cb_export_bayer_as_npy.setEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.cb_export_bayer_as_npy)

        self.cb_export_bayer_as_mat = QCheckBox(self.gp_spectral_panel)
        self.cb_export_bayer_as_mat.setObjectName("cb_export_bayer_as_mat")
        self.cb_export_bayer_as_mat.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cb_export_bayer_as_mat)

        self.cb_export_ref_CSV_simple = QCheckBox(self.gp_spectral_panel)
        self.cb_export_ref_CSV_simple.setObjectName("cb_export_ref_CSV_simple")
        self.cb_export_ref_CSV_simple.setChecked(True)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.cb_export_ref_CSV_simple)

        self.cb_export_ref_CSV_full = QCheckBox(self.gp_spectral_panel)
        self.cb_export_ref_CSV_full.setObjectName("cb_export_ref_CSV_full")
        self.cb_export_ref_CSV_full.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cb_export_ref_CSV_full)

        self.pb_export = QPushButton(self.gp_spectral_panel)
        self.pb_export.setObjectName("pb_export")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.pb_export)

        self.pbar_export = QProgressBar(self.gp_spectral_panel)
        self.pbar_export.setObjectName("pbar_export")
        self.pbar_export.setValue(0)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.pbar_export)

        self.label_2 = QLabel(self.gp_spectral_panel)
        self.label_2.setObjectName("label_2")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.cb_parameter_history = QComboBox(self.gp_spectral_panel)
        self.cb_parameter_history.setObjectName("cb_parameter_history")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.cb_parameter_history)

        self.line_2 = QFrame(self.gp_spectral_panel)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.line_2)

        self.splitter.addWidget(self.gp_spectral_panel)

        self.gridLayout_10.addWidget(self.splitter, 1, 0, 1, 1)

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
        self.tw_midcol.setCurrentIndex(0)
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
        # if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", '<html><head/><body><p><img src=":/newPrefix/MAIN_howto.png"/></p></body></html>', None))
        # endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", "Help: (Move the mouse-cursor here to see operation order)", None))
        self.gb_dir_panel.setTitle(QCoreApplication.translate("MainWindow", "Directory Control Panel", None))
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
        self._l_14.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>- Narrows file/directory names by given &quot;string&quot;.</p><p>- Helpful when you have too many files/directories</p><p><br/></p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self._l_14.setText(QCoreApplication.translate("MainWindow", "Narrow by name (Alf+f)", None))
        # if QT_CONFIG(tooltip)
        self.pb_dir_goto_parent.setToolTip(QCoreApplication.translate("MainWindow", "<html><head/><body><p>Go to parent folder</p></body></html>", None))
        # endif // QT_CONFIG(tooltip)
        self.pb_dir_goto_parent.setText(QCoreApplication.translate("MainWindow", "Go to parent (Backspace)", None))
        self.pb_system_file_explorer.setText(QCoreApplication.translate("MainWindow", "Open Sys. file-explorer", None))
        self.l_target_distance.setText(QCoreApplication.translate("MainWindow", "Distance:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", "Tab 1", None))
        self.l_physical_height.setText(QCoreApplication.translate("MainWindow", "Height: ", None))
        self.l_physical_elv.setText(QCoreApplication.translate("MainWindow", "Pitch:", None))
        self.l_physical_distance.setText(QCoreApplication.translate("MainWindow", "Distance:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", "Tab 2", None))
        self.tb_meta_json.setText("")
        self.gp_webcam_meta.setTitle(QCoreApplication.translate("MainWindow", "Raw-Bayer Image: ROI (Region of Interest) selection", None))
        self.cb_rawbayer_visual_demosiac.setText(QCoreApplication.translate("MainWindow", "Demosiac Bayer (just for visual)", None))
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
        self.tw_midcol.setTabText(self.tw_midcol.indexOf(self.midcol_tab2_bgnd), QCoreApplication.translate("MainWindow", "Background Est", None))
        self.gb_control_panel.setTitle("")
        self._l_8.setText(QCoreApplication.translate("MainWindow", "Start (pixel)", None))
        self._l_4.setText(QCoreApplication.translate("MainWindow", "Height (in pixel)", None))
        self._l_9.setText(QCoreApplication.translate("MainWindow", "Width (in pixel)", None))
        self._l_3.setText(QCoreApplication.translate("MainWindow", "Vert. Object Pixel Range", None))
        self._l_1.setText(QCoreApplication.translate("MainWindow", "Hor. (center)", None))
        self._l_11.setText(QCoreApplication.translate("MainWindow", "Top (pixel)", None))
        self._l_2.setText(QCoreApplication.translate("MainWindow", "Vert. Gray Pixel Range", None))
        # if QT_CONFIG(tooltip)
        self.sb_obje_posy.setToolTip(QCoreApplication.translate("MainWindow", '<html><head/><body><p><img src=":/newPrefix/raw_bayer_base_vert_obje_top.png"/></p></body></html>', None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.sb_gray_posy.setToolTip(QCoreApplication.translate("MainWindow", '<html><head/><body><p><img src=":/newPrefix/raw_bayer_base_vert_gray_top.png"/></p></body></html>', None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.sb_obje_sizy.setToolTip(QCoreApplication.translate("MainWindow", '<html><head/><body><p><img src=":/newPrefix/raw_bayer_base_vert_obje_height.png"/></p></body></html>', None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.sb_gray_sizy.setToolTip(QCoreApplication.translate("MainWindow", '<html><head/><body><p><img src=":/newPrefix/raw_bayer_base_vert_gray_height.png"/></p></body></html>', None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.sb_midx_init.setToolTip(QCoreApplication.translate("MainWindow", '<html><head/><body><p><img src=":/newPrefix/raw_bayer_horizontal_center_start.png"/></p></body></html>', None))
        # endif // QT_CONFIG(tooltip)
        self.tw_midcol.setTabText(self.tw_midcol.indexOf(self.midcol_tab3_rois), QCoreApplication.translate("MainWindow", "ROI geometry", None))
        self.gp_spectral_panel.setTitle(QCoreApplication.translate("MainWindow", "Spectral Reflection Calculation", None))
        self.pb_calibrate_calculate.setText(QCoreApplication.translate("MainWindow", "Calculate (Ctrl+R)", None))
        self.cb_calc1_desalt.setText(QCoreApplication.translate("MainWindow", "Median filtering (3px vertically) for SALT noise", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", "De-Salt", None))
        self.cb_calc2_background.setText(QCoreApplication.translate("MainWindow", "Estimate and substract Background", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", "BG est.", None))
        self.cb_calc3_calibrate_759.setText(QCoreApplication.translate("MainWindow", "Calibrate Based on 759.3nm absorption", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", "759 calib.", None))
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
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "Operation", None))
        self.menuDirectory_operations.setTitle(QCoreApplication.translate("MainWindow", "Directory Movements", None))
        self.menuType_Here.setTitle(QCoreApplication.translate("MainWindow", "Type Here", None))
        self.menuFile_Operations_on_selected_file.setTitle(QCoreApplication.translate("MainWindow", "File Operations (on selected file)", None))
        self.menuGeometry_Settings.setTitle(QCoreApplication.translate("MainWindow", "Geometry Settings", None))
        self.menuTutorial.setTitle(QCoreApplication.translate("MainWindow", "Help", None))

    # retranslateUi
