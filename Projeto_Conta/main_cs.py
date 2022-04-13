import datetime
import sys

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
from classBanco import Banco
from classCadastro import Cadastro
from classHisto import Historico
from classConta import Conta
from classCliente import Cliente

from main_cliente import Conectar


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
        
        self.cad = Cadastro()
        self.his = Historico()
        self.conect = Conectar()

        """CRIANDO O BANCO DE DADOS E AS TABELAS"""
        self.ban = Banco()
        database_query = "CREATE DATABASE IF NOT EXISTS banco"


        conexao = self.ban.criando_conexao(
            'localhost', 'root', '12345', 'banco')

        self.ban.criando_bancodedados(conexao, database_query)

        tabela_clientes = "CREATE TABLE IF NOT EXISTS clientes( cpf bigint(11)  PRIMARY KEY, nome text NOT NULL , endereco text NOT NULL, nascimento text NOT NULL, usuario text NOT NULL, senha VARCHAR(32) NOT NULL, conta bigint(11), data_abertura TEXT);"
        self.ban.executando_query(conexao, tabela_clientes)

        tabela_contas = "CREATE TABLE IF NOT EXISTS contas( numero int(5) NOT NULL , cpf_titular bigint(11)  PRIMARY KEY, saldo FLOAT(5,2) NOT NULL, limite text NOT NULL, historico text DEFAULT NULL);"
        self.ban.executando_query(conexao, tabela_contas)

        alter_cli_con = """
        ALTER TABLE clientes
        ADD FOREIGN KEY(conta)
        REFERENCES contas(cpf_titular);
           """
        self.ban.executando_query(conexao, alter_cli_con)

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
        login = self.tela_login.lineEdit.text()
        conexao = self.ban.criando_conexao(
                            'localhost',
                            'root',
                            '12345',
                            'banco',
                        )
        x = self.ban.Buscar_cliente_bd_login(conexao,login)
        y = self.ban.Buscar_conta_bd_login(conexao,login)
        self.tela_depositar.lineEdit_4.setText(x[0][1])
        self.tela_depositar.lineEdit_5.setText(str(y[0][0]))
        self.tela_depositar.lineEdit_3.setText('R$ ' + str(y[0][2]))

    def abrirTelaSacar(self):
        """Carrega tela para realizar saque e informa os atributos do cliente"""
        self.QtStack.setCurrentIndex(6)
        login = self.tela_login.lineEdit.text()
        conexao = self.ban.criando_conexao(
                            'localhost',
                            'root',
                            '12345',
                            'banco',
                        )
        q1 = (f"select * from clientes where usuario = '{login}'")
        dados = self.ban.lendo_dados(conexao, q1)
        lista = list(dados)
        conta = self.ban.Buscar_conta_bd(conexao,lista[0][6])
        convert_conta = list(conta)
        self.tela_sacar.lineEdit_4.setText(lista[0][1])
        self.tela_sacar.lineEdit_5.setText(str(convert_conta[0][0]))
        self.tela_sacar.lineEdit_3.setText('R$ ' + str(convert_conta[0][2]))

    def abrirTelaTransferir(self):
        """Carrega tela para realizar transferência e informa os atributos do cliente"""
        self.QtStack.setCurrentIndex(7)
        login = self.tela_login.lineEdit.text()
        conexao = self.ban.criando_conexao(
                            'localhost',
                            'root',
                            '12345',
                            'banco',
                        )
        x = self.ban.Buscar_cliente_bd_login(conexao,login)
        y = self.ban.Buscar_conta_bd_login(conexao,login)
        self.tela_transferir.lineEdit_6.setText((x[0][1]))
        self.tela_transferir.lineEdit_5.setText(str(y[0][0]))
        self.tela_transferir.lineEdit_4.setText('R$ ' + str(y[0][2]))

    def abrirTelaExtrato(self):
        """Carrega tela para mostrar o extrato do cliente"""
        self.QtStack.setCurrentIndex(8)

    def abriTelaHistorico(self):
        """Carrega tela para mostrar o histórico do cliente"""
        self.QtStack.setCurrentIndex(9)

    def botaoLogin(self):
        """Faz o login e verifica se existe usuário"""
        login = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        conexao = self.ban.criando_conexao(
                    'localhost',
                    'root',
                    '12345',
                    'banco',
                )
        cursor= conexao.cursor()
        b=self.ban.Buscar_cliente_bd_login(conexao,login) #retorna o cpf do cliente
        buscar_cliente= self.ban.Buscar_cliente_bd(conexao,b[0][0])
        
        
        cursor.execute(f"select * from clientes where usuario = '{login}' and senha = '{senha}'")
        valor = cursor.fetchall()
        convert_lista= list(valor)
        if(convert_lista!=None):
            if (convert_lista):
                
                if((convert_lista[0][4] and convert_lista[0][5]) == (login and senha)):
                    
                    #mensagem = self.conect.envia(operacao)

                    conta = self.ban.Buscar_conta_bd(conexao,convert_lista[0][6])
                    convert_conta = list(conta)
                    self.abrirTelaMenu()
                    self.tela_menu.lineEdit_2.setText(convert_lista[0][1])
                    self.tela_menu.lineEdit_3.setText(str(convert_conta[0][0]))
                    self.tela_menu.lineEdit.setText('R$ ' + str(convert_conta[0][2]))
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
        conexao.close()    
        """Faz o login e verifica se existe usuário"""



    def cadastrar_cliente(self):
        """ Função para cadastrar o cliente"""
        nome = self.tela_CadastroCli.lineEdit.text()
        endereco = self.tela_CadastroCli.lineEdit_2.text()
        cpf = self.tela_CadastroCli.lineEdit_3.text()
        nascimento = self.tela_CadastroCli.lineEdit_4.text()
        usuario = self.tela_CadastroCli.lineEdit_5.text()
        senha = self.tela_CadastroCli.lineEdit_6.text()

        conexao = self.ban.criando_conexao(
                            'localhost',
                            'root',
                            '12345',
                            'banco',
                        )
        if not (nome == '' or endereco == '' or cpf == '' or nascimento == '' or usuario == ' ' or senha == ''):
            
            #c = Cliente(nome, endereco, cpf, nascimento, usuario, senha)
            buscar = self.ban.Buscar_cliente_bd(conexao,cpf)
            
            if(buscar ==None):
                QMessageBox.information(
                    None, 'POO2', 'Cadastro Realizado com sucesso!')
                
                inserindo_clientes = f"INSERT INTO clientes (cpf, nome, endereco, nascimento, usuario, senha) VALUES ({cpf}, {nome}, {endereco}, {nascimento},{usuario}, {senha})"
                self.ban.executando_query(conexao, inserindo_clientes)

                self.tela_CadastroCli.lineEdit.setText('')
                self.tela_CadastroCli.lineEdit_2.setText('')
                self.tela_CadastroCli.lineEdit_3.setText('')
                self.tela_CadastroCli.lineEdit_4.setText('')
                self.tela_CadastroCli.lineEdit_5.setText('')
                self.tela_CadastroCli.lineEdit_6.setText('')
            else:
                QMessageBox.information(
                    None, 'POO2', 'O Cpf já foi cadastrado!')
        else:
            QMessageBox.information(
                None, 'POO2', 'Todos os valores devem ser preenchidos')

    def cadastrar_conta(self):
        """função para cadastrar conta"""
        numero = self.tela_CadastroCon.lineEdit.text()
        cpf_titular = self.tela_CadastroCon.lineEdit_2.text()
        saldo = 10
        limite = self.tela_CadastroCon.lineEdit_3.text()
        
        conexao = self.ban.criando_conexao(
                    'localhost',
                    'root',
                    '12345',
                    'banco',
                )
        

        cliente = self.ban.Buscar_cliente_bd(conexao,cpf_titular)
        conta =self.ban.Buscar_conta_bd(conexao,cpf_titular)
        teste=self.ban.retorna_dado_conta(conexao,numero,cpf_titular,2)
        
        now = datetime.datetime.utcnow()
        if (cliente != None):
            if not(numero == '' or cpf_titular == '' or limite == ''):
    
                if(conta==None):
                    QMessageBox.information(
                        None, 'POO2', 'Cadastro Realizado com sucesso!')
                    self.ban.gravar_abertura_conta(conexao,cliente[0][0],now.strftime('%Y-%m-%d %H:%M:%S'))
                    
                    inserindo_contas = f"INSERT INTO contas (numero, cpf_titular, saldo, limite) VALUES ({numero}, {cpf_titular}, {saldo}, {limite})"
                    self.ban.executando_query(conexao, inserindo_contas)
                    self.ban.InserirConta_cliente(conexao,cpf_titular)
                    
                    self.tela_CadastroCon.lineEdit.setText('')
                    self.tela_CadastroCon.lineEdit_2.setText('')
                    self.tela_CadastroCon.lineEdit_3.setText('')
                else:
                    QMessageBox.information(
                        None, 'POO2', 'Essa conta já existe!')
            else:
                QMessageBox.information(
                    None, 'POO2', 'Todos os campos devem ser preenchidos')
        else:
            QMessageBox.information(None, 'POO2', 'Cliente não cadastrado!')
    # chamada para a tela de depositar

    def botaoDepositar(self):
        """ Função para realizar depoósito"""
        conta_dep = self.tela_depositar.lineEdit.text()
        valor = self.tela_depositar.lineEdit_2.text()
        conexao = self.ban.criando_conexao(
                    'localhost',
                    'root',
                    '12345',
                    'banco',
                )
        
        c = self.ban.retorna_dado_conta(conexao,'cpf_titular','numero',conta_dep)
        saldo =self.ban.retorna_dado_conta(conexao,'saldo','numero',conta_dep)
        list(saldo)
        if(c != None):
            if not(c==None):

                self.ban.altera_saldo(conexao,float(valor),c[0][0])
                saldo =self.ban.retorna_dado_conta(conexao,'saldo','numero',conta_dep)
                
                QMessageBox.information(
                    None, 'POO2', 'deposito feito com sucesso!')
                self.tela_depositar.lineEdit.setText('')
                self.tela_depositar.lineEdit_2.setText('')
                self.tela_depositar.lineEdit_3.setText('R$ ' + str(saldo[0][0]))
                self.tela_menu.lineEdit.setText('R$ ' + str(saldo[0][0]))
            else:
                QMessageBox.information(
                    None, 'POO2', 'Todos os campos devem ser preenchidos!')
