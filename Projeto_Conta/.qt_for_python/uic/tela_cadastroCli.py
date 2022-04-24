# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_cadastroCli.ui'
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
    QWidget)

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
        self.label_2.setGeometry(QRect(130, 100, 61, 16))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(11)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(258, 220, 211, 20))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(256, 100, 211, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(256, 140, 211, 20))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(257, 178, 211, 20))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(130, 140, 91, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(131, 180, 61, 16))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(130, 220, 121, 16))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 360, 191, 31))
        font1 = QFont()
        font1.setFamilies([u"Agency FB"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 422, 91, 31))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 68, 68);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 20, 651, 61))
        self.frame.setStyleSheet(u"background-color: rgb(64, 64, 64);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 0, 231, 51))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 260, 61, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(260, 260, 211, 21))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 300, 61, 21))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(260, 300, 211, 21))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Data de Nasc:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Cliente", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cadastro Cliente", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
    # retranslateUi

