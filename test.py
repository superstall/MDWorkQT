import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QTextEdit, QPushButton, QToolBar, QSizePolicy
)
from PySide6.QtCore import Qt, QTimer,QSize
from PySide6.QtWebEngineWidgets import QWebEngineView
import markdown


class MarkdownEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("智能Markdown编辑器")
        self.resize(1000, 700)

        # 创建主布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # 左侧编辑区
        edit_container = QWidget()
        edit_layout = QVBoxLayout(edit_container)

        # 工具栏
        self.create_toolbar()
        edit_layout.addWidget(self.toolbar)

        # 文本编辑器
        self.text_edit = QTextEdit()
        self.text_edit.setAcceptRichText(False)
        self.text_edit.setPlaceholderText("输入Markdown内容...")
        edit_layout.addWidget(self.text_edit)

        # 右侧预览区
        self.preview_view = QWebEngineView()
        self.preview_view.setMinimumWidth(400)

        # 添加布局
        main_layout.addWidget(edit_container)
        main_layout.addWidget(self.preview_view)

        # 实时预览设置
        self.preview_timer = QTimer()
        self.preview_timer.setInterval(800)
        self.preview_timer.timeout.connect(self.update_preview)
        self.text_edit.textChanged.connect(self.on_text_changed)

    def create_toolbar(self):
        """创建智能Markdown工具栏"""
        self.toolbar = QToolBar("Markdown工具")
        self.toolbar.setIconSize(QSize(20, 20))

        # 按钮配置：名称、提示文本、插入内容、处理函数
        buttons = [
            ("H1", "一级标题", "# ", self.insert_text),
            ("H2", "二级标题", "## ", self.insert_text),
            ("H3", "三级标题", "### ", self.insert_text),
            ("B", "加粗", "****", self.wrap_selection),
            ("I", "斜体", "**", self.wrap_selection),
            ("S", "删除线", "~~", self.wrap_selection),
            ("Link", "链接", "[链接文本](https://)", self.insert_text),
            ("Img", "图片", "![图片描述](https://)", self.insert_text),
            ("List", "无序列表", "- ", self.insert_text),
            ("Num", "有序列表", "1. ", self.insert_text),
            ("Code", "行内代码", "`", self.wrap_selection),
            ("Block", "代码块", "\n```\n\n```\n", self.insert_code_block),
            ("Quote", "引用", "> ", self.insert_text),
            ("HR", "分割线", "\n---\n", self.insert_text),
            ("Table", "表格", "| 标题1 | 标题2 |\n| --- | --- |\n| 内容 | 内容 |", self.insert_text)
        ]

        for name, tip, content, handler in buttons:
            btn = QPushButton(name)
            btn.setToolTip(tip)
            btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

            # 特殊处理需要参数的函数
            if handler == self.wrap_selection:
                btn.clicked.connect(lambda _, c=content: handler(c))
            elif handler == self.insert_code_block:
                btn.clicked.connect(handler)
            else:
                btn.clicked.connect(lambda _, c=content: handler(c))

            self.toolbar.addWidget(btn)

    def insert_text(self, text):
        """在光标处插入文本"""
        cursor = self.text_edit.textCursor()
        cursor.beginEditBlock()

        # 插入文本并调整光标位置
        if cursor.hasSelection():
            # 替换选中内容
            cursor.insertText(text)
        else:
            # 插入文本并定位光标
            cursor.insertText(text)
            if len(text) > 1:
                # 移动光标到中间位置
                pos = cursor.position()
                move_left = len(text) // 2
                cursor.setPosition(pos - move_left)

        cursor.endEditBlock()
        self.text_edit.setFocus()

    def wrap_selection(self, wrapper):
        """用指定标记包裹选中内容或插入空标记"""
        cursor = self.text_edit.textCursor()
        cursor.beginEditBlock()

        if cursor.hasSelection():
            # 包裹选中内容
            selected = cursor.selectedText()
            cursor.insertText(f"{wrapper}{selected}{wrapper}")
        else:
            # 插入空标记并定位光标
            cursor.insertText(f"{wrapper}{wrapper}")
            pos = cursor.position()
            move_left = len(wrapper)
            cursor.setPosition(pos - move_left)

        cursor.endEditBlock()
        self.text_edit.setFocus()

    def insert_code_block(self):
        """插入代码块并定位光标"""
        cursor = self.text_edit.textCursor()
        cursor.beginEditBlock()

        # 插入代码块模板
        cursor.insertText("\n```\n\n```\n")

        # 定位到代码块中间
        pos = cursor.position()
        cursor.setPosition(pos - 5)  # 移动到第二个```之前

        cursor.endEditBlock()
        self.text_edit.setFocus()

    def on_text_changed(self):
        """文本改变时启动预览更新"""
        if not self.preview_timer.isActive():
            self.preview_timer.start()

    def update_preview(self):
        """更新预览内容"""
        self.preview_timer.stop()
        md_text = self.text_edit.toPlainText()

        # 添加基本CSS样式
        css = """
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                line-height: 1.6;
                color: #333;
            }
            h1, h2, h3 {
                color: #2c3e50;
                border-bottom: 1px solid #eaeaea;
            }
            pre {
                background-color: #f8f8f8;
                padding: 10px;
                border-radius: 5px;
                overflow: auto;
            }
            code {
                background-color: #f8f8f8;
                padding: 2px 4px;
                border-radius: 3px;
            }
            blockquote {
                border-left: 4px solid #ddd;
                padding-left: 10px;
                color: #777;
            }
            img {
                max-width: 100%;
            }
        </style>
        """

        # 渲染Markdown为HTML
        html = markdown.markdown(
            md_text,
            extensions=[
                'markdown.extensions.fenced_code',
                'markdown.extensions.tables',
                'markdown.extensions.extra'
            ]
        )

        # 加载到预览视图
        self.preview_view.setHtml(f"<html>{css}<body>{html}</body></html>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = MarkdownEditor()
    editor.show()
    sys.exit(app.exec())