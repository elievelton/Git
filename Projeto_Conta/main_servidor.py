import socket
from classBanco import Banco
from classCadastro import Cadastro
import datetime

def aceita_conexoes():
    """Esse loop aguarda eternamente(infinito) requerimentos de possíveis clientes"""
    pass

def trata_cliente(client):  # Recebe o socket do cliente como argumento
    """Lida com uma única conexão de cliente."""
    pass

host = 'localhost' #Criando o nome do Host (aquele que vai receber os pedidos do cliente)
port = 8000 #Definindo número de porta
addr = (host, port) #Tupla que armazena o endereço e numero de porta

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket e define o tipo de conexao e o tipo do protocolo de comunicaço
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicializa o socket, para que possamos usar a porta novamente
serv_socket.bind(addr) #define o endereço do servidor
serv_socket.listen(10)

print('\nAGUARDANDO CONEXAO...')
conex, c = serv_socket.accept() # servidor aguarda uma conexao

"""CRIANDO O BANCO DE DADOS E AS TABELAS"""
cad = Cadastro()
ban = Banco()
database_query = "CREATE DATABASE IF NOT EXISTS banco"
conexao = ban.criando_conexao('localhost', 'root', '12345', 'banco')

ban.criando_bancodedados(conexao, database_query)

tabela_clientes = "CREATE TABLE IF NOT EXISTS clientes( cpf bigint(11)  PRIMARY KEY, nome text NOT NULL , endereco text NOT NULL, nascimento text NOT NULL, usuario text NOT NULL, senha VARCHAR(32) NOT NULL, conta bigint(11), data_abertura TEXT);"
ban.executando_query(conexao, tabela_clientes)

tabela_contas = "CREATE TABLE IF NOT EXISTS contas( numero int(5) NOT NULL , cpf_titular bigint(11)  PRIMARY KEY, saldo FLOAT(5,2) NOT NULL, limite text NOT NULL, historico text DEFAULT NULL);"
ban.executando_query(conexao, tabela_contas)

alter_cli_con = """ALTER TABLE clientes ADD FOREIGN KEY(conta) REFERENCES contas(cpf_titular);"""
ban.executando_query(conexao, alter_cli_con)

