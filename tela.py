# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaCadastro.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ClassCliente import Cliente
from ClassCadastro import Cadastro


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Cadastro = QtWidgets.QLabel(self.centralwidget)
        self.Cadastro.setGeometry(QtCore.QRect(258, 10, 91, 20))
        self.Cadastro.setMaximumSize(QtCore.QSize(91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Cadastro.setFont(font)
        self.Cadastro.setObjectName("Cadastro")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(155, 50, 231, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 63, 20))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(155, 90, 241, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 63, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(155, 130, 240, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 63, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(158, 170, 221, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 81, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 210, 106, 21))
        self.pushButton.setObjectName("pushButton")
        self.Buscar = QtWidgets.QLabel(self.centralwidget)
        self.Buscar.setGeometry(QtCore.QRect(250, 260, 71, 20))
        self.Buscar.setMaximumSize(QtCore.QSize(91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Buscar.setFont(font)
        self.Buscar.setObjectName("Buscar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-13, 240, 661, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(65, 302, 63, 20))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 302, 171, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 302, 106, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 400, 63, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(145, 370, 241, 21))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 370, 63, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(148, 430, 221, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(145, 400, 240, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 430, 81, 20))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        '''modificações'''
        self.cad = Cadastro()
        self.pushButton.clicked.connect(self.botaoCadastro)
        self.pushButton_2.clicked.connect(self.botaoBusca)

    def botaoCadastro(self):
        nome=self.lineEdit.text()
        endereco = self.label_2.text()
        cpf = self.label_3.text()
        nascimento = self.label_4.text()
        if not (nome == '' or endereco == '' or cpf == '' or nascimento == ''):
            c = Cliente(nome,endereco,cpf,nascimento)
            if(self.cad.cadastrar(c)):
                QMessageBox.information(None,'POO2', 'Cadastro Realizado com sucesso!')
                self.lineEdit.setText('')
                self.lineEdit_2.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
            else:
                QMessageBox.information(None,'POO2', 'O Cpf informado já encontra-se na base de dados')
        else:
            QMessageBox.information(None,'POO2', 'Todos os valores devem ser preenchidos')

    def botaoBusca(self):
        cpf = self.lineEdit_5.text()
        cliente = self.cad.buscar(cpf)
        if(cliente == None):

            self.lineEdit_8.setText(cliente.nome)
            self.lineEdit_6.setText(cliente.endereco)
            self.lineEdit_7.setText(cliente.nascimento)
        else:
            QMessageBox.information(None,'POO2', 'CPF não encontrado')



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Cadastro.setText(_translate("MainWindow", "Cadastro"))
        self.label.setText(_translate("MainWindow", "Nome"))
        self.label_2.setText(_translate("MainWindow", "Endereço"))
        self.label_3.setText(_translate("MainWindow", "CPF"))
        self.label_4.setText(_translate("MainWindow", "Nascimento"))
        self.pushButton.setText(_translate("MainWindow", "Cadastrar"))
        self.Buscar.setText(_translate("MainWindow", "Buscar"))
        self.label_5.setText(_translate("MainWindow", "CPF"))
        self.pushButton_2.setText(_translate("MainWindow", "Buscar"))
        self.label_6.setText(_translate("MainWindow", "CPF"))
        self.label_7.setText(_translate("MainWindow", "Endereço"))
        self.label_8.setText(_translate("MainWindow", "Nascimento"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

