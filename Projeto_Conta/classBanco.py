import mysql.connector
from mysql.connector import Error
from classHisto import Historico
from classConta import Conta
from classCliente import Cliente
import datetime


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

        self.cursor.execute(f'SELECT * FROM clientes WHERE clientes.cpf = {cpf}') #filtra pelo cpf
        resultado = self.cursor.fetchall()

        if resultado:
            return list(resultado)
        else:
            None


    def Buscar_conta_bd(self,conexao,cpf):
        self.cursor = conexao.cursor()

        self.cursor.execute(f'SELECT * FROM contas WHERE contas.cpf_titular = {cpf}') #filtra pelo cpf
        resultado = self.cursor.fetchall()

        if resultado:
            return list(resultado)
        else:
            None

    def Buscar_conta_bd_login(self,conexao,login):
        self.cursor = conexao.cursor()

        resultado = self.Buscar_cliente_bd_login(conexao,login)

        self.cursor.execute(f'SELECT * FROM contas WHERE contas.cpf_titular = {resultado[0][0]}')
        resultado2= self.cursor.fetchall()

        if resultado2:
            return list(resultado2)
        else:
            None
    
    def Buscar_cliente_bd_login(self,conexao,login):
        self.cursor = conexao.cursor()

        self.cursor.execute(f'SELECT * FROM clientes WHERE clientes.usuario = {login}') #filtra pelo cpf
        resultado = self.cursor.fetchall()

        if resultado:
            return list(resultado)
        else:
            None      

    def InserirConta_cliente(self,conexao,cpf_titular):
        self.cursor = conexao.cursor()

        self.cursor.execute(f'UPDATE `banco`.`clientes` SET conta = {cpf_titular} WHERE (cpf = {cpf_titular});')
        self.conexao.commit()
        #cliente = self.Buscar_cliente_bd(conexao,cpf_titular)
        #return cliente
    
    def logar_na_conta(self,conexao,login,senha):
        self.cursor = conexao.cursor()
        self.cursor.execute(f"select * from clientes where usuario = '{login}' and senha = MD5('{senha}')")
        valor = self._cursor.fetchall()
        print(valor)

    def altera_saldo(self,conexao,novo_valor,chave_de_busca):
        self.cursor = conexao.cursor()
        self.cursor.execute(f'SELECT * FROM contas WHERE contas.cpf_titular = {chave_de_busca}') #filtra pelo cpf
        resultado = self.cursor.fetchall()
        list(resultado)
        saldo2 = self.retorna_dado_conta(conexao,'saldo','cpf_titular',chave_de_busca)
        float(saldo2[0][0])
        teste=saldo2[0][0]
        float(novo_valor)
        
        teste+=novo_valor
    
        
        self.cursor.execute(f'UPDATE `banco`.`contas` SET saldo = {teste} WHERE (cpf_titular = {chave_de_busca});')
  
        msg=f'Deposito de: {novo_valor}\n'

        self.conexao.commit()
        self.gravar_historico(conexao,chave_de_busca,msg)
        





    def retorna_dado_conta(self,conexao,dado,atributo,parametro):
        self.cursor = conexao.cursor()



        self.cursor.execute(f'select {dado} from contas where {atributo} = {parametro}')

        valor = self.cursor.fetchall()
        print(valor)

        if valor == []:
            return None
        else:
            return list(valor)

    def transferirBD(self,conexao,destino,saida,valor):
        self.cursor = conexao.cursor()

        self.altera_saldo(conexao,valor,destino)

    
        self.cursor.execute(f'SELECT * FROM contas WHERE contas.cpf_titular = {saida}') #filtra pelo cpf
        resultado = self.cursor.fetchall()
        list(resultado)
        saldo2 = self.retorna_dado_conta(conexao,'saldo','cpf_titular',saida)
        float(saldo2[0][0])
        teste=saldo2[0][0]
        float(valor)
        
        teste-=valor
        
        self.cursor.execute(f'UPDATE `banco`.`contas` SET saldo = {teste} WHERE (cpf_titular = {saida});')
    

        self.conexao.commit()
        msg=f'Transferencia no valor de: {valor}\n'
        self.gravar_historico(conexao,destino,msg)


    def altera_saldo2(self,conexao, query):
        self.cursor = conexao.cursor()
        altera_saldo = query
        try:
            self.cursor.execute(altera_saldo)
            self.conexao.commit()
            print("Saldo alterado com sucesso")
        except Error as err:
            print(f"Error: '{err}'")


    def gravar_historico(self,conexao,id,info):
        self.cursor = conexao.cursor()
        lista=[]

        sql='UPDATE `banco`.`contas` SET historico = %s WHERE (cpf_titular = %s);'
        val =(info,id)
        self.cursor.execute(sql,val)
        self.conexao.commit()



    def gravar_abertura_conta(self,conexao,id,info):
        self.cursor = conexao.cursor()
        sql='UPDATE `banco`.`clientes` SET data_abertura = %s WHERE (cpf = %s);'
        val =(info,id)
        self.cursor.execute(sql,val)
        self.conexao.commit()   


