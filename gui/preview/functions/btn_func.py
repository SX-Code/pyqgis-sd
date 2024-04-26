from os.path import basename

from PyQt5.QtGui import QFont, QColor
from osgeo import gdal
from qgis._core import QgsRasterLayer, QgsProject, QgsVectorLayer, QgsPalLayerSettings, QgsTextFormat, Qgis, \
    QgsVectorLayerSimpleLabeling
from qgis._gui import QgsMapCanvas

import utils.fileUtil as FileUtil


def open_raster_file(main):
    """
    打开栅格文件
    :param main:
    :return:
    """
    # 选择文件
    filepath = FileUtil.select_single_file(main, 'GeoTiff(*.tif;*tiff;*TIF;*TIFF)', 'last_dir_raster')
    if filepath == '':
        return

    canvas: QgsMapCanvas = main.preview_canvas
    # 添加图层
    layer: QgsRasterLayer = QgsRasterLayer(filepath, basename(filepath), 'gdal')
    layer.dataProvider().setNoDataValue(1, 0)
    # 检查图层合法性
    if not layer.isValid():
        return False
    QgsProject.instance().addMapLayer(layer)
    # 绘图中是否已存在数据
    is_first_add_layer = len(canvas.layers()) == 0
    # 渲染栅格图像，渲染到最上层
    canvas.setLayers([layer] + canvas.layers())
    if is_first_add_layer:
        # 使用第一个图层的范围和crs，这里根据需要自定义
        canvas.setExtent(layer.extent())    # 更新范围
        canvas.setDestinationCrs(layer.crs())   # 更新crs
    canvas.freeze(False)
    canvas.setVisible(True)
    canvas.refresh()


def open_shp_file(main):
    filepath = FileUtil.select_single_file(main, '等深线数据(*.shp)', 'last_dir_contour_shp')
    if filepath == '' or not filepath.endswith('.shp'):
        return

    gdal.SetConfigOption('SHAPE_RESTORE_SHX', 'YES')
    layer = QgsVectorLayer(filepath, basename(filepath), 'ogr')

    if not layer.isValid():
        return False

    # 设置标注
    layer_setting = QgsPalLayerSettings()
    layer_setting.drawLabels = True
    layer_setting.fieldName = layer.fields()[1].name()

    # 文本样式设置
    text_format = QgsTextFormat()
    text_format.setFont(QFont("Arial", 12))
    text_format.setColor(QColor(255, 255, 255))
    layer_setting.setFormat(text_format)
    layer_setting.placement = Qgis.LabelPlacement.Line
    layer_setting.placementFlags = QgsPalLayerSettings.AboveLine

    layer.setLabelsEnabled(True)
    layer.setLabeling(QgsVectorLayerSimpleLabeling(layer_setting))
    layer.triggerRepaint(True)

    canvas: QgsMapCanvas = main.preview_canvas
    QgsProject.instance().addMapLayer(layer)
    canvas.setLayers([layer] + canvas.layers())
    canvas.setDestinationCrs(layer.crs())
    canvas.setExtent(layer.extent())
    canvas.refresh()


def slot_set_gis_tool(canvas: QgsMapCanvas, tool):
    canvas.setMapTool(tool)


def slot_refresh_canvas(canvas: QgsMapCanvas):
    """
    刷新画布
    :param canvas:
    :return:
    """
    for layer in canvas.layers():
        canvas.setExtent(layer.extent())
        canvas.setDestinationCrs(layer.crs())
        break
    canvas.refreshAllLayers()
