from PyQt5.QtWidgets import QLabel
from qgis._core import QgsMapSettings, QgsPointXY, QgsCoordinateReferenceSystem
from qgis._gui import QgsMapCanvas

from utils.raster import convert_to_wgs84


def set_status_crs(label: QLabel, canvas: QgsMapCanvas):
    canvas.mapSettings().destinationCrs().description()
    map_setting: QgsMapSettings = canvas.mapSettings()
    label.setText(f"坐标系: {map_setting.destinationCrs().description()}-{map_setting.destinationCrs().authid()}")


def set_status_xy(label_origin: QLabel, label_latlon: QLabel, canvas: QgsMapCanvas, point: QgsPointXY):
    label_origin.setText(f'{point.x():.0f}, {point.y():.0f}')
    convert_point = convert_to_wgs84(QgsCoordinateReferenceSystem(canvas.mapSettings().destinationCrs().authid()),
                                     point)
    label_latlon.setText(f'{convert_point.y():.5f}°, {convert_point.x():.5f}°')
    label_latlon.setCursorPosition(0)
