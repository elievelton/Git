import sys
import os


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication

#importando as telas
from telas.tela_depositar import Tela_Depositar
from telas.tela_extrato import Tela_Extrato
from telas.tela_historico import Tela_Historico
from telas.tela_sacar import Tela_Sacar
from telas.tela_transferir import Tela_Transferir
from telas.tela_CadastroCli import Tela_CadastroCli
from telas.tela_CadastroCon import Tela_CadastroCon
from telas.tela_login import Tela_Login
from telas.tela_menu import Tela_Menu
from telas.tela_menuCadastrar import Tela_Menu_Cadastrar


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


class Main(QMainWindow, Ui_Main):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        self.his = Historico()
        

        self.tela_login.pushButton.clicked.connect(self.botaoLogin)
        self.tela_login.pushButton_2.clicked.connect(self.abrirTelaMenu_Cadastro)

        self.tela_menu.pushButton.clicked.connect(self.abrirTelaDepositar)
        self.tela_menu.pushButton_2.clicked.connect(self.abrirTelaSacar)
        self.tela_menu.pushButton_3.clicked.connect(self.abrirTelaTransferir)
        self.tela_menu.pushButton_4.clicked.connect(self.abrirTelaExtrato)
        self.tela_menu.pushButton_5.clicked.connect(self.abrirTelaLogin)

        self.tela_menuCadastrar.pushButton.clicked.connect(self.abrirTelaCadastroCliente)
        self.tela_menuCadastrar.pushButton_2.clicked.connect(self.abrirTelaCadastroConta)
        self.tela_menuCadastrar.pushButton_3.clicked.connect(self.abrirTelaLogin)

        self.tela_CadastroCli.pushButton.clicked.connect(self.cadastrar_cliente)
        self.tela_CadastroCli.pushButton_2.clicked.connect(self.abrirTelaMenu_Cadastro)

        self.tela_CadastroCon.pushButton.clicked.connect(self.cadastrar_conta)
        self.tela_CadastroCon.pushButton_2.clicked.connect(self.abrirTelaMenu_Cadastro)

        self.tela_depositar.pushButton.clicked.connect(self.botaoDepositar)
        self.tela_depositar.pushButton_2.clicked.connect(self.abrirTelaMenu)

        self.tela_sacar.pushButton.clicked.connect(self.botaoSacar)
        self.tela_sacar.pushButton_2.clicked.connect(self.abrirTelaMenu)

        self.tela_transferir.pushButton.clicked.connect(self.botaoTransferir)
        self.tela_transferir.pushButton_2.clicked.connect(self.abrirTelaMenu)

        self.tela_extrato.pushButton.clicked.connect(self.botaoExtrato)
        self.tela_extrato.pushButton_2.clicked.connect(self.abrirTelaMenu)
        self.tela_extrato.pushButton_3.clicked.connect(self.abriTelaHistorico)

        self.tela_historico.pushButton.clicked.connect(self.botaoHistorico)
        self.tela_historico.pushButton_2.clicked.connect(self.abrirTelaExtrato)


    def abrirTelaLogin(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaMenu(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaMenu_Cadastro(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTelaCadastroCliente(self):
        self.QtStack.setCurrentIndex(3)

    def abrirTelaCadastroConta(self):
        self.QtStack.setCurrentIndex(4)

    def abrirTelaDepositar(self):
        self.QtStack.setCurrentIndex(5)
        login = self.tela_login.lineEdit.text()
        x = self.cad.buscarConCli(login)
        y = self.cad.buscarCliCon(login)
        self.tela_depositar.lineEdit_4.setText(x.nome)
        self.tela_depositar.lineEdit_5.setText(str(y.numero))
        self.tela_depositar.lineEdit_3.setText('R$ ' + str(y.saldo))

    def abrirTelaSacar(self):
        self.QtStack.setCurrentIndex(6)
        login = self.tela_login.lineEdit.text()
        x = self.cad.buscarConCli(login)
        y = self.cad.buscarCliCon(login)
        self.tela_sacar.lineEdit_4.setText(x.nome)
        self.tela_sacar.lineEdit_5.setText(str(y.numero))
        self.tela_sacar.lineEdit_3.setText('R$ ' + str(y.saldo))

    def abrirTelaTransferir(self):
        self.QtStack.setCurrentIndex(7)
        login = self.tela_login.lineEdit.text()
        x = self.cad.buscarConCli(login)
        y = self.cad.buscarCliCon(login)
        self.tela_transferir.lineEdit_6.setText(x.nome)
        self.tela_transferir.lineEdit_5.setText(str(y.numero))
        self.tela_transferir.lineEdit_4.setText('R$ ' + str(y.saldo))

    def abrirTelaExtrato(self):
        self.QtStack.setCurrentIndex(8)

    def abriTelaHistorico(self):
        self.QtStack.setCurrentIndex(9)

    def botaoLogin(self):
        login = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()

        existe = self.cad.buscarUsuario(login)
        x = self.cad.buscarConCli(login)
        y = self.cad.buscarCliCon(login)
        if(existe!=None):
        
            if (x != None):
                if((existe.usuario and existe.senha) == (login and senha)):
                    self.abrirTelaMenu()
                    self.tela_menu.lineEdit_2.setText(existe.nome)
                    self.tela_menu.lineEdit_3.setText(y.numero)
                    self.tela_menu.lineEdit.setText('R$ ' + str(y.saldo))
                else :
                    self.tela_login.textBrowser.setText("Dados de login incorretos!")
                    self.tela_login.lineEdit.setText('')
                    self.tela_login.lineEdit_2.setText('')
            else:
                QMessageBox.information(None, 'POO2', 'Esse cliente não possue uma conta! Realize um cadastro primeiro')
        else:
            QMessageBox.information(None, 'POO2', 'Cliente não existe! Clique no botão Cadastrar e faça seu cadastro')
            self.tela_login.lineEdit.setText('')
            self.tela_login.lineEdit_2.setText('')
        

# Função para cadastrar o cliente
    def cadastrar_cliente(self):
        nome = self.tela_CadastroCli.lineEdit.text()
        endereco = self.tela_CadastroCli.lineEdit_2.text()
        cpf = self.tela_CadastroCli.lineEdit_3.text()
        nascimento = self.tela_CadastroCli.lineEdit_4.text()
        usuario = self.tela_CadastroCli.lineEdit_5.text() 
        senha = self.tela_CadastroCli.lineEdit_6.text() 

        if not (nome == '' or endereco == '' or cpf == '' or nascimento == '' or usuario == ' ' or senha == ''):
            c = Cliente(nome, endereco, cpf, nascimento, usuario, senha)
            if(self.cad.cadastrarCli(c)):
                QMessageBox.information(None, 'POO2', 'Cadastro Realizado com sucesso!')
                
                
                self.tela_CadastroCli.lineEdit.setText('')
                self.tela_CadastroCli.lineEdit_2.setText('')
                self.tela_CadastroCli.lineEdit_3.setText('')
                self.tela_CadastroCli.lineEdit_4.setText('')
                self.tela_CadastroCli.lineEdit_5.setText('')
                self.tela_CadastroCli.lineEdit_6.setText('')
            else:
                QMessageBox.information(None, 'POO2', 'O Cpf já foi cadastrado!')
        else:
            QMessageBox.information(None, 'POO2', 'Todos os valores devem ser preenchidos')
#função para cadastrar conta
    def cadastrar_conta(self):
        numero = self.tela_CadastroCon.lineEdit.text()
        cpf_titular = self.tela_CadastroCon.lineEdit_2.text()
        saldo = 0
        limite = self.tela_CadastroCon.lineEdit_3.text()

        existe = self.cad.buscarCli(cpf_titular)
        if (existe != None):
            if not(numero == '' or cpf_titular == '' or limite == ''):
                co = Conta(numero, cpf_titular, saldo, limite)
                if(self.cad.cadastrarCon(co)):
                    QMessageBox.information(None, 'POO2', 'Cadastro Realizado com sucesso!')
                    self.tela_CadastroCon.lineEdit.setText('')
                    self.tela_CadastroCon.lineEdit_2.setText('')
                    self.tela_CadastroCon.lineEdit_3.setText('')
                else:
                    QMessageBox.information(None, 'POO2', 'Essa conta já existe!') 
            else:
                QMessageBox.information(None, 'POO2', 'Todos os campos devem ser preenchidos') 
        else:
            QMessageBox.information(None, 'POO2', 'Cliente não cadastrado!')
    #chamada para a tela de depositar
    def botaoDepositar(self):
        conta_dep = self.tela_depositar.lineEdit.text()
        valor = self.tela_depositar.lineEdit_2.text()
        c=self.cad.buscarCon(conta_dep)
        if(c != None):
            if not(conta_dep == '' or valor == ''):                
                    
                c.deposita(int(valor))
                
                QMessageBox.information(None, 'POO2', 'deposito feito com sucesso!')   
                self.tela_depositar.lineEdit.setText('')
                self.tela_depositar.lineEdit_2.setText('')
                self.tela_depositar.lineEdit_3.setText('R$ ' + str(c.saldo))
                self.tela_menu.lineEdit.setText('R$ ' + str(c.saldo))
            else:
                QMessageBox.information(None, 'POO2', 'Todos os campos devem ser preenchidos!')
#chamada para tela de sacar
    def botaoSacar(self):
        conta_saq = self.tela_sacar.lineEdit.text()
        valor = self.tela_sacar.lineEdit_2.text()
        cs=self.cad.buscarCon(conta_saq)
        
        if not(conta_saq == '' or valor == ''):
            if (cs != None):
                cs.sacar(int(valor))
                QMessageBox.information(None, 'POO2', 'Saque feito com sucesso!')
                self.tela_sacar.lineEdit.setText('')
                self.tela_sacar.lineEdit_2.setText('')
                self.tela_sacar.lineEdit_3.setText('R$ ' + str(cs.saldo))
                self.tela_menu.lineEdit.setText('R$ ' + str(cs.saldo)) 
            else:
                QMessageBox.information(None, 'POO2', 'Essa conta não existe!')
        else:
            QMessageBox.information(None, 'POO2', 'Todos os campos devem ser preenchidos!')

    #chamada para a tela de transferencia    
    def botaoTransferir(self):
        conta_saida = self.tela_transferir.lineEdit_3.text()
        conta_destino = self.tela_transferir.lineEdit.text()
        valor = self.tela_transferir.lineEdit_2.text()
        cs = self.cad.buscarCon(conta_saida)
        if not(conta_saida == '' or conta_destino == '' or valor == ''):
            if (cs != None):
                if(self.cad.buscarCon(conta_destino)):
                    d =self.cad.buscarCon(conta_destino)
                    d.transfere(cs,d,int(valor))
                    QMessageBox.information(None, 'POO2', 'Transferencia feita com sucesso')
                    self.tela_transferir.lineEdit_3.setText('R$ ' + str(cs.saldo))
                    self.tela_menu.lineEdit.setText('R$ ' + str(cs.saldo))
                else:
                    QMessageBox.information(None, 'POO2', 'Conta de destino não existe!')
            else:
                QMessageBox.information(None, 'POO2', 'Conta de saída não existe!')
        else:
            QMessageBox.information(None, 'POO2', 'Todos os campos devem ser preenchidos!')
#chamada para tela de extrato
    def botaoExtrato(self):
        conta = self.tela_extrato.lineEdit.text()
        c = self.cad.buscarCon(conta)
        if not(conta== ''):
            if (c != None):
                x = c.extrato()
                self.tela_extrato.textBrowser.setText(x)
            else:
                QMessageBox.information(None, 'POO2', 'Essa conta não existe!')
        else:
            QMessageBox.information(None, 'POO2', 'Todos os campos devem ser preenchidos!')
#chamada para a tela historico
    def botaoHistorico(self):
        conta = self.tela_historico.lineEdit.text()
        c = self.cad.buscarCon(conta)
        if not(conta== ''):
            if (c != None):
                self.tela_historico.textBrowser.setText(self.his.data_de_abertura.strftime("%Y-%m-%d %H:%M:%S"))
                #para conseguir imprimir no TextBrowser
                msg = ""
                for x in c.historico.transacoes:
                    msg+=str(x)+"\n"
                self.tela_historico.textBrowser.setText(msg)
                
                
            else:
                QMessageBox.information(None, 'POO2', 'Essa conta não existe!')
        else:
            QMessageBox.information(None, 'POO2', 'Todos os campos devem ser preenchidos!')
        
 
if __name__ == "__main__":

    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
