# -*- coding: utf-8 -*-
from src.manage import Manages_running
from PySide6.QtWidgets import QApplication,QMainWindow
import sys,time
# from qfluentwidgets import FluentStyleSheet

class admin_windows(object):
    def __init__(self,app, example):
        self.example = example
        self.app = app

    def close_example(self):

        print('系统关闭页面!')
        # self.example.close()
        # self.app.quit()  # 显式退出事件循环
        # QTimer.singleShot(5000, self.example.close())
        # QTimer.singleShot(5000, self.app.quit())

def startWinwos(app,example):
    this_show = example
    example = admin_windows(app=app, example=this_show)
    this_show.destroyed.connect(example.close_example)  # 系统自动关闭监听
    this_show.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 1. 定义全局滚动条样式（Fluent 风格）
    app.setStyleSheet("""
        /* 垂直滚动条 */
        QScrollBar:vertical {
            border: none;
            background: #f3f3f3;
            width: 12px;
            margin: 0;
        }

        QScrollBar::handle:vertical {
            background: #c8c8c8;
            border-radius: 4px;
            min-height: 20px;
        }

        QScrollBar::handle:vertical:hover {
            background: #a6a6a6;
        }

        QScrollBar::handle:vertical:pressed {
            background: #606060;
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            background: none;
            height: 0px;
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }

        /* 水平滚动条（类似垂直滚动条） */
        QScrollBar:horizontal {
            border: none;
            background: #f3f3f3;
            height: 12px;
            margin: 0;
        }

        QScrollBar::handle:horizontal {
            background: #c8c8c8;
            border-radius: 4px;
            min-width: 20px;
        }

        QScrollBar::handle:horizontal:hover {
            background: #a6a6a6;
        }

        QScrollBar::handle:horizontal:pressed {
            background: #606060;
        }
    """)
    # app.setQuitOnLastWindowClosed(False)  # 关闭窗口不会自动退出

    example = Manages_running()
    example_dict = example.start()

    startWinwos(app, example_dict['home'])
    sys.exit(app.exec())