# chamada para tela de sacar

    def botaoSacar(self):
        """ Função para realizar saque"""
        login = self.tela_login.lineEdit.text()
        valor_saq = float(self.tela_sacar.lineEdit_2.text())
        conexao = self.ban.criando_conexao(
                            'localhost',
                            'root',
                            '12345',
                            'banco',
                        )
        cursor= conexao.cursor()
        cursor.execute(f"select * from clientes where usuario = '{login}'")
        valor = cursor.fetchall()
        convert_lista= list(valor)
        texto= str(valor_saq)

        if (convert_lista):
            if not(valor_saq == ''):
                if((convert_lista[0][4]) == (login)):
                    conta =self.ban.Buscar_conta_bd(conexao,convert_lista[0][6])
                    s = conta[0][2]
                    if (s >= valor_saq):
                        QMessageBox.information(None, 'POO2', 'Saque feito com sucesso!')
                        msg=f'Saque no Valor de : {valor_saq}\n'
                        self.ban.gravar_historico(conexao,conta[0][1],msg)
                        
                        convert_conta = list(map(list, conta))
                        convert_conta[0][2] = (s - valor_saq)
                        self.tela_sacar.lineEdit_4.setText(convert_lista[0][1])
                        self.tela_sacar.lineEdit_5.setText(str(convert_conta[0][0]))
                        self.tela_sacar.lineEdit_3.setText('R$ ' + str(convert_conta[0][2]))
                        self.tela_menu.lineEdit.setText('R$ ' + str(convert_conta[0][2]))


                        alterar_saldo = (f'UPDATE `banco`.`contas` SET saldo = {convert_conta[0][2]} WHERE (numero = {conta[0][0]});')
                        self.ban.executando_query(conexao, alterar_saldo)
                        
                    else:
                        QMessageBox.information(None, 'POO2', 'Saldo insuficiente!')
            else:
                QMessageBox.information(
                    None, 'POO2', 'Todos os campos devem ser preenchidos!')

    # chamada para a tela de transferencia
    def botaoTransferir(self):
        """ Função para realizar transferência"""

        conta_destino = self.tela_transferir.lineEdit.text()
        valor = self.tela_transferir.lineEdit_2.text()
        conexao = self.ban.criando_conexao(
                    'localhost',
                    'root',
                    '12345',
                    'banco',
                )

        cs = self.tela_login.lineEdit.text()
        buscar_conta = self.ban.Buscar_conta_bd_login(conexao,cs) #retorna a chave primaria da conta que é o cpf
        Busca_conta_de_destino = self.ban.retorna_dado_conta(conexao,'cpf_titular','numero',conta_destino)
        if not( conta_destino == '' or valor == ''):
            if (buscar_conta[0][0] != None):
                if(Busca_conta_de_destino):
                    
                    self.ban.transferirBD(conexao,Busca_conta_de_destino[0][0],cs,float(valor))
                    cs =self.ban.Buscar_conta_bd(conexao,buscar_conta[0][1])
                    QMessageBox.information(None, 'POO2', 'Transferencia feita com sucesso')
                    self.tela_transferir.lineEdit_4.setText('R$ ' + str(cs[0][2]))
                    self.tela_menu.lineEdit.setText('R$ ' + str(cs[0][2]))
                else:
                    QMessageBox.information(None, 'POO2', 'Conta de destino não existe!')
            else:
                QMessageBox.information(None, 'POO2', 'Conta de saída não existe!')
        else:
            QMessageBox.information(None, 'POO2', 'Todos os campos devem ser preenchidos!')
