from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QColor
from qgis._core import QgsCoordinateReferenceSystem, QgsLayerTreeModel, QgsProject
from qgis._gui import QgsMapCanvas, QgsMapToolPan, QgsMapToolZoom, QgsLayerTreeView, QgsLayerTreeMapCanvasBridge

from gui.preview.functions import open_raster_file, open_shp_file, slot_set_gis_tool, slot_refresh_canvas
from utils.help_dialog import show_help_dialog


def load_preview(main):
    """
    装载预览界面
    :param main:
    :return:
    """
    # 初始化界面变量
    declaring_variable(main)
    # 初始化界面布局
    init_preview(main)
    # 初始化 QGIS
    init_qgis_map(main)
    # 绑定方法
    bind_func(main)


def declaring_variable(main):
    main.preview_canvas = None  # 图层显示器
    main.preview_tool_pan = None
    main.preview_tool_zoom_in = None
    main.preview_tool_zoom_out = None


def init_preview(main):
    # 设置splitter缩放因子
    main.ui.splitter.setStretchFactor(0, 3)
    main.ui.splitter.setStretchFactor(1, 5)


def init_qgis_map(main):
    # 初始化画布
    main.preview_canvas = QgsMapCanvas()
    main.preview_canvas.setDestinationCrs(QgsCoordinateReferenceSystem("EPSG:4326"))
    main.preview_canvas.setCanvasColor(Qt.white)
    main.preview_canvas.enableAntiAliasing(True)
    main.preview_canvas.setFocus()
    main.preview_canvas.setParallelRenderingEnabled(True)
    # 添加到布局中
    main.ui.preview_qgis_map.addWidget(main.preview_canvas)

    # 初始化工具
    main.preview_tool_pan = QgsMapToolPan(main.preview_canvas)
    main.preview_tool_zoom_in = QgsMapToolZoom(main.preview_canvas, False)
    main.preview_tool_zoom_out = QgsMapToolZoom(main.preview_canvas, True)
    # 默认使用移动工具
    main.preview_canvas.setMapTool(main.preview_tool_pan)

    # 初始化图层管理器
    # 创建图层树视图，然后添加到
    main.layerTreeView = QgsLayerTreeView(main)
    main.ui.layout_prev_layers.addWidget(main.layerTreeView)
    # 树节点
    main.model = QgsLayerTreeModel(QgsProject.instance().layerTreeRoot(), main)
    main.model.setFlag(QgsLayerTreeModel.AllowNodeRename)  # 允许图层节点重命名
    main.model.setFlag(QgsLayerTreeModel.AllowNodeReorder)  # 允许图层拖拽排序
    main.model.setFlag(QgsLayerTreeModel.AllowNodeChangeVisibility)  # 允许改变图层节点可视性
    main.model.setFlag(QgsLayerTreeModel.ShowLegendAsTree)  # 展示图例
    main.model.setAutoCollapseLegendNodes(10)  # 当节点数大于等于10时自动折叠
    main.layerTreeView.setModel(main.model)
    # 4 建立图层树与地图画布的桥接
    main.layerTreeBridge = QgsLayerTreeMapCanvasBridge(QgsProject.instance().layerTreeRoot(), main.preview_canvas, main)


def bind_func(main):
    _ui = main.ui
    # 添加栅格数据按钮绑定方法
    _ui.button_add_raster.clicked.connect(lambda self: open_raster_file(main))
    # 添加矢量数据按钮绑定方法
    _ui.button_add_shp.clicked.connect(lambda self: open_shp_file(main))
    # 绑定工具方法
    _ui.button_move.clicked.connect(lambda self: slot_set_gis_tool(main.preview_canvas, main.preview_tool_pan))
    _ui.button_zoom_in.clicked.connect(lambda self: slot_set_gis_tool(main.preview_canvas, main.preview_tool_zoom_in))
    _ui.button_zoom_out.clicked.connect(lambda self: slot_set_gis_tool(main.preview_canvas, main.preview_tool_zoom_out))
    _ui.button_refresh.clicked.connect(lambda self: slot_refresh_canvas(main.preview_canvas))
    _ui.button_help.clicked.connect(lambda self: show_help_dialog(main, 'preview', '数据预览'))


def switch_theme(main, theme):
    canvas_color = Qt.white if main.theme == 'light' else QColor(30, 31, 34)
    main.preview_canvas.setCanvasColor(canvas_color)

    if 'dark' == theme:
        main.layerTreeView.setStyleSheet("background-color: rgb(30, 31, 34)")
        main.ui.button_prev_clear.setIcon(QIcon(":/icon/action_trash_dark"))
        main.ui.button_prev_remove.setIcon(QIcon(":/icon/action_remove_dark"))
    else:
        main.layerTreeView.setStyleSheet("background-color: white")
        main.ui.button_prev_clear.setIcon(QIcon(":/icon/action_trash_light"))
        main.ui.button_prev_remove.setIcon(QIcon(":/icon/action_remove_light"))
