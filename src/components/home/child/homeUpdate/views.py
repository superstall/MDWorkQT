from src.components.home.child.homeUpdate.ui.homeUpdate import Ui_Form
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,QScrollArea,QFileDialog,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from API.homeindexCallAPI import *

from qfluentwidgets import (RoundMenu,Action)
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import (ListWidget,InfoBar,InfoBarPosition,ScrollBar)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,QScrollArea,QFileDialog,QGraphicsScene,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,QGraphicsTextItem,
    QVBoxLayout, QWidget)
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtCore import Qt, QTimer,QSize
from PySide6.QtCore import Qt, QRectF
class HomeUpdateWindow(QWidget,Ui_Form):
    def __init__(self,homeUI):
        self.homeUI = homeUI
        super(HomeUpdateWindow, self).__init__()
        self.setupUi(self)

        # 初始化组件内容
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        # 创建 QGraphicsTextItem 并设置 HTML
        self.text_item = QGraphicsTextItem()

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

        # 实时预览设置
        self.preview_timer = QTimer()
        self.preview_timer.setInterval(50)
        self.preview_timer.timeout.connect(self.update_preview)
        self.textEdit.textChanged.connect(self.on_text_changed)

        # 保存按钮
        self.pushButton_3.clicked.connect(self.pushButton3_click)

    def pushButton3_click(self):
        # 表单验证
        if not self.lineEdit.text() or not self.lineEdit_2.text() or not self.lineEdit_3.text():
            InfoBar.error(
                title='保存失败！',
                content="表单提交错误！请检查表单是否有未填写！",
                orient=Qt.Orientation.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP_RIGHT,
                # position='Custom',   # NOTE: use custom info bar manager
                duration=2000,
                parent=self
            )
            return

        # 保存md
        isTrue = Request_update_package(self.lineEdit.text(),self.textEdit.toPlainText(), self.homeUI.packages,self.lineEdit_2.text(),self.lineEdit_3.text(),self.homeUI)
        if isTrue:
            InfoBar.success(
                title='保存成功！',
                content="成功保存到文件！",
                orient=Qt.Orientation.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP_RIGHT,
                # position='Custom',   # NOTE: use custom info bar manager
                duration=2000,
                parent=self
            )
        # 给index页面提示更新信号
        self.homeUI.isChange_tall_homeindex_package = True
        self.isChange_tall_home = True


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
                            break

            # 显示文件内容
            self.textEdit.setText(file_content)

            html_content = markdown(file_content)
            self.text_item.setHtml(html_content)
            self.text_item.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
            self.scene.addItem(self.text_item)

            # self.graphicsView.resizeEvent = lambda _: self.resize_content()




        else:
            # 对新建的数据不做校验
            pass

    def update_preview(self):
        """更新预览内容"""
        self.preview_timer.stop()
        md_text = self.textEdit.toPlainText()

        # 渲染Markdown为HTML
        html = markdown(
            md_text,
            extensions=[
                'markdown.extensions.fenced_code',
                'markdown.extensions.tables',
                'markdown.extensions.extra'
            ]
        )

        # 加载到预览视图
        html_content = markdown(html)
        self.text_item.setHtml(html_content)
        self.text_item.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard)
        self.scene.addItem(self.text_item)



        # self.graphicsView.resizeEvent = lambda _: self.resize_content()

    def on_text_changed(self):
        """文本改变时启动预览更新"""
        if not self.preview_timer.isActive():
            self.preview_timer.start()

    def pushButton_click(self):
        create_fileID = create_uuid()
        # 表单输入自动化设置
        self.lineEdit.setText(create_fileID)
        self.lineEdit_3.setText('')
        self.lineEdit_2.setText('')
        # 清空内容
        self.textEdit.setText('')


    def menu_clicked(self,index):
        # 可选标签-填入表单
        self.lineEdit_3.setText(index.text())

    # 4. 动态调整缩放
    def resize_content(self):
        # 这里需要优化，尽量不让用户来操作，
        # 当内容宽度溢出窗口需要缩小内容尺度，给个按钮，让用户自己选择显示方式
        # 获取当前视图尺寸
        width = self.graphicsView.width()
        height = self.graphicsView.height()

        # 计算缩放比例（基准尺寸 600x400）
        scale_factor = min(width / 1920, height / 1200) * 1

        # 应用缩放
        self.graphicsView.resetTransform()
        self.graphicsView.scale(scale_factor, scale_factor)


    def on_text_changed(self):
        """文本改变时启动预览更新"""
        if not self.preview_timer.isActive():
            self.preview_timer.start()