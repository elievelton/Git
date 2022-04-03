import mysql.connector
from mysql.connector import Error



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
