import mysql.connector as mysql
from mysql.connector import Error

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

conexao = criando_conexao('localhost', 'root', 'mikasa', 'poo2')

database_query = "CREATE DATABASE IF NOT EXISTS pooII"
criando_bancodedados(conexao, database_query)

criando_tabela1 = """CREATE TABLE IF NOT EXISTS usuarios(id integer AUTO_INCREMENT PRIMARY KEY, nome text NOT NULL, email text NOT NULL);"""
executando_query(conexao, criando_tabela1)

nome = 'bruna'
email = 'gamessbrunaa'
inserindo_tabela1 = (f'INSERT INTO usuarios (id, nome, email) VALUES (12, "{nome}", "{email}")')
executando_query(conexao, inserindo_tabela1)

q1 = """SELECT * FROM usuarios;"""
results = lendo_dados(conexao, q1)
for result in results:
    print(result)

criando_tabela2 = """CREATE TABLE IF NOT EXISTS usuarios_senha (id integer AUTO_INCREMENT PRIMARY KEY, nome text NOT NULL, senha VARCHAR(32) NOT NULL, email text NOT NULL);"""
executando_query(conexao, criando_tabela2)

senha = 'teste'

inserindo_tabela2 = (f'INSERT INTO usuarios_senha (id, nome, senha, email) VALUES (2, "{nome}", "{senha}", "{email}")')
executando_query(conexao, inserindo_tabela2)

q2 = """SELECT * FROM usuarios_senha WHERE nome = %s AND senha = MD5(%s)"""
results2 = lendo_dados(conexao, q2)
for result2 in results2:
    print(result2)
