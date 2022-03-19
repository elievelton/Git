# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extrato.ui'
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
        MainWindow.resize(640, 480)
        MainWindow.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 410, 106, 36))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(150, 180, 311, 221))
        self.textBrowser.setStyleSheet(u"background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 160, 63, 20))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 20, 651, 61))
        self.frame.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 10, 221, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 120, 63, 20))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(210, 120, 113, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 114, 106, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 420, 211, 21))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(500, 420, 91, 21))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(170, 85, 0);\n"
"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Extrato", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Extrato da Conta", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Conta", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Consulte o hist\u00f3rico completo:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Continuar", None))
    # retranslateUi

