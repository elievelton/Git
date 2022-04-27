
import mysql.connector


#conexãoBD
conexao = mysql.connector.connect(
    host ='localhost', 
    database = 'cadastro',
    user ='root', 
    password ='12345'
    
    )
cursor = conexao.cursor()

#criando uma base de caddados chamada cadastro
def criarBd():
    cursor.execute("CREATE DATABASE IF NOT EXISTS cadastro")
    print("Banco de dados criado com sucesso\n")

#criando Tabelas no banco de dados Cadastro para
def criarTabelas():
    cursor.execute("CREATE TABLE If NOT EXISTS usuarios (id int AUTO_INCREMENT PRIMARY KEY ,nome TEXT, senha TEXT, email TEXT);")
#Removendo dados do BD
def removerDado():
    id=(int(input("Digite o ID para remover")))

    sql= f"DELETE FROM usuarios WHERE id = {id}"
    cursor.execute(sql)
    
    conexao.commit()
    print("Dado removido com sucesso!")

#mostra o resultado de um busca por ID
def mostrar():

    id=(int(input("Digite o Id de quem você quer buscar: ")))

    cursor.execute("SELECT * FROM usuarios")
    #resultado = cursor.fetchall()#retorna uma lista com todos os usuarios do banco de dados cadastrados
    resultado = cursor.fetchmany(id) #retorna apenas o elemento com id apresentado
    #print(resultado)

    lista =[]
    #percorrendo  a lista resultado e adionando os elementos em uma nova lista para pegar só o usuario buscado
    for x in resultado[id-1]:
        lista.append(x)
    for i in lista:
        print(i)


  

#inserindo dados
def inserirDados():
    nome = input("Cadastrar Login: ")
    senha = input("Cadastrar Senha: ")
    email = input("Cadastrar email: ")
    print("Dados inseridos com sucesso no BD!\n")

    comando_Sql= "INSERT INTO usuarios (nome, senha,email) VALUES (%s, MD5(%s),%s)"
    val = (nome, senha, email)
    cursor.execute(comando_Sql,val)
    conexao.commit()



removerDado()
#inserirDados()
#mostrar()