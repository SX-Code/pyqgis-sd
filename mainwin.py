# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 850)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 850))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_data_preview = QtWidgets.QWidget()
        self.tab_data_preview.setObjectName("tab_data_preview")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_data_preview)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_prev_top = QtWidgets.QFrame(self.tab_data_preview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_prev_top.sizePolicy().hasHeightForWidth())
        self.frame_prev_top.setSizePolicy(sizePolicy)
        self.frame_prev_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prev_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prev_top.setObjectName("frame_prev_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_prev_top)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_prev_tools = QtWidgets.QFrame(self.frame_prev_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_prev_tools.sizePolicy().hasHeightForWidth())
        self.frame_prev_tools.setSizePolicy(sizePolicy)
        self.frame_prev_tools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prev_tools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prev_tools.setObjectName("frame_prev_tools")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_prev_tools)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prev_tools_add = QtWidgets.QFrame(self.frame_prev_tools)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_tools_add.sizePolicy().hasHeightForWidth())
        self.prev_tools_add.setSizePolicy(sizePolicy)
        self.prev_tools_add.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.prev_tools_add.setFrameShadow(QtWidgets.QFrame.Raised)
        self.prev_tools_add.setObjectName("prev_tools_add")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.prev_tools_add)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_add_raster = QtWidgets.QToolButton(self.prev_tools_add)
        self.button_add_raster.setMinimumSize(QtCore.QSize(0, 0))
        self.button_add_raster.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.button_add_raster.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/open_raster"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_add_raster.setIcon(icon)
        self.button_add_raster.setIconSize(QtCore.QSize(36, 36))
        self.button_add_raster.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_add_raster.setAutoRaise(True)
        self.button_add_raster.setObjectName("button_add_raster")
        self.horizontalLayout_3.addWidget(self.button_add_raster)
        self.button_add_shp = QtWidgets.QToolButton(self.prev_tools_add)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.button_add_shp.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/open_vector"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_add_shp.setIcon(icon1)
        self.button_add_shp.setIconSize(QtCore.QSize(36, 36))
        self.button_add_shp.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_add_shp.setAutoRaise(True)
        self.button_add_shp.setObjectName("button_add_shp")
        self.horizontalLayout_3.addWidget(self.button_add_shp)
        self.horizontalLayout_2.addWidget(self.prev_tools_add)
        self.prev_tools_teach = QtWidgets.QFrame(self.frame_prev_tools)
        self.prev_tools_teach.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.prev_tools_teach.setFrameShadow(QtWidgets.QFrame.Raised)
        self.prev_tools_teach.setObjectName("prev_tools_teach")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.prev_tools_teach)
        self.horizontalLayout_9.setContentsMargins(4, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.button_help = QtWidgets.QToolButton(self.prev_tools_teach)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.button_help.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/help"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_help.setIcon(icon2)
        self.button_help.setIconSize(QtCore.QSize(36, 36))
        self.button_help.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_help.setAutoRaise(True)
        self.button_help.setObjectName("button_help")
        self.horizontalLayout_9.addWidget(self.button_help)
        self.horizontalLayout_2.addWidget(self.prev_tools_teach)
        self.horizontalLayout.addWidget(self.frame_prev_tools)
        self.frame_prev_fill = QtWidgets.QFrame(self.frame_prev_top)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.frame_prev_fill.setFont(font)
        self.frame_prev_fill.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prev_fill.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prev_fill.setObjectName("frame_prev_fill")
        self.horizontalLayout.addWidget(self.frame_prev_fill)
        self.verticalLayout_2.addWidget(self.frame_prev_top)
        self.widget_middle = QtWidgets.QWidget(self.tab_data_preview)
        self.widget_middle.setObjectName("widget_middle")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_middle)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.widget_middle)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(2)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.frame_prev_layers = QtWidgets.QFrame(self.splitter)
        self.frame_prev_layers.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_prev_layers.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prev_layers.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prev_layers.setObjectName("frame_prev_layers")
        self.layout_prev_layers = QtWidgets.QVBoxLayout(self.frame_prev_layers)
        self.layout_prev_layers.setContentsMargins(0, 0, 0, 0)
        self.layout_prev_layers.setSpacing(0)
        self.layout_prev_layers.setObjectName("layout_prev_layers")
        self.frame_prev_layers_mgr = QtWidgets.QFrame(self.frame_prev_layers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_prev_layers_mgr.sizePolicy().hasHeightForWidth())
        self.frame_prev_layers_mgr.setSizePolicy(sizePolicy)
        self.frame_prev_layers_mgr.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_prev_layers_mgr.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_prev_layers_mgr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prev_layers_mgr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prev_layers_mgr.setObjectName("frame_prev_layers_mgr")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_prev_layers_mgr)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_prev_layers_mgr)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.button_prev_clear = QtWidgets.QToolButton(self.frame_prev_layers_mgr)
        self.button_prev_clear.setStyleSheet("padding:4px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/clear_layer"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_prev_clear.setIcon(icon3)
        self.button_prev_clear.setIconSize(QtCore.QSize(16, 16))
        self.button_prev_clear.setAutoRaise(True)
        self.button_prev_clear.setObjectName("button_prev_clear")
        self.horizontalLayout_5.addWidget(self.button_prev_clear)
        self.button_prev_remove = QtWidgets.QToolButton(self.frame_prev_layers_mgr)
        self.button_prev_remove.setStyleSheet("padding:4px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/remove_layer"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_prev_remove.setIcon(icon4)
        self.button_prev_remove.setIconSize(QtCore.QSize(16, 16))
        self.button_prev_remove.setAutoRaise(True)
        self.button_prev_remove.setObjectName("button_prev_remove")
        self.horizontalLayout_5.addWidget(self.button_prev_remove)
        self.layout_prev_layers.addWidget(self.frame_prev_layers_mgr)
        self.frame_prev_map = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_prev_map.sizePolicy().hasHeightForWidth())
        self.frame_prev_map.setSizePolicy(sizePolicy)
        self.frame_prev_map.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prev_map.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prev_map.setObjectName("frame_prev_map")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_prev_map)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_prev_map_mgr = QtWidgets.QFrame(self.frame_prev_map)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_prev_map_mgr.sizePolicy().hasHeightForWidth())
        self.frame_prev_map_mgr.setSizePolicy(sizePolicy)
        self.frame_prev_map_mgr.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_prev_map_mgr.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_prev_map_mgr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prev_map_mgr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prev_map_mgr.setObjectName("frame_prev_map_mgr")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_prev_map_mgr)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.prev_map_tools = QtWidgets.QFrame(self.frame_prev_map_mgr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_map_tools.sizePolicy().hasHeightForWidth())
        self.prev_map_tools.setSizePolicy(sizePolicy)
        self.prev_map_tools.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.prev_map_tools.setFrameShadow(QtWidgets.QFrame.Raised)
        self.prev_map_tools.setObjectName("prev_map_tools")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.prev_map_tools)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.button_move = QtWidgets.QToolButton(self.prev_map_tools)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/action_move"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_move.setIcon(icon5)
        self.button_move.setCheckable(True)
        self.button_move.setChecked(True)
        self.button_move.setAutoExclusive(True)
        self.button_move.setAutoRaise(True)
        self.button_move.setObjectName("button_move")
        self.horizontalLayout_6.addWidget(self.button_move)
        self.button_zoom_in = QtWidgets.QToolButton(self.prev_map_tools)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/action_zoom_in"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_zoom_in.setIcon(icon6)
        self.button_zoom_in.setCheckable(True)
        self.button_zoom_in.setChecked(False)
        self.button_zoom_in.setAutoExclusive(True)
        self.button_zoom_in.setAutoRaise(True)
        self.button_zoom_in.setObjectName("button_zoom_in")
        self.horizontalLayout_6.addWidget(self.button_zoom_in)
        self.button_zoom_out = QtWidgets.QToolButton(self.prev_map_tools)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/action_zoom_out"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_zoom_out.setIcon(icon7)
        self.button_zoom_out.setCheckable(True)
        self.button_zoom_out.setAutoExclusive(True)
        self.button_zoom_out.setAutoRaise(True)
        self.button_zoom_out.setObjectName("button_zoom_out")
        self.horizontalLayout_6.addWidget(self.button_zoom_out)
        self.button_refresh = QtWidgets.QToolButton(self.prev_map_tools)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/action_refresh"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_refresh.setIcon(icon8)
        self.button_refresh.setCheckable(True)
        self.button_refresh.setAutoExclusive(True)
        self.button_refresh.setAutoRaise(True)
        self.button_refresh.setObjectName("button_refresh")
        self.horizontalLayout_6.addWidget(self.button_refresh)
        self.verticalLayout_5.addWidget(self.prev_map_tools)
        self.verticalLayout_4.addWidget(self.frame_prev_map_mgr)
        self.frame_prev_map_show = QtWidgets.QFrame(self.frame_prev_map)
        self.frame_prev_map_show.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_prev_map_show.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prev_map_show.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prev_map_show.setObjectName("frame_prev_map_show")
        self.preview_qgis_map = QtWidgets.QVBoxLayout(self.frame_prev_map_show)
        self.preview_qgis_map.setContentsMargins(0, 0, 0, 0)
        self.preview_qgis_map.setSpacing(0)
        self.preview_qgis_map.setObjectName("preview_qgis_map")
        self.verticalLayout_4.addWidget(self.frame_prev_map_show)
        self.horizontalLayout_4.addWidget(self.splitter)
        self.verticalLayout_2.addWidget(self.widget_middle)
        self.frame_prev_bottom = QtWidgets.QFrame(self.tab_data_preview)
        self.frame_prev_bottom.setMinimumSize(QtCore.QSize(0, 34))
        self.frame_prev_bottom.setMaximumSize(QtCore.QSize(16777215, 34))
        self.frame_prev_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_prev_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_prev_bottom.setObjectName("frame_prev_bottom")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_prev_bottom)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_tips_prev = QtWidgets.QLabel(self.frame_prev_bottom)
        self.label_tips_prev.setText("")
        self.label_tips_prev.setObjectName("label_tips_prev")
        self.horizontalLayout_7.addWidget(self.label_tips_prev)
        self.frame_coords = QtWidgets.QFrame(self.frame_prev_bottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_coords.sizePolicy().hasHeightForWidth())
        self.frame_coords.setSizePolicy(sizePolicy)
        self.frame_coords.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_coords.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_coords.setObjectName("frame_coords")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_coords)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_coords_name = QtWidgets.QLabel(self.frame_coords)
        self.label_coords_name.setObjectName("label_coords_name")
        self.horizontalLayout_8.addWidget(self.label_coords_name)
        self.edit_coords_value = QtWidgets.QLineEdit(self.frame_coords)
        self.edit_coords_value.setStyleSheet("padding-left: 1px;\n"
"padding-right: 1px;")
        self.edit_coords_value.setObjectName("edit_coords_value")
        self.horizontalLayout_8.addWidget(self.edit_coords_value)
        self.label_coords_default_name = QtWidgets.QLabel(self.frame_coords)
        self.label_coords_default_name.setStyleSheet("padding: 0px;\n"
"margin-left: 5px")
        self.label_coords_default_name.setObjectName("label_coords_default_name")
        self.horizontalLayout_8.addWidget(self.label_coords_default_name)
        self.edit_coords_default_value = QtWidgets.QLineEdit(self.frame_coords)
        self.edit_coords_default_value.setStyleSheet("padding-left: 1px;\n"
"padding-right: 1px;")
        self.edit_coords_default_value.setObjectName("edit_coords_default_value")
        self.horizontalLayout_8.addWidget(self.edit_coords_default_value)
        self.horizontalLayout_7.addWidget(self.frame_coords)
        self.label_crs = QtWidgets.QLabel(self.frame_prev_bottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_crs.sizePolicy().hasHeightForWidth())
        self.label_crs.setSizePolicy(sizePolicy)
        self.label_crs.setStyleSheet("margin-left: 4px;")
        self.label_crs.setText("")
        self.label_crs.setObjectName("label_crs")
        self.horizontalLayout_7.addWidget(self.label_crs)
        self.verticalLayout_2.addWidget(self.frame_prev_bottom)
        self.tabWidget.addTab(self.tab_data_preview, "")
        self.tab_others = QtWidgets.QWidget()
        self.tab_others.setObjectName("tab_others")
        self.tabWidget.addTab(self.tab_others, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_add_raster.setText(_translate("MainWindow", "添加栅格\n"
"影像"))
        self.button_add_shp.setText(_translate("MainWindow", "添加矢量\n"
"数据"))
        self.button_help.setText(_translate("MainWindow", "帮助文档\n"
""))
        self.label.setText(_translate("MainWindow", "图层管理"))
        self.button_prev_clear.setText(_translate("MainWindow", "..."))
        self.button_prev_remove.setText(_translate("MainWindow", "..."))
        self.button_move.setText(_translate("MainWindow", "..."))
        self.button_zoom_in.setText(_translate("MainWindow", "..."))
        self.button_zoom_out.setText(_translate("MainWindow", "..."))
        self.button_refresh.setText(_translate("MainWindow", "..."))
        self.label_coords_name.setText(_translate("MainWindow", "EPSG:4326 坐标: "))
        self.label_coords_default_name.setText(_translate("MainWindow", "默认坐标: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data_preview), _translate("MainWindow", "数据预览"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_others), _translate("MainWindow", "其他"))
import rc_rc
