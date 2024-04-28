from qgis._core import QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsCoordinateTransformContext, QgsPointXY


def convert_to_wgs84(src_crs, point: QgsPointXY):
    """
    转换到 EPSG:4326 坐标系
    :param src_crs: 原始坐标系
    :param point:
    :return:
    """
    dest_crs = QgsCoordinateReferenceSystem("EPSG:4326")
    crs_tras = QgsCoordinateTransform(src_crs, dest_crs, QgsCoordinateTransformContext())
    return crs_tras.transform(point)
