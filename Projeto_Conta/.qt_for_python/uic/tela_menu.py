# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_menu.ui'
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
        MainWindow.setCursor(QCursor(Qt.OpenHandCursor))
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 190, 121, 31))
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 250, 121, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(250, 310, 121, 31))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(250, 370, 121, 31))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(500, 412, 81, 31))
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 68, 68);\n"
"")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 30, 661, 71))
        self.frame.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 101, 41))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 120, 171, 21))
        font3 = QFont()
        font3.setFamily(u"Noto Sans")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QRect(460, 117, 140, 30))
        self.lineEdit.setCursor(QCursor(Qt.SizeHorCursor))
        self.lineEdit.setFocusPolicy(Qt.NoFocus)
        self.lineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"font: 75 14pt \"Noto Sans\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setInputMethodHints(Qt.ImhNone)
        self.lineEdit.setFrame(True)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 120, 111, 21))
        self.lineEdit_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 160, 111, 21))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 61, 16))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(14, 163, 61, 16))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.frame.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Depositar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Sacar", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Transferir", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Extrato", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Saldo Dispon\u00edvel:", None))
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Conta:", None))
    # retranslateUi

