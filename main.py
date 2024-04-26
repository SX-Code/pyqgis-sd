import os
import sys

from PyQt5.QtCore import QSettings, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow
from qgis._core import QgsApplication

from ui.mainwin import Ui_MainWindow
import gui as GUI
from utils import QSSLoader
from utils.help_dialog import refresh_help_dialog


class PyQgisSEApp(QMainWindow, Ui_MainWindow):
    def __init__(self, app: QgsApplication):
        super(PyQgisSEApp, self).__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QSettings('PyQgisSEApp')
        # 装载模块
        GUI.GUIPreview.load_preview(self)

        # 加载主题文件
        self.help_dialog = None  # 帮助Dialog
        self.theme = 'light'
        self.load_qss()

    def load_qss(self):
        # 从配置中加载主题选项
        self.theme = self.settings.value('theme', 'dark')
        self.switch_theme()

    def slot_switch_theme(self):
        """
        切换主题插槽，用于绑定按钮
        """
        self.theme = 'dark' if self.theme == 'light' else 'light'
        # 写入配置
        self.settings.setValue('theme', self.theme)
        self.switch_theme()

    def switch_theme(self):
        # 切换主题文件
        file = f"{os.path.dirname(sys.argv[0])}/ui/style/{self.theme}/theme.qss"
        qss = QSSLoader(file).load()
        self.ui.centralwidget.setStyleSheet(qss)
        # 写入主题信息到文件
        self.save_theme_file()
        # 刷新帮助Dialog
        refresh_help_dialog(self.help_dialog, self.theme)

        # 数据预览页面主题切换
        GUI.GUIPreview.switch_theme(self, self.theme)

    def save_theme_file(self):
        try:
            path = f'{os.path.dirname(sys.argv[0])}/markdown/theme.json'
            f = open(path, 'w', encoding='utf-8')
            f.write(f"theme='{self.theme}'")
            f.close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # 第二个参数为是否启用 GUI
    qgs = QgsApplication([], False)
    # 初始化 QGIS
    qgs.initQgis()
    app = PyQgisSEApp(qgs)
    app.show()

    qgs.exec_()
    qgs.exitQgis()
