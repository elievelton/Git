import mysql.connector
from mysql.connector import Error

import datetime
from tratamento import concatenar_operacao, replace_dados, v_int, v_float

'''Essa classe Banco tem como objetivo auxiliar  main_servidor.py'''

class Banco:
    '''Função usada para criar uma conexao com o Banco de dados'''
    def criando_conexao(self, host_name, user_name, user_passwd, db_name):
        self.conexao = None
        try:
            self.conexao = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_passwd,
                database=db_name
            )
            print("Conection Sucessful")
        except Error as err:
            print(f"Error: '{err}'")
        return self.conexao
    #funcao para criar banco de dados
    def criando_bancodedados(self, conexao, query):
        self.cursor = conexao.cursor()
        try:
            self.cursor.execute(query)
            print("Banco de dados criado com sucesso!")
            return True
        except Error as err:
            print(f"Error: '{err}'")
    #executando um query, já recebe o comando do bando de dados na variavel query
    def executando_query(self, conexao, query):
        self.cursor = conexao.cursor()
        try:
            self.cursor.execute(query)
            conexao.commit()
            print("SQL Executado!")
            return True
        except Error as err:
            print(f"Error: '{err}'")
    #lendo dados de um Banco 
    def lendo_dados(self, conexao, query):
        self.cursor = conexao.cursor()
        self.result = None
        try:
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            return self.result
        except Error as err:
            print(f"Error: '{err}'")
    #busca cliente pelo cpf
    def Buscar_cliente_bd(self, conexao, cpf):
        self.cursor = conexao.cursor()

        # filtra pelo cpf
        self.cursor.execute(
            f'SELECT * FROM clientes WHERE clientes.cpf = {cpf}')
        resultado = self.cursor.fetchall()

        if resultado:
            return list(resultado)
        else:
            None
    #busca uma conta pelo cpf
    def Buscar_conta_bd(self, conexao, cpf):
        self.cursor = conexao.cursor()

        # filtra pelo cpf
        self.cursor.execute(
            f'SELECT * FROM contas WHERE contas.cpf_titular = {cpf}')
        resultado = self.cursor.fetchall()

        if resultado:
            return list(resultado)
        else:
            None

    def Buscar_conta_bd_login(self, conexao, login):
        self.cursor = conexao.cursor()

        resultado = self.Buscar_cliente_bd_login(conexao, login)

        self.cursor.execute(
            f"SELECT * FROM contas WHERE contas.cpf_titular = {resultado[0][0]}")
        resultado2 = self.cursor.fetchall()

        if resultado2:
            return list(resultado2)
        else:
           return None

    def Buscar_cliente_bd_login(self, conexao, login):
        self.cursor = conexao.cursor()

        self.cursor.execute(
            f'SELECT * FROM clientes WHERE clientes.usuario = "{login}"')  # filtra pelo cpf
        resultado = self.cursor.fetchall()
        print(resultado)

        if resultado:
            return list(resultado)
        else:
            return None

    def InserirConta_cliente(self, conexao, cpf_titular):
        self.cursor = conexao.cursor()

        self.cursor.execute(
            f'UPDATE `banco`.`clientes` SET conta = {cpf_titular} WHERE (cpf = {cpf_titular});')
        self.conexao.commit()
       

    def logar_na_conta(self, conexao, login, senha):
        self.cursor = conexao.cursor()
        self.cursor.execute(
            f"select * from clientes where usuario = '{login}' and senha = MD5('{senha}')")
        valor = self._cursor.fetchall()
        print(valor)

    def altera_saldo(self, conexao, novo_valor, chave_de_busca):
        self.cursor = conexao.cursor()
        self.cursor.execute(
            f'SELECT * FROM contas WHERE contas.cpf_titular = {chave_de_busca}')  # filtra pelo cpf
        resultado = self.cursor.fetchall()
        list(resultado)
        saldo2 = self.retorna_dado_conta(
            conexao, 'saldo', 'cpf_titular', chave_de_busca)
        float(saldo2[0][0])
        teste = saldo2[0][0]
        float(novo_valor)

        teste += novo_valor

        self.cursor.execute(
            f'UPDATE `banco`.`contas` SET saldo = {teste} WHERE (cpf_titular = {chave_de_busca});')

        msg = f'Deposito de: {novo_valor}\n'

        self.conexao.commit()
        self.gravar_historico(conexao, chave_de_busca, msg)

    def criar_Banco(self):

        database_query = "CREATE DATABASE IF NOT EXISTS banco"
        conexao = self.criando_conexao(
            'localhost', 'root', '12345', 'banco')

        self.criando_bancodedados(conexao, database_query)

        tabela_clientes = "CREATE TABLE IF NOT EXISTS clientes( cpf bigint(11)  PRIMARY KEY, nome VARCHAR(50) NOT NULL , endereco VARCHAR(50) NOT NULL, nascimento VARCHAR(50) NOT NULL, usuario VARCHAR(50) NOT NULL, senha VARCHAR(50) NOT NULL, conta bigint(11), data_abertura TEXT);"
        self.executando_query(conexao, tabela_clientes)

        tabela_contas = "CREATE TABLE IF NOT EXISTS contas( numero int(5) NOT NULL , cpf_titular bigint(11)  PRIMARY KEY, saldo FLOAT(5,2) NOT NULL, limite VARCHAR(50) NOT NULL, historico TEXT DEFAULT NULL);"
        self.executando_query(conexao, tabela_contas)

        alter_cli_con = """ALTER TABLE clientes ADD FOREIGN KEY(conta) REFERENCES contas(cpf_titular);"""
        self.executando_query(conexao, alter_cli_con)

    def retorna_dado_conta(self, conexao, dado, atributo, parametro):
        self.cursor = conexao.cursor()

        self.cursor.execute(
            f'select {dado} from contas where {atributo} = {parametro}')

        valor = self.cursor.fetchall()
        print(valor)

        if valor == []:
            return None
        else:
            return list(valor)

    def transferirBD(self, conexao, destino, saida, valor):
        self.cursor = conexao.cursor()

        self.altera_saldo(conexao, valor, destino)

        # filtra pelo cpf
        self.cursor.execute(
            f'SELECT * FROM contas WHERE contas.cpf_titular = {saida}')
        resultado = self.cursor.fetchall()
        list(resultado)
        saldo2 = self.retorna_dado_conta(
            conexao, 'saldo', 'cpf_titular', saida)
        float(saldo2[0][0])
        teste = saldo2[0][0]
        float(valor)
        
        if(valor>teste):
            return False
        elif(valor<teste):
            return True

        teste -= valor

        self.cursor.execute(
            f'UPDATE `banco`.`contas` SET saldo = {teste} WHERE (cpf_titular = {saida});')

        self.conexao.commit()
        msg = f'Transferencia recebida de: {valor} da conta :{saida}\n'
        msg2 = f'Transferencia Feita de: {valor} para conta :{destino}\n'
        self.gravar_historico(conexao, destino, msg)
        self.gravar_historico(conexao, saida, msg2)
        self.conexao.commit()

    def altera_saldo2(self, conexao, query):
        self.cursor = conexao.cursor()
        altera_saldo = query
        try:
            self.cursor.execute(altera_saldo)
            self.conexao.commit()
            print("Saldo alterado com sucesso")
        except Error as err:
            print(f"Error: '{err}'")

    def gravar_historico(self, conexao, id, info):
        self.cursor = conexao.cursor()

        # filtra pelo cpf
        self.cursor.execute(
            f'SELECT * FROM contas WHERE contas.cpf_titular = {id}')
        resultado = self.cursor.fetchall()
        list(resultado)
        msg = str(resultado[0][4])
        msg += str(info)

        sql = 'UPDATE `banco`.`contas` SET historico = %s WHERE (cpf_titular = %s);'
        val = (msg, id)
        self.cursor.execute(sql, val)
        self.conexao.commit()

    def gravar_abertura_conta(self, conexao, id, info):
        self.cursor = conexao.cursor()
        sql = 'UPDATE `banco`.`clientes` SET data_abertura = %s WHERE (cpf = %s);'
        val = (info, id)
        self.cursor.execute(sql, val)
        self.conexao.commit()

    def tratamento_dados(self, conexao, user):
        login = user

        q1 = (f"select * from clientes where usuario = '{login}'")
        dados = self.lendo_dados(conexao, q1)
        lista = list(dados)
        busca_conta = self.Buscar_conta_bd_login(conexao, login)
        cli = concatenar_operacao(lista)
        con = concatenar_operacao(busca_conta)
        resu_cli = replace_dados(cli)
        resu_con = replace_dados(con)
        resultado = resu_cli + resu_con
        return resultado
