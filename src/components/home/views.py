from src.components.home.ui.home import Ui_Form
from PySide6.QtWidgets import QWidget, QVBoxLayout

from src.components.home.child.homeIndex.views import HomeIndexWindow
from src.components.home.child.homeUpdate.views import HomeUpdateWindow
from src.components.home.child.homeDelete.views import HomeDeleteWindow
from API.homeindexCallAPI import *
class HomeWindow(QWidget,Ui_Form):
    def __init__(self):
        super(HomeWindow, self).__init__()
        # 实例化
        self.setupUi(self)
        # 默认文档根目录
        self.DOCUMENTPATH = str(get_RootDirName()) + '\markdownfile'  # 动态目录
        # 初始化packages
        self.packages = Request_init_package(self.DOCUMENTPATH)
        # 是否更新package
        self.isChange_tall_homeindex_package = False
        # 默认首先显示首页 -主页
        self.tabWidget.setCurrentIndex(0)
        # 实例化子页面
        self.homeindexWindow = HomeIndexWindow(self)   #主页
        # 这俩个主要用来判定当前显示文件是否存在，不存在label_10发出警告，组件位于self.homeindexWindow.label_10
        self.homeindexWindow_this_package = {}
        self.homeindexWindow_this_fileID = ""

        self.HomeUpdateWindow = HomeUpdateWindow(self)  # 更新页
        self.HomeDeleteWindow = HomeDeleteWindow(self) #删除页
        self.HomeDeleteWindow_this_fileID = ""
        self.isChange_tall_home = False # 更新动作需要home页面提前配合


        # 动态声明子页面
        self.HomeWindow_child_widget_1 = QWidget()
        self.HomeWindow_child_widget_1.setObjectName(u"HomeWindow_child_widget_1") #唯一ID
        # 声明布局
        self.HomeWindow_verticalLayout_1 = QVBoxLayout(self.tab)
        self.HomeWindow_verticalLayout_1.setObjectName(u"HomeWindow_verticalLayout_1") #唯一ID
        # 布局内添加子页面
        self.HomeWindow_verticalLayout_1.addWidget(self.homeindexWindow)

        # 动态声明子页面
        self.HomeWindow_child_widget_2 = QWidget()
        self.HomeWindow_child_widget_2.setObjectName(u"HomeWindow_child_widget_2") #唯一ID
        # 声明布局
        self.HomeWindow_verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.HomeWindow_verticalLayout_2.setObjectName(u"HomeWindow_verticalLayout_2") #唯一ID
        # 布局内添加子页面
        self.HomeWindow_verticalLayout_2.addWidget(self.HomeUpdateWindow)

        # 动态声明子页面
        self.HomeWindow_child_widget_3 = QWidget()
        self.HomeWindow_child_widget_3.setObjectName(u"HomeWindow_child_widget_3") #唯一ID
        self.HomeWindow_verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.HomeWindow_verticalLayout_3.setObjectName(u"HomeWindow_verticalLayout_3") #唯一ID
        # 布局内添加子页面
        self.HomeWindow_verticalLayout_3.addWidget(self.HomeDeleteWindow)

        # 子页面添加内容
        self.HomeWindow_child_widget_1.setLayout(self.HomeWindow_verticalLayout_1)
        self.HomeWindow_child_widget_2.setLayout(self.HomeWindow_verticalLayout_2)
        self.HomeWindow_child_widget_3.setLayout(self.HomeWindow_verticalLayout_3)
        # 获取QTabWdiget布局管理器
        layout = self.tab.layout()
        # 将动态子页面添加到布局中
        layout.addWidget(self.HomeWindow_child_widget_1)

        layout_2 = self.tab_2.layout()
        # 将动态子页面添加到布局中
        layout_2.addWidget(self.HomeWindow_child_widget_2)

        layout_3 = self.tab_3.layout()
        # 将动态子页面添加到布局中
        layout_3.addWidget(self.HomeWindow_child_widget_3)
        # 点击标签页事件
        self.tabWidget.tabBarClicked.connect(self.on_tab_clicked)

    def on_tab_clicked(self,index):
        # 处理删除文件信号
        if self.homeindexWindow_this_fileID == self.HomeDeleteWindow_this_fileID:
            self.homeindexWindow.label_10.setText('')
            try:
                read_file(self.homeindexWindow_this_package['filepath'])
            except Exception as e:
                self.homeindexWindow.label_10.setText('警告：该文件已被删除')

        # 处理更新文件信号
        if self.isChange_tall_home:
            self.isChange_tall_home = False
            # 此时的更新动作触发了全局文档更新# 初始化文档根目录 #所有文件的ID都被梭哈了
            self.homeindexWindow.init_listWidget() #更新menu动态列表





