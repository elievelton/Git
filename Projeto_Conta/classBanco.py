import mysql.connector
from mysql.connector import Error
from classHisto import Historico
from classConta import Conta
from classCliente import Cliente


class Banco:


    def criando_conexao(self,host_name, user_name, user_passwd, db_name):
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

    def criando_bancodedados(self,conexao, query):
        self.cursor = conexao.cursor()
        try:
            self.cursor.execute(query)
            print("Banco de dados criado com sucesso!")
        except Error as err:
            print(f"Error: '{err}'")

    def executando_query(self,conexao, query):
        self.cursor = conexao.cursor()
        try:
            self.cursor.execute(query)
            conexao.commit()
            print("SQL Executado!")
        except Error as err:
            print(f"Error: '{err}'")

    def lendo_dados(self,conexao, query):
        self.cursor = conexao.cursor()
        self.result = None
        try:
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
            return self.result
        except Error as err:
            print(f"Error: '{err}'")

    def Buscar_cliente_bd(self,conexao,cpf):
        self.cursor = conexao.cursor()

        self.cursor.execute(f'SELECT * FROM clientes WHERE clientes.cpf = {cpf}')
        resultado = self.cursor.fetchall()

        if resultado:
            return resultado
        else:
            None


    def Buscar_conta_bd(self,conexao,cpf):
        self.cursor = conexao.cursor()

        self.cursor.execute(f'SELECT * FROM contas WHERE contas.cpf_titular = {cpf}')
        resultado = self.cursor.fetchall()

        if resultado:
            return resultado
        else:
            None




