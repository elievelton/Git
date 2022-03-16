import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

from tela_inicial import Tela_Inicial
from tela_busca import Tela_Busca
from tela_cadastro import Tela_Cadastro
from ClassCliente import Cliente
from ClassCadastro import Cadastro


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout() #pilhas de telas

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial() 
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_busca = Tela_Busca()
        self.tela_busca.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)


class Main(QMainWindow, Ui_Main):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        self.tela_inicial.pushButton.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaBuscar)

        self.tela_busca.pushButton_2.clicked.connect(self.abrirTelaInicial)# tela de inicio

        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastro)
        self.tela_busca.pushButton.clicked.connect(self.botaoBusca)

    def botaoCadastro(self):

        nome = self.tela_cadastro.lineEdit.text()
        endereco = self.tela_cadastro.lineEdit_2.text()
        cpf = self.tela_cadastro.lineEdit_3.text()
        nascimento = self.tela_cadastro.lineEdit_4.text()

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
    
    def botaoBusca(self,cpf):
        cpf = self.tela_busca.lineEdit_3.text()
        cliente = self.cad.buscar(cpf)
        if(cliente != None):

            self.tela_busca.lineEdit.setText(cliente.nome)
            self.tela_busca.lineEdit_5.setText(cliente.endereco)
            self.tela_busca.lineEdit_4.setText(cliente.nascimento)
        else:
            QMessageBox.information(None,'POO2', 'CPF não encontrado')
    
    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaBuscar(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTelaInicial(self):  #usado para botão voltar na tela de busca
        self.QtStack.setCurrentIndex(0)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
