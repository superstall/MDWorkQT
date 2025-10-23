# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeUpdate.ui'
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
    QLabel, QLayout, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

from qfluentwidgets import (DropDownPushButton, LineEdit, PushButton, ToolButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1033, 659)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.widget_4.setMaximumSize(QSize(16777215, 16777215))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_3 = PushButton(self.widget_6)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)

        self.lineEdit_3 = LineEdit(self.widget_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit = LineEdit(self.widget_6)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_2 = DropDownPushButton(self.widget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.lineEdit_2 = LineEdit(self.widget_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.pushButton = PushButton(self.widget_6)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)

        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget_6)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 5))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_4 = ToolButton(self.widget_8)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_5 = ToolButton(self.widget_8)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 450))
        self.widget_7.setStyleSheet(u"background-color: rgb(243, 243, 243);")
        self.verticalLayout_4 = QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.widget_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(80, 16777215))
        self.label_4.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_4.addWidget(self.widget_9)

        self.textEdit = QTextEdit(self.widget_7)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_4.addWidget(self.textEdit)


        self.verticalLayout_3.addWidget(self.widget_7)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(450, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphicsView = QGraphicsView(self.widget_2)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.graphicsView)


        self.horizontalLayout_2.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6807\u9898:", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u53ef\u9009\u6807\u7b7e", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u751f\u6210ID", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6807\u7b7e:", None))
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u5c55\u793a\u6587\u4ef6\uff1a", None))
        self.label_6.setText("")
    # retranslateUi

