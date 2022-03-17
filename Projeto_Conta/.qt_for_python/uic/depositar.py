# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'depositar.ui'
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
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 220, 201, 31))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 280, 181, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 340, 131, 36))
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 400, 106, 36))
        font2 = QFont()
        font2.setFamily(u"Agency FB")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(330, 230, 113, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(330, 280, 113, 21))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 30, 651, 61))
        self.frame.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 13, 131, 31))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 109, 61, 16))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 109, 171, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(24, 152, 61, 16))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QRect(470, 106, 140, 30))
        self.lineEdit_3.setCursor(QCursor(Qt.SizeHorCursor))
        self.lineEdit_3.setFocusPolicy(Qt.NoFocus)
        self.lineEdit_3.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_3.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"font: 75 14pt \"Noto Sans\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setEchoMode(QLineEdit.Normal)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(90, 109, 111, 21))
        self.lineEdit_4.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(90, 149, 111, 21))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Conta para deposito:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Valor do dep\u00f3sito:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Depositar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Depositar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Saldo Dispon\u00edvel:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Conta:", None))
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
    # retranslateUi

