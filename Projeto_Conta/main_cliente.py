import socket

import datetime
import string
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

"""importando as telas"""
from telas.tela_menuCadastrar import Tela_Menu_Cadastrar
from telas.tela_menu import Tela_Menu
from telas.tela_login import Tela_Login
from telas.tela_CadastroCon import Tela_CadastroCon
from telas.tela_CadastroCli import Tela_CadastroCli
from telas.tela_transferir import Tela_Transferir
from telas.tela_sacar import Tela_Sacar
from telas.tela_historico import Tela_Historico
from telas.tela_extrato import Tela_Extrato
from telas.tela_depositar import Tela_Depositar


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self):
        """ Função que realiza as configurações das telas"""
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()  # pilhas de telas

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()

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
        self.tela_historico = Tela_Historico()
        self.tela_historico.setupUi(self.stack9)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)

    def recebe():
        """Lida com o recebimento de mensagens"""
    pass

    def envia():
        """Lida com o envio de mensagens."""
        pass

    def exit():
        """Encerra a conexão"""
        pass

    def fecha():
        """Essa funcão é chamada quando a janela é fechada"""
        pass

class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        """ Função que realiza as configurações do que está presente nas telas"""
        super(Main, self).__init__(parent)
        self.setupUi(self)

ip = 'localhost' #definindo o endereço
port = 8000 #definindo o número de porta
addr = ((ip, port)) #criando tupla para armazenar o endereço e a porta

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

