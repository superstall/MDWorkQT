from src.components.home.child.homeDelete.ui.homeDelete import Ui_Form
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,QScrollArea,QFileDialog,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from API.homeindexCallAPI import *
from qfluentwidgets import (ListWidget,InfoBar,InfoBarPosition,ScrollBar)
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

class HomeDeleteWindow(QWidget,Ui_Form):
    def __init__(self,homeUI):
        self.homeUI = homeUI
        super(HomeDeleteWindow, self).__init__()
        self.setupUi(self)
        # 初始化package
        self.package_fileID = [this_package['fileID'] for this_package in self.homeUI.packages]
        self.pushButton.setText('删除')
        self.lineEdit.setPlaceholderText("请输入文档fileID..")  # 设置 placeholder 文本
        self.label.setText("当前操作目录：%s"%(str(self.homeUI.DOCUMENTPATH)))
        #设置鼠标选中
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label.setWordWrap(True)  # 启用自动换行
        # 删除按钮
        self.pushButton.clicked.connect(self.pushButton_click)

        # 监听查询输入框内容
        self.watchDeleteInputEdit()

    def watchDeleteInputEdit(self):
        # 监听查询输入框内容
        self.lineEdit.textChanged.connect(self.watchDeleteInputfileID)
    def watchDeleteInputfileID(self,text):
        # 初始化package
        self.package_fileID = [this_package['fileID'] for this_package in self.homeUI.packages]

        if text in self.package_fileID:
            self.label_2.setText('')
        else:
            self.label_2.setText('fileID不存在！')

    def pushButton_click(self):
        # 表单验证
        if not self.lineEdit.text():
            InfoBar.error(
                title='操作失败！',
                content="表单提交错误！请检查表单是否有未填写！",
                orient=Qt.Orientation.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP_RIGHT,
                # position='Custom',   # NOTE: use custom info bar manager
                duration=2000,
                parent=self
            )
            return

        # 获取输入的文本
        isTrue = Request_delete_package(self.lineEdit.text(), self.homeUI.packages)
        if isTrue:
            InfoBar.success(
                title='操作成功！',
                content="删除成功fileID:%s"%(self.lineEdit.text()),
                orient=Qt.Orientation.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP_RIGHT,
                # position='Custom',   # NOTE: use custom info bar manager
                duration=2000,
                parent=self
            )
        # 更新
        self.homeUI.packages = [p for p in self.homeUI.packages if p['fileID'] != self.lineEdit.text()]
        self.homeUI.isChange_tall_homeindex_package = True
        # 这俩个主要用来判定当前显示文件是否存在，不存在label_10发出警告，组件位于self.homeindexWindow.label_10
        self.homeUI.HomeDeleteWindow_this_fileID = self.lineEdit.text()