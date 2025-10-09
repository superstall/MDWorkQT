# -*- coding: utf-8 -*-
import sys

from src.components.home.views import HomeWindow


class Manages_running():
    def __init__(self):
        super().__init__()
        # 国际化 汉化
        # translator = QTranslator()
        # translator.load(QLocale.system(),":/i18n/gallery.zh_")
        # app.installTranslator(translator)
        # LoginsWindow().show()
    def start(self):
        return {
            "home":HomeWindow()
        }




