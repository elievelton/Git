import datetime
import sys
import hashlib

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


"""import das classes"""



from main_cliente import Conectar
from servidor.tratamento import concatenar_operacao, replace_dados


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
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


"""Classe principal"""


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        """ Função que realiza as configurações do que está presente nas telas"""
        super(Main, self).__init__(parent)
        self.setupUi(self)
        
        self.conect = Conectar()
        

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
        """Carrega tela inicial"""
        self.QtStack.setCurrentIndex(0)

    def abrirTelaMenu(self):
        """Carrega tela menu"""
        self.QtStack.setCurrentIndex(1) 
        self.tela_menu.pushButton_5.clicked.connect(self.botaoSair)
        

       

    def abrirTelaMenu_Cadastro(self):
        """Carrega tela menu cadastro"""
        self.QtStack.setCurrentIndex(2)

    def abrirTelaCadastroCliente(self):
        """Carrega tela para cadastrar clientes"""
        self.QtStack.setCurrentIndex(3)

    def abrirTelaCadastroConta(self):
        """Carrega tela para cadastrar contas"""
        self.QtStack.setCurrentIndex(4)

    def abrirTelaDepositar(self):
        """Carrega tela para realizar depósito e informa os atributos do cliente"""
        self.QtStack.setCurrentIndex(5)
    
        
        mensagem = self.conect.envia(concatenar_operacao(['10']))
        
        if(mensagem !=None):
            self.tela_depositar.lineEdit_4.setText(f'{mensagem[2]}')
            self.tela_depositar.lineEdit_5.setText(f'{mensagem[9]}')
            self.tela_depositar.lineEdit_3.setText('R$ ' + f'{mensagem[11]}')
            self.tela_depositar.pushButton_2.clicked.connect(self.botao_Voltar_Menu)
            
            

    def botaoSair(self): #função para fecha conexao do cliente
        
        self.conect.sair()
        self.conect.envia("encerrar")
    
    def botao_Voltar_Menu(self):# função para atualizar saldo da conta
        mensagem = self.conect.envia(concatenar_operacao(['13']))
        self.tela_depositar.lineEdit_3.setText('R$ ' + f'{mensagem[11]}')


        

        
    def abrirTelaSacar(self):
        """Carrega tela para realizar saque e informa os atributos do cliente"""
        self.QtStack.setCurrentIndex(6)
        
        mensagem = self.conect.envia(concatenar_operacao(['11']))
        

        if(mensagem !=None):
            self.tela_sacar.lineEdit_4.setText(f'{mensagem[2]}')
            self.tela_sacar.lineEdit_5.setText(f'{mensagem[9]}')
            self.tela_sacar.lineEdit_3.setText('R$ ' + f'{mensagem[11]}')
            self.tela_sacar.pushButton_2.clicked.connect(self.botao_Voltar_Menu)

    def abrirTelaTransferir(self):
        """Carrega tela para realizar transferência e informa os atributos do cliente"""
        self.QtStack.setCurrentIndex(7)
        
        mensagem = self.conect.envia(concatenar_operacao(['12']))
        
  
        self.tela_transferir.lineEdit_6.setText(f'{mensagem[2]}') #Nome do Cliente
        self.tela_transferir.lineEdit_5.setText(f'{mensagem[9]}') #Numero da conta
        self.tela_transferir.lineEdit_4.setText('R$ ' + f'{mensagem[11]}') #valor da conta
        self.tela_transferir.pushButton_2.clicked.connect(self.botao_Voltar_Menu)

    def abrirTelaExtrato(self):
        """Carrega tela para mostrar o extrato do cliente"""
        self.QtStack.setCurrentIndex(8)

    def abriTelaHistorico(self):
        """Carrega tela para mostrar o histórico do cliente"""
        self.QtStack.setCurrentIndex(9)

    def botaoLogin(self):
        """Faz o login e verifica se existe usuário"""
        login = self.tela_login.lineEdit.text()
        senha_sem_tratar = self.tela_login.lineEdit_2.text()
        senha = self.md5_generator(senha_sem_tratar)
        
        if not(login == '' or senha == ''):
            mensagem = self.conect.envia(concatenar_operacao(['3', login, senha]))
            self.tela_login.lineEdit.setText('')
            self.tela_login.lineEdit_2.setText('')
            print(mensagem)
            if mensagem != None:
                if mensagem[0] == '0':
                    self.abrirTelaMenu()
                    QMessageBox.information(None, 'mensagem', mensagem[1])
                                
                    self.tela_menu.lineEdit_2.setText(str(f'{mensagem[3]}'))
                    self.tela_menu.lineEdit_3.setText(f'{mensagem[10]}')
                    self.tela_menu.lineEdit.setText('R$ ' + f'{mensagem[12]}')
                    
                elif mensagem[0] == '1':
                    QMessageBox.information(None, 'mensagem', mensagem[1])

                elif mensagem[0] == '2':
                    QMessageBox.information(None, 'mensagem', mensagem[1])

                elif mensagem[0] == '3':
                    QMessageBox.information(None, 'mensagem', mensagem[1])
            else:
                QMessageBox.information(None, 'POO2', 'Usuaio não cadastro, Realize seu cadastro!')

        else:
            QMessageBox.information(None, 'POO2', 'Todos os campos devem ser preenchidos')  


    def cadastrar_cliente(self):
        """ Função para cadastrar o cliente"""
        nome = self.tela_CadastroCli.lineEdit.text()
        endereco = self.tela_CadastroCli.lineEdit_2.text()
        cpf = self.tela_CadastroCli.lineEdit_3.text()
        nascimento = self.tela_CadastroCli.lineEdit_4.text()
        usuario = self.tela_CadastroCli.lineEdit_5.text()
        senha = self.tela_CadastroCli.lineEdit_6.text()

        if not (nome == '' or endereco == '' or cpf == '' or nascimento == '' or usuario == ' ' or senha == ''):
            mensagem = self.conect.envia(concatenar_operacao(['2', nome, endereco, cpf, nascimento, usuario, senha]))
            QMessageBox.information(None, 'mensagem', mensagem[1])

            self.tela_CadastroCli.lineEdit.setText('')
            self.tela_CadastroCli.lineEdit_2.setText('')
            self.tela_CadastroCli.lineEdit_3.setText('')
            self.tela_CadastroCli.lineEdit_4.setText('')
            self.tela_CadastroCli.lineEdit_5.setText('')
            self.tela_CadastroCli.lineEdit_6.setText('')
        else:
            QMessageBox.information(None, 'POO2', 'Todos os valores devem ser preenchidos')

    def cadastrar_conta(self):
        """função para cadastrar conta"""
        numero = self.tela_CadastroCon.lineEdit.text()
        cpf_titular = self.tela_CadastroCon.lineEdit_2.text()
        saldo = 10
        limite = self.tela_CadastroCon.lineEdit_3.text()
        
        if not(numero == '' or cpf_titular == '' or limite == ''):
            mensagem = self.conect.envia(concatenar_operacao(['1', numero, cpf_titular, saldo, limite]))
            QMessageBox.information(None, 'mensagem', mensagem[1])

            self.tela_CadastroCon.lineEdit.setText('')
            self.tela_CadastroCon.lineEdit_2.setText('')
            self.tela_CadastroCon.lineEdit_3.setText('')
        else:
            QMessageBox.information(None, 'POO2', 'Todos os campos devem ser preenchidos')

    #funcionamento tela de depositar
    def botaoDepositar(self):
        """ Função para realizar depoósito"""
        
        valor = self.tela_depositar.lineEdit_2.text()
       

        if not( valor == ''):
            mensagem = self.conect.envia(concatenar_operacao(['6', valor]))

            QMessageBox.information(None, 'mensagem', mensagem[1])

            self.tela_depositar.lineEdit_2.setText('')
            self.tela_depositar.lineEdit_4.setText(f'{mensagem[3]}')
            self.tela_depositar.lineEdit_5.setText(f'{mensagem[10]}')
            self.tela_depositar.lineEdit_3.setText('R$ ' + f'{mensagem[12]}')
            self.tela_menu.lineEdit.setText('R$ ' + f'{mensagem[12]}') 
            
        else:
            QMessageBox.information(None, 'POO2', 'Todos os campos devem ser preenchidos!')

    #funcionamento tela de sacar
    def botaoSacar(self):
        """ Função para realizar saque"""
        
        valor_saq = self.tela_sacar.lineEdit_2.text()
        

        if not(valor_saq == ''):
            mensagem = self.conect.envia(concatenar_operacao(['5', valor_saq]))
            if(mensagem[0]=='0'):              
            
                QMessageBox.information(None, 'mensagem', mensagem[1])
        
                self.tela_sacar.lineEdit_4.setText(f'{mensagem[3]}')
                self.tela_sacar.lineEdit_5.setText(f'{mensagem[10]}')
                self.tela_sacar.lineEdit_3.setText('R$ ' + f'{mensagem[12]}')
                self.tela_menu.lineEdit.setText('R$ ' + f'{mensagem[12]}')
            else:
                QMessageBox.information(None, 'mensagem', mensagem[1])    
        else:
            QMessageBox.information(None, 'POO2', 'Todos os campos devem ser preenchidos!')

    #funcionamento tela de transferencia
    def botaoTransferir(self):
        """ Função para realizar transferência"""

        conta_destino = self.tela_transferir.lineEdit.text()
        valor = self.tela_transferir.lineEdit_2.text()
        

        
        if not ( conta_destino == '' or valor == '' ):
            mensagem = self.conect.envia(concatenar_operacao(['7', conta_destino, valor]))

            if(mensagem[0]=='0'):
                QMessageBox.information(None, 'mensagem', mensagem[1])
                self.tela_transferir.lineEdit_4.setText('R$ ' + f'{mensagem[12]}')
                self.tela_transferir.lineEdit_6.setText(f'{mensagem[3]}')
                self.tela_transferir.lineEdit_5.setText(f'{mensagem[10]}')
                self.tela_menu.lineEdit.setText('R$ ' + f'{mensagem[12]}')
                self.tela_transferir.lineEdit.setText('')
                self.tela_transferir.lineEdit_2.setText('')
            elif(mensagem[0]=='1'):
                QMessageBox.information(None, 'mensagem', mensagem[1])
            elif(mensagem[0]=='3'):
                QMessageBox.information(None, 'mensagem', mensagem[1])
        else:
            QMessageBox.information(None, 'POO2', 'Todos os campos devem ser preenchidos!')

    #funcionamento tela de extrato
    def botaoExtrato(self):
        
        """ Função para informar o extrato"""
        mensagem = self.conect.envia(concatenar_operacao(['8']))        

        self.tela_extrato.textBrowser.setText("Numero Conta: {} \nSaldo Disponível: {}".format(f'{mensagem[10]}', f'{mensagem[12]}'))
    
    #funcionamento tela historico
    def botaoHistorico(self):
        """ Função para informar o histórico"""
        
        mensagem = self.conect.envia(concatenar_operacao(['9']))
        
        QMessageBox.information(None, 'mensagem', mensagem[1])

        tratar= mensagem[14]
        dividir = tratar.split('\\n')
        
        msg = "Abertura da conta : " + mensagem[9] + "\n" + "\n"

        for i in dividir:
            msg+= str(i) + "\n"

        self.tela_historico.textBrowser.setText(msg)

    def md5_generator(self,str):
        m = hashlib.md5()
        m.update(str.encode())
        return m.hexdigest()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())