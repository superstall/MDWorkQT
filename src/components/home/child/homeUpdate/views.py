from src.components.home.child.homeUpdate.ui.homeUpdate import Ui_Form
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,QScrollArea,QFileDialog,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from API.homeindexCallAPI import *


class HomeUpdateWindow(QWidget,Ui_Form):
    def __init__(self,homeUI):
        self.homeUI = homeUI
        super(HomeUpdateWindow, self).__init__()
        self.setupUi(self)

        # 监听查询输入框内容
        self.watchSearchInputEdit()


    def watchSearchInputEdit(self):
        # 监听查询输入框内容
        self.lineEdit.textChanged.connect(self.watchSearchInputTitle)

    def watchSearchInputTitle(self,text):
        # 监听查询输入框内容
        # 查询
        packageList = Request_search_fileID_package(text, self.homeUI.packages)
        if len(packageList):
            # 对已经存在的fileID做全局数据加载
            this_package = packageList[0]
            # 载入标签
            self.lineEdit_3.setText(this_package['label'])
            # 载入标题
            self.lineEdit_2.setText(this_package['name'])
            # 载入内容
            this_fileID = this_package['fileID']
            try:
                file_content = read_file(this_package['filepath'])
                fileTime = get_file_open_time(this_package['filepath'])
                # 保障被删除的内容还可以被点击观看
                for p_index in range(len(self.homeUI.packages)):
                    if self.homeUI.packages[p_index]['fileID'] == this_fileID:
                        self.homeUI.packages[p_index]['file_content'] = file_content
                        self.homeUI.packages[p_index]['fileTime'] = fileTime
            except Exception as e:
                # 读取错误时尝试从内存提取
                for p_index in range(len(self.homeUI.packages)):
                    if this_fileID == self.homeUI.packages[p_index]['fileID']:
                        if "file_content" in self.homeUI.packages[p_index]:
                            file_content = self.homeUI.packages[p_index]['file_content']

        else:
            # 对新建的数据不做校验
            pass
