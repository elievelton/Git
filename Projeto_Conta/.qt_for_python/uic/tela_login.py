# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 533)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 206, 63, 20))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 246, 63, 20))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(230, 206, 161, 20))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(230, 246, 161, 20))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 316, 101, 23))
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 390, 181, 31))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font: 75 11pt \"Noto Sans\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 390, 101, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, 50, 671, 51))
        self.frame.setStyleSheet(u"background-color: rgb(64, 64, 64);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 4, 221, 41))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(187, 270, 256, 41))
        self.textBrowser.setStyleSheet(u"color: rgb(255, 255, 127);\n"
"border-color: rgb(0, 0, 127);\n"
"background-color: rgb(0, 0, 127);")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setLineWidth(-1)
        self.textBrowser.setMidLineWidth(-1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 125, 81, 71))
        self.label_3.setMaximumSize(QSize(256, 256))
        self.label_3.setPixmap(QPixmap(u"user.png"))
        self.label_3.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o \u00e9 cadastrado?", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fa\u00e7a seu login", None))
        self.label_3.setText("")
    # retranslateUi

