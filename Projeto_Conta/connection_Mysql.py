import mysql.connector


conexao = mysql.connector.connect(
    host ='localhost', 
    database = 'cadastro',
    user ='root', 
    password ='12345'
    
    )
cursor = conexao.cursor()

#criando uma base de caddados chamada cadastro
def criarBd():
    cursor.execute("CREATE DATABASE banco")

#criando Tabelas no banco de dados Cadastro para
def criarTabelas():
    cursor.execute("CREATE TABLE clientes (nome TEXT, senha TEXT)")

def inserirDados():
    nome = input("Criar Login")
    senha = input("Criar Senha")

    comando_Sql= "INSERT INTO clientes (nome, senha) VALUES (%s, MD5(%s))"
    val = (nome, senha)
    cursor.execute(comando_Sql,val)
    conexao.commit()



criarBd()