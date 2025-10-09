# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeindex.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QListWidgetItem, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (LineEdit, ListWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1112, 707)
        Form.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 100))
        self.widget_2.setStyleSheet(u"background-color: rgb(236, 236, 236);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(5, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(400, 0))
        self.horizontalLayout = QHBoxLayout(self.widget_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = LineEdit(self.widget_6)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.horizontalLayout_2.addWidget(self.widget_6)

        self.horizontalSpacer_2 = QSpacerItem(5, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 41))
        self.widget_4.setStyleSheet(u"background-color: rgb(211, 248, 226);")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.widget_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_6 = QPushButton(self.widget_4)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.horizontalSpacer_3 = QSpacerItem(905, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 15))
        self.label.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.label.setStyleSheet(u"color: rgb(15, 152, 0);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scrollArea = QScrollArea(self.widget_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(250, 16777215))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 248, 574))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.scrollAreaWidgetContents)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setMinimumSize(QSize(242, 0))
        self.widget_10.setMaximumSize(QSize(250, 16777215))
        font = QFont()
        font.setBold(False)
        self.widget_10.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.widget_10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"border-bottom-color: rgb(0, 0, 0);")
        self.verticalLayout_5 = QVBoxLayout(self.widget_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_8 = QLabel(self.widget_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_5.addWidget(self.label_8)

        self.listWidget = ListWidget(self.widget_11)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(280, 16777215))
        self.listWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)

        self.verticalLayout_5.addWidget(self.listWidget)


        self.verticalLayout_4.addWidget(self.widget_11)


        self.verticalLayout_6.addWidget(self.widget_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_4.addWidget(self.scrollArea)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(500, 0))
        self.widget_5.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 150))
        self.widget_8.setMaximumSize(QSize(16777215, 150))
        self.widget_8.setStyleSheet(u"background-color: rgb(238, 238, 238);")
        self.gridLayout = QGridLayout(self.widget_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.widget_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1)

        self.label_2 = QLabel(self.widget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 2)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_5)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 40))
        self.widget_9.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_5 = QPushButton(self.widget_9)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.label_10 = QLabel(self.widget_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.widget_9)

        self.graphicsView = QGraphicsView(self.widget_5)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_3.addWidget(self.graphicsView)

        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.widget_7)


        self.horizontalLayout_4.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u521d\u59cb\u5316\u6587\u6863\u5305", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u8bfb\u53d6\u9879\u76ee\u4f4d\u7f6e\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u5168\u90e8\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u5f00\u542f\u5c40\u57df\u7f51\u5171\u4eab\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6ID\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u65f6\u95f4\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5305\u540d\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u6240\u5c5e\u6807\u7b7e:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u521b\u5efa\u65f6\u95f4\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u4f4d\u7f6e\uff1a", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u5f00\u542f\u5c40\u57df\u7f51\u5171\u4eab(\u529f\u80fd\u6682\u5b9a)", None))
        self.label_10.setText("")
    # retranslateUi