msg_recebida = '' 
while(msg_recebida != 'encerrar'):
    msg_recebida = conex.recv(1024).decode()
    print(f'{msg_recebida}')
    operacao = msg_recebida.split(',')

    if(operacao[0] == 1): #cadastrar conta [1, numero, cpf_titular, saldo, limite]]
        conexao = ban.criando_conexao('localhost','root','12345','banco',)
        numero = operacao[1]
        cpf_titular = operacao[2]
        saldo = operacao[3]
        limite = operacao[4]

        cliente = ban.Buscar_cliente_bd(conexao,cpf_titular)
        conta = ban.Buscar_conta_bd(conexao,cpf_titular)
        teste= ban.retorna_dado_conta(conexao,numero,cpf_titular,2)
        
        now = datetime.datetime.utcnow()
        if (cliente != None):
            if(conta == None):
                ban.gravar_abertura_conta(conexao,cliente[0][0],now.strftime('%Y-%m-%d %H:%M:%S'))
                inserindo_contas = f"INSERT INTO contas (numero, cpf_titular, saldo, limite) VALUES ({numero}, {cpf_titular}, {saldo}, {limite})"
                ban.executando_query(conexao, inserindo_contas)
                ban.InserirConta_cliente(conexao,cpf_titular)
                conex.send('0, Cadastro realizado com sucesso!'.encode())
            else:
                conex.send('1, Essa conta já existe!'.encode())
        else:
            conex.send('1, Cliente não cadastrado'.encode())

    elif(operacao[0] == 2): #cadastrar cliente [2, nome1, endereco2, cpf3, nascimento4, usuario5, senha6]
        conexao = ban.criando_conexao('localhost','root','12345','banco',)

        nome = operacao[1]
        endereco = operacao[2]
        cpf = operacao[3]
        nascimento = operacao[4]
        usuario = operacao[5]
        senha = operacao[6]

        buscar = ban.Buscar_cliente_bd(conexao, cpf)
        if(buscar == None):
            inserindo_clientes = f"INSERT INTO clientes (cpf, nome, endereco, nascimento, usuario, senha) VALUES ({cpf}, {nome}, {endereco}, {nascimento},{usuario}, {senha})"
            ban.executando_query(conexao, inserindo_clientes)
            conex.send('0, Cadastro realizado com sucesso!'.encode())
        else:
            conex.send('1, O CPF já está cadastrado!'.encode())
        
    elif(operacao[0] == 3): #logar [3, login, senha]
        conexao = ban.criando_conexao('localhost','root','12345','banco',)
        cursor = conexao.cursor()

        login = operacao[1]
        senha = operacao[2]

        b = ban.Buscar_cliente_bd_login(conexao, login) #retorna o cpf do cliente
        buscar_cliente= ban.Buscar_cliente_bd(conexao,b[0][0])
    
        cursor.execute(f"select * from clientes where usuario = '{login}' and senha = '{senha}'")
        valor = cursor.fetchall()
        convert_lista= list(valor)
        if(convert_lista!=None):
            if (convert_lista):
                if((convert_lista[0][4] and convert_lista[0][5]) == (login and senha)):
                    conta = ban.Buscar_conta_bd(conexao,convert_lista[0][6])
                    convert_conta = list(conta)
                else :
                    conex.send('1, Dados de login incorretos'.encode())
            else:
                conex.send('1, Esse cliente não possue uma conta! Realiza um cadastro primeiro'.encode())
        else:
            conex.send('1, Cliente não existe! Clique np botão cadastrar e faça seu cadastro'.encode())

    elif(operacao[0] == 4): #ver dados
        pass

    elif(operacao[0] == 5): #sacar [5, login, valor_saq]
        conexao = ban.criando_conexao('localhost','root','12345','banco',)
        cursor= conexao.cursor()
        
        login = operacao[1]
        valor_saq = operacao[2]

        cursor.execute(f"select * from clientes where usuario = '{login}'")
        valor = cursor.fetchall()
        convert_lista= list(valor)
        texto= str(valor_saq)

        if (convert_lista):
            if((convert_lista[0][4]) == (login)):
                    conta = ban.Buscar_conta_bd(conexao,convert_lista[0][6])
                    s = conta[0][2]
                    if (s >= valor_saq):
                        msg=f'Saque no Valor de : {valor_saq}\n'
                        ban.gravar_historico(conexao,conta[0][1],msg)
                        convert_conta = list(map(list, conta))
                        convert_conta[0][2] = (s - valor_saq)
                        alterar_saldo = (f'UPDATE `banco`.`contas` SET saldo = {convert_conta[0][2]} WHERE (numero = {conta[0][0]});')
                        ban.executando_query(conexao, alterar_saldo)
                        conex.send('0, Saque realizado com sucesso!'.encode())
                    else:
                        conex.send('1, Saldo Insuficiente!'.encode())

    elif(operacao[0] == 6): #depositar [6, conta_dep, valor]
        conexao = ban.criando_conexao('localhost','root','12345','banco',)
        
        conta_dep = operacao[1]
        valor = operacao[2]

        c = ban.retorna_dado_conta(conexao,'cpf_titular','numero', conta_dep)
        saldo = ban.retorna_dado_conta(conexao,'saldo','numero', conta_dep)
        list(saldo)
        if(c != None):
            if not(c==None):
                ban.altera_saldo(conexao,float(valor),c[0][0])
                saldo = ban.retorna_dado_conta(conexao,'saldo','numero', conta_dep)
                conex.send('0, Depósito realizado com sucesso!'.encode())

    elif(operacao[0] == 7): #transferir [7, conta_destino, valor, cs]
        conexao = ban.criando_conexao('localhost','root','12345','banco',)
        
        conta_destino = operacao[1]
        valor = operacao[2]
        cs = operacao[3]

        buscar_conta = ban.Buscar_conta_bd_login(conexao, cs) #retorna a chave primaria da conta que é o cpf
        Busca_conta_de_destino = ban.retorna_dado_conta(conexao,'cpf_titular','numero',conta_destino)
        if(Busca_conta_de_destino):
            if (buscar_conta[0][0] != None):
                ban.transferirBD(conexao,Busca_conta_de_destino[0][0],cs,float(valor))
                cs = ban.Buscar_conta_bd(conexao,buscar_conta[0][1])
                conex.send('0, Transferencia realizada com sucesso!'.encode())
            else:
                conex.send('1, Conta de destino não existe'.encode())
        else:
            conex.send('1, Conta de saída não existe'.encode())

    elif(operacao[0] == 8): #extrato [8, login]
        conexao = ban.criando_conexao('localhost','root','12345','banco',)

        login = operacao[1]

        q1 = (f"select * from clientes where usuario = '{login}'")
        dados = ban.lendo_dados(conexao, q1)
        lista = list(dados)
        conta = ban.Buscar_conta_bd(conexao,lista[0][6])
        convert_conta = list(conta)

    elif(operacao[0] == 9): #historico [9, login]
        conexao = ban.criando_conexao('localhost','root','12345','banco',)

        login = operacao[1]
        
        q1 = (f"select * from clientes where usuario = '{login}'")
        dados = ban.lendo_dados(conexao, q1)
        lista = list(dados)
        conta = ban.Buscar_conta_bd(conexao,lista[0][6])
        convert_conta = list(conta)
    else:
        conex.send('1, Operação Inválida!'.encode())
    
conex.send('1, Conexão Encerrada!!!'.encode())
serv_socket.close()
