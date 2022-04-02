import mysql.connector as mysql
from mysql.connector import Error

class Banco:
    def criando_bancodedados(conexao, query):
        cursor = conexao.cursor()
        try:
            cursor.execute(query)
            print("Banco de dados criado com sucesso!")
        except Error as err:
            print(f"Error: '{err}'")

    def criando_conexao(host_name, user_name, user_passwd, db_name):
        conexao = None
        try:
            conexao = mysql.connect(host = host_name, user = user_name, passwd = user_passwd, database = db_name)
            print("Conection Sucessful")
        except Error as err:
            print(f"Error: '{err}'")
        return conexao

    def executando_query(conexao, query):
        cursor = conexao.cursor()
        try:
            cursor.execute(query)
            conexao.commit()
            print("SQL Executado!")
        except Error as err:
            print(f"Error: '{err}'")

    def lendo_dados(conexao, query):
        cursor = conexao.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")