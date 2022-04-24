from operator import concat
import socket
from classBanco import Banco
from classCadastro import Cadastro
import datetime
from tratamento import concatenar_operacao, replace_dados, v_int, v_float, md5_generator
import hashlib

import threading

class cliente_Thread(threading.Thread):

    def __init__(self, addr, socket, sinc):
        threading.Thread.__init__(self)
        self.conex = socket
        self.sinc = sinc
        print(f"Nova conexao de: {addr}")

    def run(self) -> None:
        """CRIANDO O BANCO DE DADOS E AS TABELAS"""
        cad = Cadastro()
        ban = Banco()
        database_query = "CREATE DATABASE IF NOT EXISTS banco"
        conexao = ban.criando_conexao('localhost', 'root', 'daniel398', 'banco')

        ban.criando_bancodedados(conexao, database_query)

        tabela_clientes = "CREATE TABLE IF NOT EXISTS clientes( cpf bigint(11)  PRIMARY KEY, nome VARCHAR(50) NOT NULL , endereco VARCHAR(50) NOT NULL, nascimento VARCHAR(50) NOT NULL, usuario VARCHAR(50) NOT NULL, senha VARCHAR(50) NOT NULL, conta bigint(11), data_abertura TEXT);"
        ban.executando_query(conexao, tabela_clientes)

        tabela_contas = "CREATE TABLE IF NOT EXISTS contas( numero int(5) NOT NULL , cpf_titular bigint(11)  PRIMARY KEY, saldo FLOAT(5,2) NOT NULL, limite VARCHAR(50) NOT NULL, historico TEXT DEFAULT NULL);"
        ban.executando_query(conexao, tabela_contas)

        alter_cli_con = """ALTER TABLE clientes ADD FOREIGN KEY(conta) REFERENCES contas(cpf_titular);"""
        ban.executando_query(conexao, alter_cli_con)

        sessao = ''

        msg_recebida = '' 
        while(msg_recebida != 'encerrar'):
            msg_recebida = self.conex.recv(1024).decode()
            print(f'{msg_recebida}')
            operacao = msg_recebida.split(',')

            if(operacao[0] == '1'): #cadastrar conta [1, numero, cpf_titular, saldo, limite]]
                conexao = ban.criando_conexao('localhost','root','daniel398','banco',)
                numero = v_int(operacao[1])
                cpf_titular = v_int(operacao[2])
                saldo = v_float(operacao[3])
                limite = operacao[4]

                cliente = ban.Buscar_cliente_bd(conexao,cpf_titular)
                conta = ban.Buscar_conta_bd(conexao,cpf_titular)
                teste= ban.retorna_dado_conta(conexao,numero,cpf_titular,2)
                
                now = datetime.datetime.utcnow()
                if (cliente != None):
                    self.sinc.acquire()
                    if(conta == None):
                        ban.gravar_abertura_conta(conexao,cliente[0][0],now.strftime('%Y-%m-%d %H:%M:%S'))
                        inserindo_contas = f"INSERT INTO contas (numero, cpf_titular, saldo, limite) VALUES ({numero}, {cpf_titular}, {saldo}, {limite})"
                        ban.executando_query(conexao, inserindo_contas)
                        ban.InserirConta_cliente(conexao,cpf_titular)
                        self.conex.send('0, Cadastro realizado com sucesso!'.encode())
                    else:
                        self.conex.send('1, Essa conta já existe!'.encode())
                else:
                    self.conex.send('1, Cliente não cadastrado'.encode())
                self.sinc.release()

            elif(operacao[0] == '2'): #cadastrar cliente [2, nome1, endereco2, cpf3, nascimento4, usuario5, senha6]
                conexao = ban.criando_conexao('localhost','root','daniel398','banco',)

                nome = str(operacao[1])
                endereco = str(operacao[2])
                cpf = v_int(operacao[3])
                nascimento = str(operacao[4])
                usuario = str(operacao[5])
                senha = operacao[6]

                buscar = ban.Buscar_cliente_bd(conexao, cpf)
                if(buscar == None):
                    self.sinc.acquire()
                    inserindo_clientes = f'INSERT INTO clientes (nome, endereco, cpf, nascimento, usuario, senha) VALUES ("{nome}","{endereco}", {cpf}, "{nascimento}","{usuario}", MD5("{senha}"))'
                    ban.executando_query(conexao, inserindo_clientes)
                    self.conex.send('0, Cadastro realizado com sucesso!'.encode())
                else:
                    self.conex.send('1, O CPF já está cadastrado!'.encode())
                self.sinc.release()
                
            elif(operacao[0] == '3'): #logar [3, login, senha]
                self.sinc.acquire()
                conexao = ban.criando_conexao('localhost','root','daniel398','banco',)
                cursor = conexao.cursor()

                login = operacao[1]
            
                valor = operacao[2]
                senha = md5_generator(valor)
                sessao = login

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
                            
                            teste = concatenar_operacao(convert_lista)
                            teste2 = concatenar_operacao(convert_conta)
                            resul = replace_dados(teste)
                            resul2 = replace_dados(teste2)
                            resultado = resul+resul2
            
                            self.conex.send(('0, Login Realizado com Sucesso!,' + resultado).encode())
                            
                        else :
                            self.conex.send('1, Dados de login incorretos'.encode())
                    else:
                        self.conex.send('1, Esse cliente não possue uma conta! Realiza um cadastro primeiro'.encode())
                else:
                    self.conex.send('1, Cliente não existe! Clique np botão cadastrar e faça seu cadastro'.encode())
                self.sinc.release()

            elif(operacao[0] == 4): #ver dados
                pass

            elif(operacao[0] == '5'): #sacar [5, login, valor_saq]
                self.sinc.acquire()
                conexao = ban.criando_conexao('localhost','root','daniel398','banco',)
                cursor= conexao.cursor()
                
                login = sessao
                valor_saq = v_float(operacao[1])

                cursor.execute(f"select * from clientes where usuario = '{login}'")
                valor = cursor.fetchall()
                convert_lista= list(valor)
                texto= str(valor_saq)

                if (convert_lista):
                    if((convert_lista[0][4]) == (login)):
                            conta = ban.Buscar_conta_bd(conexao,valor[0][0])
                            print("Entrou 2")
                            print(conta)
                            s = v_float(conta[0][2])
                            print(s)
                            if (s >= valor_saq):
                                msg=(f'Saque no Valor de : {valor_saq}\n')
                                ban.gravar_historico(conexao,conta[0][1],msg)
                                convert_conta = list(map(list, conta))
                                convert_conta[0][2] = (s - valor_saq)
                                alterar_saldo = (f'UPDATE `banco`.`contas` SET saldo = {convert_conta[0][2]} WHERE (numero = {conta[0][0]});')
                                ban.executando_query(conexao, alterar_saldo)
                                conta = ban.Buscar_conta_bd(conexao,convert_lista[0][0])
                                conta = concatenar_operacao(conta)
                                resu = replace_dados(conta)
                                self.conex.send(('0, Saque realizado com sucesso!,' +resu).encode())
                            else:
                                self.conex.send('1, Saldo Insuficiente!'.encode())
                            self.sinc.release()

            elif(operacao[0] == '6'): #depositar [6, conta_dep, valor]
                self.sinc.acquire()
                conexao = ban.criando_conexao('localhost','root','daniel398','banco',)
                
                conta_dep = ban.Buscar_conta_bd_login(conexao, sessao)
                numero_conta = conta_dep[0][0]

                valor = v_float(operacao[1])

                c = ban.retorna_dado_conta(conexao,'cpf_titular','numero', numero_conta)
                saldo = ban.retorna_dado_conta(conexao,'saldo','numero', numero_conta)
                list(saldo)
                if(c != None):
                    if not(c==None):
                    
                        ban.altera_saldo(conexao,valor,c[0][0])
                        saldo = ban.retorna_dado_conta(conexao,'saldo','numero', numero_conta)
                        saldo = concatenar_operacao(saldo)
                        conta_dep = concatenar_operacao(conta_dep)
                        resultado =  conta_dep + saldo
                        resu = replace_dados(resultado)
                        
                        self.conex.send(('0, Depósito realizado com sucesso!,' + resu).encode())
                    self.sinc.release()

            elif(operacao[0] == '7'): #transferir [7, conta_destino, valor, cs]
                self.sinc.acquire()
                conexao = ban.criando_conexao('localhost','root','daniel398','banco',)
                
                conta_destino = operacao[1]
                valor = v_float(operacao[2])
                cs = sessao

                buscar_conta = ban.Buscar_conta_bd_login(conexao, cs) #retorna a chave primaria da conta que é o cpf
                Busca_conta_de_destino = ban.retorna_dado_conta(conexao,'cpf_titular','numero',conta_destino)
                if(Busca_conta_de_destino):
                    
                    if (buscar_conta[0][0] != None):
                        
                        ban.transferirBD(conexao,Busca_conta_de_destino[0][0],buscar_conta[0][1],valor)
                        cs1 = ban.Buscar_conta_bd(conexao,buscar_conta[0][1])
                        
                        cliente = ban.Buscar_cliente_bd_login(conexao,cs1[0][1])
                        
                        cliente = concatenar_operacao(cliente)
                        cliente_replace = replace_dados(cliente)
                        cs1 = concatenar_operacao(cs1)
                        resu = replace_dados(cs1)
                        resultado = resu + cliente_replace
                        
                        self.conex.send(('0, Transferencia realizada com sucesso!,' + resultado).encode())
                    else:
                        self.conex.send('1, Conta de destino não existe'.encode())
                else:
                    self.conex.send('1, Conta de saída não existe'.encode())
                self.sinc.release()

            elif(operacao[0] == '8'): #extrato [8, login]
                self.sinc.acquire()
                conexao = ban.criando_conexao('localhost','root','daniel398','banco',)

                login = sessao

                q1 = (f"select * from clientes where usuario = '{login}'")
                dados = ban.lendo_dados(conexao, q1)
                lista = list(dados)
                conta = ban.Buscar_conta_bd(conexao,lista[0][6])
                convert_conta = list(conta)
                resu = concatenar_operacao(convert_conta)
                resultado = replace_dados(resu)
                
                self.conex.send(('0,' + resultado).encode())
                self.sinc.release()

            elif(operacao[0] == '9'): #historico [9, login]
                self.sinc.acquire()
                conexao = ban.criando_conexao('localhost','root','daniel398','banco',)

                login = sessao
                
                q1 = (f"select * from clientes where usuario = '{login}'")
                dados = ban.lendo_dados(conexao, q1)
                lista = list(dados)
                conta = ban.Buscar_conta_bd(conexao,lista[0][6])
                convert_conta = list(conta)
                teste = concatenar_operacao(lista)
                teste2 = concatenar_operacao(convert_conta)
                resul = replace_dados(teste)
                resul2 = replace_dados(teste2)
                resultado = resul+resul2
                
                self.conex.send(('0, Extrato realizado com sucesso!!,' + resultado).encode())
                self.sinc.release()

            elif(operacao[0] == '10'):#Abrir menu de de depositar
                conexao = ban.criando_conexao('localhost','root','daniel398','banco',)
                cursor= conexao.cursor()

                login = sessao
                
                cursor.execute(f"select * from clientes where usuario = '{login}'")
                valor = cursor.fetchall()

                lista = concatenar_operacao(valor)
                
                conta = ban.Buscar_conta_bd(conexao,valor[0][6])
                convert_conta = concatenar_operacao(conta)
                resultado = lista + convert_conta
                tratamento = replace_dados(resultado)  # remove aspas e () das mensagens    
                self.conex.send(('0,' + tratamento).encode())

            elif(operacao[0] == '11'):#Abrir menu de saque
                conexao = ban.criando_conexao('localhost','root','daniel398','banco',)
                login = sessao
                q1 = (f"select * from clientes where usuario = '{login}'")
                dados = ban.lendo_dados(conexao, q1)
                lista = list(dados)
                conta = ban.Buscar_conta_bd(conexao,lista[0][6])
                convert_conta = concatenar_operacao(conta)
                tratamento = replace_dados(convert_conta)
                print(tratamento)
                self.conex.send(('0,' + tratamento).encode())

            elif(operacao[0] == '12'):#Abrir menu de saque
                conexao = ban.criando_conexao('localhost','root','daniel398','banco',)
                login = sessao

                q1 = (f"select * from clientes where usuario = '{login}'")
                dados = ban.lendo_dados(conexao, q1)
                lista = list(dados)
                busca_conta = ban.Buscar_conta_bd_login(conexao,login)
                cli = concatenar_operacao(lista)
                con = concatenar_operacao(busca_conta)
                resu_cli = replace_dados(cli)
                resu_con = replace_dados(con)
                resultado = resu_cli + resu_con
                print(resultado)

                self.conex.send(('0,' + resultado).encode())

            else:
                self.conex.send('1, Operação Inválida!'.encode())

        sessao = ''
        self.conex.send('1, Conexão Encerrada!!!'.encode())



