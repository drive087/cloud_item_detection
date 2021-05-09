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


class Ui_Add_Item_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(485, 371)
        MainWindow.setMinimumSize(QSize(50, 100))
        MainWindow.setStyleSheet(u"backgroud-color:rgb(131, 129, 132);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(12, 12, 231, 311))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.LabelContainer = QFrame(self.frame)
        self.LabelContainer.setObjectName(u"LabelContainer")
        self.LabelContainer.setGeometry(QRect(10, 10, 211, 111))
        self.LabelContainer.setFrameShape(QFrame.StyledPanel)
        self.LabelContainer.setFrameShadow(QFrame.Raised)
        self.Label = QPlainTextEdit(self.LabelContainer)
        self.Label.setObjectName(u"Label")
        self.Label.setGeometry(QRect(10, 10, 191, 31))
        self.Label.setReadOnly(True)
        self.class_name = QPlainTextEdit(self.LabelContainer)
        self.class_name.setObjectName(u"class_name")
        self.class_name.setGeometry(QRect(10, 60, 191, 41))
        self.class_name.setReadOnly(False)
        self.ResetContainer = QFrame(self.frame)
        self.ResetContainer.setObjectName(u"ResetContainer")
        self.ResetContainer.setGeometry(QRect(10, 200, 211, 51))
        self.ResetContainer.setAutoFillBackground(True)
        self.ResetContainer.setStyleSheet(u"backgroud-color:Red;")
        self.ResetContainer.setFrameShape(QFrame.StyledPanel)
        self.ResetContainer.setFrameShadow(QFrame.Raised)
        self.Capture = QPushButton(self.ResetContainer)
        self.Capture.setObjectName(u"Capture")
        self.Capture.setGeometry(QRect(10, 0, 191, 51))
        self.Capture.setStyleSheet(u"border: 0px solid;\n"
"")
        self.Capture.setIconSize(QSize(30, 30))
        self.AddContainer = QFrame(self.frame)
        self.AddContainer.setObjectName(u"AddContainer")
        self.AddContainer.setGeometry(QRect(10, 259, 211, 41))
        self.AddContainer.setFrameShape(QFrame.StyledPanel)
        self.AddContainer.setFrameShadow(QFrame.Raised)
        self.Reset = QPushButton(self.AddContainer)
        self.Reset.setObjectName(u"Reset")
        self.Reset.setGeometry(QRect(0, 0, 201, 31))
        self.Reset.setStyleSheet(u"border: 0px solid;")
        self.BGContainer = QFrame(self.frame)
        self.BGContainer.setObjectName(u"BGContainer")
        self.BGContainer.setGeometry(QRect(10, 130, 211, 51))
        self.BGContainer.setAutoFillBackground(True)
        self.BGContainer.setStyleSheet(u"backgroud-color:Red;")
        self.BGContainer.setFrameShape(QFrame.StyledPanel)
        self.BGContainer.setFrameShadow(QFrame.Raised)
        self.BG = QPushButton(self.BGContainer)
        self.BG.setObjectName(u"BG")
        self.BG.setGeometry(QRect(10, 0, 191, 51))
        self.BG.setStyleSheet(u"border: 0px solid;\n"
"")
        self.BG.setIconSize(QSize(30, 30))
        self.Right = QFrame(self.centralwidget)
        self.Right.setObjectName(u"Right")
        self.Right.setGeometry(QRect(250, 10, 231, 311))
        self.Right.setFrameShape(QFrame.StyledPanel)
        self.Right.setFrameShadow(QFrame.Raised)
        self.LastCapture = QFrame(self.Right)
        self.LastCapture.setObjectName(u"LastCapture")
        self.LastCapture.setGeometry(QRect(10, 40, 211, 151))
        self.LastCapture.setFrameShape(QFrame.StyledPanel)
        self.LastCapture.setFrameShadow(QFrame.Raised)
        self.Purchase = QFrame(self.Right)
        self.Purchase.setObjectName(u"Purchase")
        self.Purchase.setGeometry(QRect(10, 220, 211, 80))
        self.Purchase.setFrameShape(QFrame.StyledPanel)
        self.Purchase.setFrameShadow(QFrame.Raised)
        self.Save = QPushButton(self.Purchase)
        self.Save.setObjectName(u"Save")
        self.Save.setGeometry(QRect(0, 0, 201, 71))
        self.Save.setStyleSheet(u"border:0px solid;")
        self.Amount = QPlainTextEdit(self.Right)
        self.Amount.setObjectName(u"Amount")
        self.Amount.setGeometry(QRect(170, 10, 51, 21))
        self.Amount.setReadOnly(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 485, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Label.setPlainText(QCoreApplication.translate("MainWindow", u"           Fill items name", None))
        self.Capture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.Reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.BG.setText(QCoreApplication.translate("MainWindow", u"BG", None))
        self.Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Amount.setPlainText(QCoreApplication.translate("MainWindow", u"0/4", None))
    # retranslateUi

