# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_menuCadastrar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 200, 121, 31))
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 260, 121, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(40, 400, 121, 31))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 40, 641, 71))
        self.frame.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 20, 201, 41))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setUnderline(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Conta", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
    # retranslateUi

