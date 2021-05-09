# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(494, 501)
        MainWindow.setMinimumSize(QSize(50, 100))
        # MainWindow.setStyleSheet(u"backgroud-color:rgb(131, 129, 132);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(12, 12, 231, 434))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.LabelContainer = QFrame(self.frame)
        self.LabelContainer.setObjectName(u"LabelContainer")
        self.LabelContainer.setGeometry(QRect(10, 10, 211, 241))
        self.LabelContainer.setFrameShape(QFrame.StyledPanel)
        self.LabelContainer.setFrameShadow(QFrame.Raised)
        self.Label = QPlainTextEdit(self.LabelContainer)
        self.Label.setObjectName(u"Label")
        self.Label.setGeometry(QRect(10, 10, 191, 131))
        self.Label.setReadOnly(True)
        self.Threshold = QPlainTextEdit(self.LabelContainer)
        self.Threshold.setObjectName(u"Threshold")
        self.Threshold.setGeometry(QRect(10, 150, 191, 79))
        self.Threshold.setReadOnly(True)
        self.ResetContainer = QFrame(self.frame)
        self.ResetContainer.setObjectName(u"ResetContainer")
        self.ResetContainer.setGeometry(QRect(10, 260, 211, 80))
        self.ResetContainer.setAutoFillBackground(True)
        # self.ResetContainer.setStyleSheet(u"backgroud-color:Red;")
        self.ResetContainer.setFrameShape(QFrame.StyledPanel)
        self.ResetContainer.setFrameShadow(QFrame.Raised)
        self.Reset = QPushButton(self.ResetContainer)
        self.Reset.setObjectName(u"Reset")
        self.Reset.setGeometry(QRect(10, 0, 191, 81))
        self.Reset.setStyleSheet(u"border: 0px solid;"
"")
        self.Reset.setIconSize(QSize(30, 30))
        self.AddContainer = QFrame(self.frame)
        self.AddContainer.setObjectName(u"AddContainer")
        self.AddContainer.setGeometry(QRect(10, 350, 211, 80))
        self.AddContainer.setFrameShape(QFrame.StyledPanel)
        self.AddContainer.setFrameShadow(QFrame.Raised)
        self.Add = QPushButton(self.AddContainer)
        self.Add.setObjectName(u"Add")
        self.Add.setGeometry(QRect(0, 0, 201, 71))
        self.Add.setStyleSheet(u"border: 0px solid;")
        self.Right = QFrame(self.centralwidget)
        self.Right.setObjectName(u"Right")
        self.Right.setGeometry(QRect(250, 10, 231, 434))
        self.Right.setFrameShape(QFrame.StyledPanel)
        self.Right.setFrameShadow(QFrame.Raised)
        self.ListContainer = QFrame(self.Right)
        self.ListContainer.setObjectName(u"ListContainer")
        self.ListContainer.setGeometry(QRect(10, 10, 211, 331))
        self.ListContainer.setFrameShape(QFrame.StyledPanel)
        self.ListContainer.setFrameShadow(QFrame.Raised)
        self.List = QPlainTextEdit(self.ListContainer)
        self.List.setObjectName(u"List")
        self.List.setGeometry(QRect(0, 0, 211, 331))
        self.List.setReadOnly(True)
        self.Purchase = QFrame(self.Right)
        self.Purchase.setObjectName(u"Purchase")
        self.Purchase.setGeometry(QRect(10, 350, 211, 80))
        self.Purchase.setFrameShape(QFrame.StyledPanel)
        self.Purchase.setFrameShadow(QFrame.Raised)
        self.Purchase_2 = QPushButton(self.Purchase)
        self.Purchase_2.setObjectName(u"Purchase_2")
        self.Purchase_2.setGeometry(QRect(10, 0, 201, 71))
        self.Purchase_2.setStyleSheet(u"border:0px solid;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 494, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.Add.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.Purchase_2.setText(QCoreApplication.translate("MainWindow", u"Purchase", None))
    # retranslateUi