# chamada para tela de extrato

    def botaoExtrato(self):
        """ Função para informar o extrato"""
        login = self.tela_login.lineEdit.text()
        conexao = self.ban.criando_conexao(
                            'localhost',
                            'root',
                            '12345',
                            'banco',
                        )
        q1 = (f"select * from clientes where usuario = '{login}'")
        dados = self.ban.lendo_dados(conexao, q1)
        lista = list(dados)
        conta = self.ban.Buscar_conta_bd(conexao,lista[0][6])
        convert_conta = list(conta)
        self.tela_extrato.textBrowser.setText("Numero Conta: {} \nSaldo Disponível: {}".format(convert_conta[0][0], convert_conta[0][2]))
    
# chamada para a tela historico

    def botaoHistorico(self):
        """ Função para informar o histórico"""
        login = self.tela_login.lineEdit.text()
        conexao = self.ban.criando_conexao(
                            'localhost',
                            'root',
                            '12345',
                            'banco',
                        )
        q1 = (f"select * from clientes where usuario = '{login}'")
        dados = self.ban.lendo_dados(conexao, q1)
        lista = list(dados)
        conta = self.ban.Buscar_conta_bd(conexao,lista[0][6])
        convert_conta = list(conta)
    

        self.tela_historico.textBrowser.setText(str(convert_conta[0][4]))



if __name__ == "__main__":

    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())