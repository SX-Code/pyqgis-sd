import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWidgets import QDialog, QVBoxLayout


class CustomHelpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

    def set_theme(self, theme, bg_color):
        self.setStyleSheet(bg_color)

    def set_title(self, title):
        self.setWindowTitle(title)


class CustomWebView(QWebView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('font-family: Microsoft YaHei')
        self.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        self.page().linkClicked.connect(self.linkClicked)

    def linkClicked(self, url):
        QDesktopServices.openUrl(url)


def refresh_help_dialog(help_dialog, theme, name=None):
    if help_dialog is None:
        return
    bg_color = 'background: white' if theme == 'light' else 'background: #2B2D30'
    help_dialog.set_theme(theme, bg_color)
    web_view: QWebView = help_dialog.layout().itemAt(0).widget()
    web_view.setStyleSheet(bg_color)
    if name is not None:
        url = QUrl.fromLocalFile(f'{os.path.dirname(sys.argv[0])}/markdown/{name}.html')
        web_view.load(url)
    else:
        web_view.reload()


def show_help_dialog(main, name, title):
    bg_color = 'background: white' if main.theme == 'light' else 'background: #2B2D30'
    if main.help_dialog is None:
        main.help_dialog = CustomHelpDialog(main)
        main.help_dialog.set_title(f'{title}—帮助文档')
        # add a label to dialog
        web_view = CustomWebView()
        web_view.setStyleSheet(bg_color)
        main.help_dialog.set_theme(main.theme, bg_color)
        layout = QVBoxLayout()
        layout.setContentsMargins(4, 34, 4, 0)
        layout.addWidget(web_view)
        main.help_dialog.setLayout(layout)

        url = QUrl.fromLocalFile(f'{os.path.dirname(sys.argv[0])}/markdown/{name}.html')
        web_view.load(url)
        main.help_dialog.resize(820, 700)
    else:
        main.help_dialog.set_title(f'{title}—帮助文档')
        # 主题由js从文件中获取，需要刷新
        refresh_help_dialog(main.help_dialog, main.theme, name)

    main.help_dialog.show()