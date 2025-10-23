from src.components.home.child.homeIndex.ui.homeindex import Ui_Form
from PySide6.QtWidgets import QWidget
from API.homeindexCallAPI import *
from API.util import *
from markdown import markdown
from PySide6.QtCore import Qt
from globalUtile import *

from PySide6.QtWidgets import QVBoxLayout, QWidget,QLabel
from qfluentwidgets import (ListWidget,InfoBar,InfoBarPosition,ScrollBar)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,QScrollArea,QFileDialog,QGraphicsScene,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,QGraphicsTextItem,
    QVBoxLayout, QWidget)

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

import re
class HomeIndexWindow(QWidget,Ui_Form):
    def __init__(self,homeUI):
        self.homeUI = homeUI
        super(HomeIndexWindow, self).__init__()
        self.setupUi(self)
        # 初始化获取全部文档包：每次重载列表都要更新这个变量
        self.packages_fileID = {}
        # 读取文档包存放的fileID列表
        self.this_packages_fileID = []
        # 初始化显示项目目录
        self.label.setText("当前读取项目位置：" + str(self.homeUI.DOCUMENTPATH))
        # 设置鼠标选中
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label.setWordWrap(True)  # 启用自动换行
        self.lineEdit.setPlaceholderText("按文章标题搜索...")  # 设置 placeholder 文本

        # 打开按钮
        self.pushButton_3.clicked.connect(self.pushButton_3_click)
        # 初始化文档包按钮
        self.pushButton_6.clicked.connect(self.pushButton_6_click)

        # 初始化列表内容
        self.init_listWidget()
        # 监听查询输入框内容
        self.watchSearchInputEdit()

    # menu公共模块组件编写
    def menu_labelANDnameShow_model(self,modelname,labelsetText,listWidgetList):
        # 展示同标签下的文章标题名称
        # modelname用来设置唯一的组件名, 规则：user0001

        # 声明主widget框架
        self.widget_menu_homeindex = QWidget(self.widget_10)
        self.widget_menu_homeindex.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)  # 高度自适应
        self.widget_menu_homeindex.setObjectName(u"widget_%s"%(str(modelname)))

        # 声明布局方式(必须)
        self.verticalLayout_menu_homeindex = QVBoxLayout(self.widget_menu_homeindex)
        self.verticalLayout_menu_homeindex.setObjectName(u"verticalLayout_%s"%(str(modelname)))

        # 声明唯一标签
        self.label_menu_homeindex = QLabel(self.widget_menu_homeindex)
        self.label_menu_homeindex.setObjectName(u"label_%s"%(str(modelname)))
        self.label_menu_homeindex.setText(labelsetText+":")
        self.label_menu_homeindex.setMaximumSize(QSize(16777215, 15))
        self.label_menu_homeindex.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        # 声明唯一列表
        self.listWidget_menu_homeindex = ListWidget(self.widget_menu_homeindex)
        self.listWidget_menu_homeindex.setObjectName(u"listWidget_%s"%(str(modelname)))
        self.listWidget_menu_homeindex.setMaximumSize(QSize(280, 16777215))
        self.listWidget_menu_homeindex.addItems(listWidgetList)
        # 关键修改：禁用列表控件的滚动条
        self.listWidget_menu_homeindex.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_menu_homeindex.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 监听列表点击
        self.listWidget_menu_homeindex.currentRowChanged.connect(self.watchListWidgetcurrentRowChanged)
        self.listWidget_menu_homeindexs[u"listWidget_%s"%(str(modelname))] = self.listWidget_menu_homeindex
        # 让子控件从顶部开始排列
        self.verticalLayout_6.setAlignment(Qt.AlignTop)
        self.verticalLayout_4.setSizeConstraint(QVBoxLayout.SetFixedSize)

        # 动态计算列表高度
        total_height = sum(self.listWidget_menu_homeindex.sizeHintForRow(i) for i in range(self.listWidget_menu_homeindex.count()))
        self.listWidget_menu_homeindex.setFixedHeight(total_height + 1)  # +1像素补偿

        # 载入组件
        self.verticalLayout_menu_homeindex.setAlignment(Qt.AlignTop)  # 让子控件从顶部开始排列
        self.verticalLayout_menu_homeindex.addWidget(self.label_menu_homeindex)
        self.verticalLayout_menu_homeindex.addWidget(self.listWidget_menu_homeindex)
        self.verticalLayout_4.addWidget(self.widget_menu_homeindex)
        return self.widget_menu_homeindex.sizeHint().height()

    def pushButton_6_click(self):
        # 初始化package
        self.homeUI.packages = Request_init_package(self.homeUI.DOCUMENTPATH)

        # 初始化列表内容
        self.watchSearchInputTitle(self.lineEdit.text())
        InfoBar.success(
            title='操作成功！',
            content="package初始化成功",
            orient=Qt.Orientation.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self
        )


    def pushButton_3_click(self):
        # 选择目标项目文件
        # 打开文件夹选择对话框
        folder_path = QFileDialog.getExistingDirectory(
            self,  # 父窗口
            "选择文件夹",  # 对话框标题
            ""  # 初始目录（空表示当前工作目录）
        )

        if folder_path:  # 如果用户选择了文件夹（而不是取消）
            # 可以在这里调用回调函数或直接处理路径
            self.pushButton_3_click_on_folder_selected(folder_path)
    def pushButton_3_click_on_folder_selected(self,folder_path):
        self.label.setText("当前读取项目位置：%s"%(folder_path))
        self.homeUI.DOCUMENTPATH = folder_path
        # 初始化package
        self.homeUI.packages = Request_init_package(self.homeUI.DOCUMENTPATH)
        # 初始化列表内容
        self.init_listWidget()


    def menu_clear_verticalLayout_4(self):
        # 清空布局
        while self.verticalLayout_4.count():
            item = self.verticalLayout_4.takeAt(0)

            # 处理小部件
            if item.widget():
                widget = item.widget()
                widget.setParent(None)  # 解除父子关系
                widget.deleteLater()  # 标记删除

            # 处理嵌套布局
            elif item.layout():
                nested_layout = item.layout()
                # 递归清空嵌套布局
                while nested_layout.count():
                    nested_item = nested_layout.takeAt(0)
                    if nested_item.widget():
                        nested_item.widget().deleteLater()
                    else:
                        nested_layout.removeItem(nested_item)
                self.verticalLayout_4.removeItem(item)

            # 处理其他布局项（如间距项）
            else:
                self.verticalLayout_4.removeItem(item)

    def init_listWidget(self):
        # 初始化列表内容
        self.package_groups = {}
        for packget in self.homeUI.packages:
            if packget['label'] in self.package_groups.keys():
                self.package_groups[packget['label']].append(packget)
            else:
                self.package_groups[packget['label']] = [packget]
        #初始化menu
        self.init_menu()

    def init_menu(self):
        # 初始化menu组件 使用前请准备好已经分组好的self.package_groups数据
        # 清空布局
        self.menu_clear_verticalLayout_4()
        # 唯一化项目名称参数
        self.homeindex_menu_num = 0
        # listwidget收集存储
        self.listWidget_menu_homeindexs = {}
        # 清空当前显示
        self.packages_fileID = {}
        for package_label in self.package_groups.keys():
            self.homeindex_menu_num +=1
            namelist = [package['name'] for package in self.package_groups[package_label]]
            self.packages_fileID[package_label] = [package['fileID'] for package in self.package_groups[package_label]]
            self.menu_labelANDnameShow_model(modelname='menu%salltext%s'%(str(package_label),str(self.homeindex_menu_num)),labelsetText=package_label,listWidgetList=namelist)



    def watchSearchInputEdit(self):
        # 监听查询输入框内容
        self.lineEdit.textChanged.connect(self.watchSearchInputTitle)

    def watchSearchInputTitle(self,text):
        # 监听查询输入框内容
        # 初始化列表内容
        self.package_groups = {}
        if len(text) == 0:
            for packget in self.homeUI.packages:
                if packget['label'] in self.package_groups.keys():
                    self.package_groups[packget['label']].append(packget)
                else:
                    self.package_groups[packget['label']] = [packget]
            # 重置menu组件
            self.init_menu()


        else:
            # 查询
            packageList = Request_search_package(text,self.homeUI.packages)
            # 清空当前数据
            self.package_groups = {}
            # 更新
            for packget in packageList:
                if packget['label'] in self.package_groups.keys():
                    self.package_groups[packget['label']].append(packget)
                else:
                    self.package_groups[packget['label']] = [packget]
            # 重置menu组件
            self.init_menu()

    def watchListWidgetcurrentRowChanged(self,currentRow):
        # 监听列表点击
        if currentRow == -1:  # 如果取消选中（如点击空白处）
            return

        # 取消其他 QListWidget 的选中状态
        clicked_list = self.sender()
        for name, list_widget in self.listWidget_menu_homeindexs.items():
            if list_widget is not clicked_list:
                list_widget.setCurrentRow(-1)  # -1 表示取消选中

        # 触发删除，提前提取数据(场景：被删除内容重新选中标签页后依旧可以看，只有重新初始化页面或者menu组件才会消失)
        old_packages = []
        if self.homeUI.isChange_tall_homeindex_package and len(self.this_packages_fileID):
            self.homeUI.isChange_tall_homeindex_package = False
            #触发删除后要检查的动作
            new_fileIDs = [packget['fileID'] for packget in self.homeUI.packages]
            for packget in self.homeUI.packages:
                if packget['label'] in self.package_groups.keys():
                    r_package = [p for p in self.package_groups[packget['label']] if p['fileID'] not in new_fileIDs]
                    old_packages+=r_package
            self.homeUI.packages += old_packages
            #出发新增或修改后要检查的动作


        # 提取选中数据下label下的数据
        # 正则处理
        print_label = clicked_list.objectName()
        print_label = re.sub(r'\d+$', '', print_label)
        print_label  = print_label[10:-7]
        for labelname in self.packages_fileID.keys():
            if labelname in print_label:
                self.this_packages_fileID = self.packages_fileID[labelname]

        this_fileID = self.this_packages_fileID[currentRow]
        this_package = Request_search_fileID_package(this_fileID,self.homeUI.packages)
        # 这俩个主要用来判定当前显示文件是否存在，不存在label_10发出警告，组件位于self.homeindexWindow.label_10
        self.homeUI.homeindexWindow_this_fileID = this_fileID
        self.homeUI.homeindexWindow_this_package = this_package
        self.label_10.setText('')
        try:
            file_content = read_file(this_package['filepath'])
            fileTime = get_file_open_time(this_package['filepath'])
            # 保障被删除的内容还可以被点击观看
            for p_index in range(len(self.homeUI.packages)):
                if self.homeUI.packages[p_index]['fileID'] == this_fileID:
                    self.homeUI.packages[p_index]['file_content'] = file_content
                    self.homeUI.packages[p_index]['fileTime'] = fileTime
        except Exception as e:
            file_content = ""
            fileTime = ["",""]
            # 读取错误时尝试从内存提取
            for p_index in range(len(self.homeUI.packages)):
                if this_fileID == self.homeUI.packages[p_index]['fileID']:
                    if "file_content" in self.homeUI.packages[p_index]:
                        file_content = self.homeUI.packages[p_index]['file_content']
                    if "fileTime" in self.homeUI.packages[p_index]:
                        fileTime = self.homeUI.packages[p_index]['fileTime']
            self.label_10.setText('警告：该文件已被删除')


        # 内容展示
        self.label_2.setText('文件ID：' + str(this_package['fileID']))
        #设置鼠标选中
        self.label_2.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_2.setWordWrap(True)  # 启用自动换行

        self.label_3.setText('包名：' + str(this_package['mddirname']))
        #设置鼠标选中
        self.label_3.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_3.setWordWrap(True)  # 启用自动换行

        self.label_4.setText('修改时间：' + str(fileTime[0]))
        #设置鼠标选中
        self.label_4.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_4.setWordWrap(True)  # 启用自动换行

        self.label_5.setText('最后访问时间：' + str(fileTime[1]))
        #设置鼠标选中
        self.label_5.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_5.setWordWrap(True)  # 启用自动换行

        self.label_6.setText('文件位置：' + str(this_package['filepath']))
        #设置鼠标选中
        self.label_6.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_6.setWordWrap(True)  # 启用自动换行

        self.label_7.setText('是否开启局域网共享：' + str(this_package['isLANshared']))
        #设置鼠标选中
        self.label_7.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_7.setWordWrap(True)  # 启用自动换行

        self.label_9.setText('所属标签：' + str(this_package['label']))
        # 设置鼠标选中
        self.label_9.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_9.setWordWrap(True)  # 启用自动换行

        html_content = markdown(file_content)
        scene = QGraphicsScene()
        self.graphicsView.setScene(scene)
        # 创建 QGraphicsTextItem 并设置 HTML
        text_item = QGraphicsTextItem()
        text_item.setHtml(html_content)
        text_item.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        scene.addItem(text_item)

        self.graphicsView.resizeEvent = lambda _: self.resize_content()

    # 4. 动态调整缩放
    def resize_content(self):
        # 获取当前视图尺寸
        width = self.graphicsView.width()
        height = self.graphicsView.height()

        # 计算缩放比例（基准尺寸 600x400）
        scale_factor = min(width / 500, height / 300) * 0.8

        # 应用缩放
        self.graphicsView.resetTransform()
        self.graphicsView.scale(scale_factor, scale_factor)




