from src.components.home.child.homeUpdate.ui.homeUpdate import Ui_Form
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,QScrollArea,QFileDialog,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from API.homeindexCallAPI import *

from qfluentwidgets import (RoundMenu,Action)
from qfluentwidgets import FluentIcon as FIF

class HomeUpdateWindow(QWidget,Ui_Form):
    def __init__(self,homeUI):
        self.homeUI = homeUI
        super(HomeUpdateWindow, self).__init__()
        self.setupUi(self)

        # 监听查询输入框内容
        self.watchSearchInputEdit()

        # 生成ID按钮
        self.pushButton.clicked.connect(self.pushButton_click)

        # 添加下拉选项，标签
        self.menu = RoundMenu(parent=self)
        self.menu.view.itemClicked.connect(self.menu_clicked)
        alltab_list = []
        # 获取所有的标签,homeUI包在项目启动时已经完成初始化
        for package in self.homeUI.packages:
            if package['label'] in alltab_list:
                continue
            alltab_list.append(package['label'])
        for label in alltab_list:
            self.menu.addAction(Action(FIF.LABEL, label))
        self.pushButton_2.setMenu(self.menu)



    def watchSearchInputEdit(self):
        # 监听查询输入框内容
        self.lineEdit.textChanged.connect(self.watchSearchInputTitle)

    def watchSearchInputTitle(self,text):
        # 监听查询输入框内容
        # 查询
        this_package = {}
        if text:
            this_package = Request_search_fileID_package(text, self.homeUI.packages)
        if this_package:
            # 对已经存在的fileID做全局数据加载
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

    def pushButton_click(self):
        create_fileID = create_uuid()
        # 表单输入自动化设置
        self.lineEdit.setText(create_fileID)
        self.lineEdit_3.setText('')
        self.lineEdit_2.setText('')


    def menu_clicked(self,index):
        self.lineEdit_3.setText(index.text())


