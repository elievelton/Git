# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transferir.ui'
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
        self.label_2.setGeometry(QRect(30, 250, 271, 20))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 300, 261, 20))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 350, 131, 36))
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 410, 106, 36))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(67, 67, 67);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(310, 249, 113, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(310, 295, 113, 21))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 20, 651, 61))
        self.frame.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(259, 11, 131, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(310, 200, 111, 21))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 200, 151, 20))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 98, 191, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(24, 141, 71, 16))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QRect(470, 95, 140, 30))
        self.lineEdit_4.setCursor(QCursor(Qt.SizeHorCursor))
        self.lineEdit_4.setFocusPolicy(Qt.NoFocus)
        self.lineEdit_4.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_4.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"font: 75 14pt \"Noto Sans\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setEchoMode(QLineEdit.Normal)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 98, 71, 16))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(90, 138, 111, 21))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(90, 98, 111, 21))
        self.lineEdit_6.setFocusPolicy(Qt.NoFocus)
        self.lineEdit_6.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Conta para Transfer\u00eancia:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Valor da Transfer\u00eancia:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Transferir", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Transferir", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Conta de Sa\u00edda:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Saldo Dispon\u00edvel:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Conta:", None))
        self.lineEdit_4.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.lineEdit_6.setText("")
    # retranslateUi

