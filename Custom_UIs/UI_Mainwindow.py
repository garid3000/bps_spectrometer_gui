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
from pyqtgraph import ImageView, PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow) -> None:
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 929)
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
        self.limg_webcam = QLabelClick(self.gb_dir_panel)
        self.limg_webcam.setObjectName("limg_webcam")

        self.gridLayout_3.addWidget(self.limg_webcam, 2, 0, 1, 1)

        self.tb_meta_json = QTextBrowser(self.gb_dir_panel)
        self.tb_meta_json.setObjectName("tb_meta_json")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_meta_json.sizePolicy().hasHeightForWidth())
        self.tb_meta_json.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies(["Monospace"])
        self.tb_meta_json.setFont(font)

        self.gridLayout_3.addWidget(self.tb_meta_json, 3, 0, 1, 1)

        self.cb_ft_filter = QCheckBox(self.gb_dir_panel)
        self.cb_ft_filter.setObjectName("cb_ft_filter")
        self.cb_ft_filter.setChecked(True)

        self.gridLayout_3.addWidget(self.cb_ft_filter, 0, 0, 1, 1)

        self.tv_dir = QTreeView(self.gb_dir_panel)
        self.tv_dir.setObjectName("tv_dir")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.tv_dir.sizePolicy().hasHeightForWidth())
        self.tv_dir.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies(["Monospace"])
        font1.setPointSize(10)
        self.tv_dir.setFont(font1)
        self.tv_dir.setSortingEnabled(True)

        self.gridLayout_3.addWidget(self.tv_dir, 1, 0, 1, 1)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 430, 724))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graph_2dimg = ImageView(self.scrollAreaWidgetContents_2)
        self.graph_2dimg.setObjectName("graph_2dimg")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(200)
        sizePolicy2.setVerticalStretch(200)
        sizePolicy2.setHeightForWidth(self.graph_2dimg.sizePolicy().hasHeightForWidth())
        self.graph_2dimg.setSizePolicy(sizePolicy2)
        self.graph_2dimg.setMinimumSize(QSize(400, 400))

        self.verticalLayout_4.addWidget(self.graph_2dimg)

        self.graph_raw = PlotWidget(self.scrollAreaWidgetContents_2)
        self.graph_raw.setObjectName("graph_raw")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(200)
        sizePolicy3.setHeightForWidth(self.graph_raw.sizePolicy().hasHeightForWidth())
        self.graph_raw.setSizePolicy(sizePolicy3)
        self.graph_raw.setMinimumSize(QSize(400, 300))

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
        self.sb_waveperpixel.setSingleStep(0.010000000000000)
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
        self.sb_rigx_init_rel.setMaximum(9999)
        self.sb_rigx_init_rel.setValue(810)

        self.gridLayout_2.addWidget(self.sb_rigx_init_rel, 3, 1, 1, 1)

        self.sb_rigx_size = QSpinBox(self.gb_control_panel)
        self.sb_rigx_size.setObjectName("sb_rigx_size")
        self.sb_rigx_size.setMaximum(100)
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
        self.sb_lefx_init_rel.setMinimum(-999)
        self.sb_lefx_init_rel.setMaximum(9999)
        self.sb_lefx_init_rel.setValue(-50)

        self.gridLayout_2.addWidget(self.sb_lefx_init_rel, 2, 1, 1, 1)

        self._l_8 = QLabel(self.gb_control_panel)
        self._l_8.setObjectName("_l_8")

        self.gridLayout_2.addWidget(self._l_8, 0, 1, 1, 1)

        self.sb_lefx_size = QSpinBox(self.gb_control_panel)
        self.sb_lefx_size.setObjectName("sb_lefx_size")
        self.sb_lefx_size.setMaximum(100)
        self.sb_lefx_size.setValue(40)

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
        self.gridLayout_4 = QGridLayout(self.gp_spectral_panel)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cb_fraunhofer = QCheckBox(self.gp_spectral_panel)
        self.cb_fraunhofer.setObjectName("cb_fraunhofer")

        self.gridLayout_4.addWidget(self.cb_fraunhofer, 0, 1, 1, 1)

        self.scrollArea = QScrollArea(self.gp_spectral_panel)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 429, 772))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.label.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cb_export_bayer_as_tif = QCheckBox(self.scrollAreaWidgetContents)
        self.cb_export_bayer_as_tif.setObjectName("cb_export_bayer_as_tif")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cb_export_bayer_as_tif)

        self.cb_bayer_show_geometry = QCheckBox(self.scrollAreaWidgetContents)
        self.cb_bayer_show_geometry.setObjectName("cb_bayer_show_geometry")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.cb_bayer_show_geometry)

        self.cb_export_bayer_as_npy = QCheckBox(self.scrollAreaWidgetContents)
        self.cb_export_bayer_as_npy.setObjectName("cb_export_bayer_as_npy")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_export_bayer_as_npy)

        self.cb_export_bayer_as_mat = QCheckBox(self.scrollAreaWidgetContents)
        self.cb_export_bayer_as_mat.setObjectName("cb_export_bayer_as_mat")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.cb_export_bayer_as_mat)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.line)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.label_2.setFont(font3)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.label_2)

        self.cb_export_raw_plot_as_png = QCheckBox(self.scrollAreaWidgetContents)
        self.cb_export_raw_plot_as_png.setObjectName("cb_export_raw_plot_as_png")

        self.formLayout.setWidget(
            6, QFormLayout.LabelRole, self.cb_export_raw_plot_as_png
        )

        self.tbtn_raw_spectrum_config = QToolButton(self.scrollAreaWidgetContents)
        self.tbtn_raw_spectrum_config.setObjectName("tbtn_raw_spectrum_config")

        self.formLayout.setWidget(
            6, QFormLayout.FieldRole, self.tbtn_raw_spectrum_config
        )

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.line_2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font3)

        self.formLayout.setWidget(10, QFormLayout.SpanningRole, self.label_3)

        self.cb_export_ref_plot_as_png = QCheckBox(self.scrollAreaWidgetContents)
        self.cb_export_ref_plot_as_png.setObjectName("cb_export_ref_plot_as_png")

        self.formLayout.setWidget(
            11, QFormLayout.LabelRole, self.cb_export_ref_plot_as_png
        )

        self.tbtn_ref_spectrum_config = QToolButton(self.scrollAreaWidgetContents)
        self.tbtn_ref_spectrum_config.setObjectName("tbtn_ref_spectrum_config")

        self.formLayout.setWidget(
            11, QFormLayout.FieldRole, self.tbtn_ref_spectrum_config
        )

        self.graph_ref = PlotWidget(self.scrollAreaWidgetContents)
        self.graph_ref.setObjectName("graph_ref")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(200)
        sizePolicy4.setHeightForWidth(self.graph_ref.sizePolicy().hasHeightForWidth())
        self.graph_ref.setSizePolicy(sizePolicy4)
        self.graph_ref.setMinimumSize(QSize(400, 400))

        self.formLayout.setWidget(12, QFormLayout.SpanningRole, self.graph_ref)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 1, 0, 1, 3)

        self.pb_refresh = QPushButton(self.gp_spectral_panel)
        self.pb_refresh.setObjectName("pb_refresh")

        self.gridLayout_4.addWidget(self.pb_refresh, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.gp_spectral_panel)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_6.setChecked(True)

        self.gridLayout_4.addWidget(self.checkBox_6, 3, 1, 1, 1)

        self.pb_export = QPushButton(self.gp_spectral_panel)
        self.pb_export.setObjectName("pb_export")

        self.gridLayout_4.addWidget(self.pb_export, 3, 2, 1, 1)

        self.splitter.addWidget(self.gp_spectral_panel)

        self.verticalLayout_3.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1240, 19))
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
        self.limg_webcam.setText(QCoreApplication.translate("MainWindow", "....", None))
        self.cb_ft_filter.setText(
            QCoreApplication.translate("MainWindow", "File type filter (Ctrl-F)", None)
        )
        self.gp_webcam_meta.setTitle(
            QCoreApplication.translate("MainWindow", "Webcam + Meta Data Panel", None)
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
            QCoreApplication.translate("MainWindow", "Spectral Data Panel", None)
        )
        self.cb_fraunhofer.setText(
            QCoreApplication.translate("MainWindow", "Calibrate", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "1. Raw Bayer", None)
        )
        self.cb_export_bayer_as_tif.setText(
            QCoreApplication.translate("MainWindow", "Export (Bayer as TIF)", None)
        )
        self.cb_bayer_show_geometry.setText(
            QCoreApplication.translate("MainWindow", "Draw Geometry", None)
        )
        self.cb_export_bayer_as_npy.setText(
            QCoreApplication.translate("MainWindow", "Export (Bayer as NPY)", None)
        )
        self.cb_export_bayer_as_mat.setText(
            QCoreApplication.translate("MainWindow", "Export (Bayer as MAT)", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow", "2. Raw Spectrum (Ditigal Number)", None
            )
        )
        self.cb_export_raw_plot_as_png.setText(
            QCoreApplication.translate("MainWindow", "Export Plot (PNG)", None)
        )
        self.tbtn_raw_spectrum_config.setText(
            QCoreApplication.translate("MainWindow", "Plot Config (Ctrl+Shift+P)", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", "3. Spectrum (Reflectance)", None)
        )
        self.cb_export_ref_plot_as_png.setText(
            QCoreApplication.translate("MainWindow", "Export Plot (PNG)", None)
        )
        self.tbtn_ref_spectrum_config.setText(
            QCoreApplication.translate("MainWindow", "Plot Config (Ctrl+P)", None)
        )
        self.pb_refresh.setText(
            QCoreApplication.translate("MainWindow", "Refresh (Ctrl+R)", None)
        )
        self.checkBox_6.setText(
            QCoreApplication.translate(
                "MainWindow", "Export Numerical Values  (CSV)", None
            )
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
