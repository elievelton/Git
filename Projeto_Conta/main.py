import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

#importando as telas
from tela_depositar import Tela_Depositar
from tela_extrato import Tela_Extrato
from tela_sacar import Tela_Sacar
from tela_transferir import Tela_Transferir
from tela_CadastroCli import Tela_CadastroCli
from tela_CadastroCon import Tela_CadastroCon
from tela_login import Tela_Login
from tela_menu import Tela_Menu
from tela_menuCadastrar import Tela_Menu_Cadastrar

#import das classes
from classCliente import Cliente
from classConta import Conta
from classHisto import Historico
from classCadastro import Cadastro

# Ainda precisa ajustar esse código, depois que todas as telas estiverem prontas
class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout() #pilhas de telas

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()

        self.tela_login = Tela_Login() 
        self.tela_login.setupUi(self.stack0)
        self.tela_menu = Tela_Menu() 
        self.tela_menu.setupUi(self.stack1)
        self.tela_menuCadastrar = Tela_Menu_Cadastrar() 
        self.tela_menuCadastrar.setupUi(self.stack2)
        self.tela_CadastroCli = Tela_CadastroCli() 
        self.tela_CadastroCli.setupUi(self.stack3)
        self.tela_CadastroCon = Tela_CadastroCon() 
        self.tela_CadastroCon.setupUi(self.stack4)
        self.tela_depositar = Tela_Depositar()
        self.tela_depositar.setupUi(self.stack5)
        self.tela_sacar = Tela_Sacar()
        self.tela_sacar.setupUi(self.stack6)
        self.tela_transferir = Tela_Transferir()
        self.tela_transferir.setupUi(self.stack7)
        self.tela_extrato = Tela_Extrato()
        self.tela_extrato.setupUi(self.stack8)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)


class Main(QMainWindow, Ui_Main):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        
        
        
        self.cad = Cadastro()

        self.tela_login.pushButton.clicked.connect(self.login)
        self.tela_login.pushButton_2.clicked.connect(self.menu_cadastro)

        self.tela_menu.pushButton.clicked.connect(self.depositar)
        self.tela_menu.pushButton_2.clicked.connect(self.sacar)
        self.tela_menu.pushButton_3.clicked.connect(self.transferir)
        self.tela_menu.pushButton_4.clicked.connect(self.extrato)
        self.tela_menu.pushButton_5.clicked.connect(self.login)

        self.tela_menuCadastrar.pushButton.clicked.connect(self.cadastrar_cliente)
        self.tela_menuCadastrar.pushButton.clicked.connect(self.cadastrar_conta)
        self.tela_menuCadastrar.pushButton.clicked.connect(self.menu)


    def login(self):
        self.QtStack.setCurrentIndex(1)

    def menu(self):
        self.QtStack.setCurrentIndex(1)

    def menu_cadastro(self):
        self.QtStack.setCurrentIndex(2)

    def cadastrar_cliente(self):
        nome = self.tela_cadastroCli.lineEdit_2.text()
        endereco = self.tela_cadastroCli.lineEdit_5.text()
        cpf = self.tela_cadastroCli.lineEdit_6.text()
        nascimento = self.tela_cadastroCli.lineEdit_7.text()

        if not (nome == '' or endereco == '' or cpf == '' or nascimento == ''):
            c = Cliente(nome, endereco, cpf, nascimento)
            if(self.cad.cadastrar(c)):
                QMessageBox.information(
                    None, 'POO2', 'Cadastro Realizado com sucesso!')
                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
            else:
                QMessageBox.information(
                    None, 'POO2', 'O Cpf informado já encontra-se na base de dados')
        else:
            QMessageBox.information(
                None, 'POO2', 'Todos os valores devem ser preenchidos')
        self.QtStack.setCurrentIndex(0)

    def cadastrar_conta(self):
        self.QtStack.setCurrentIndex(4)

    def depositar(self):
        self.QtStack.setCurrentIndex(5)

    def sacar(self):
        self.QtStack.setCurrentIndex(6)

    def transferir(self):
        self.QtStack.setCurrentIndex(7)

    def extrato(self):
        self.QtStack.setCurrentIndex(8)
        
    

if __name__ == "__main__":

    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
