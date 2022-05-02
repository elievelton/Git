from io import UnsupportedOperation
import classCadastro, classCliente, classConta
import classBanco

import pytest
from pytest import mark

class TestDocument:

    @pytest.fixture #classCliente
    def cliente(self):
        cliente = classCliente.Cliente('Bruna', 'rua sao pedro', 10, '20/10/2000', 'gamesbrunaa', 123)
        return cliente

    @pytest.fixture #classCliente
    def cliente2(self):
        cliente2 = classCliente.Cliente('Weslley', 'rua sao vicente', 11, '17/10/2000', 'wesllyn', 124)
        return cliente2

    @pytest.fixture #classConta
    def Conta(self, cliente):
        conta = classConta.Conta(10, cliente, 100, 10000)
        return conta

    @pytest.fixture #classConta
    def conta2(self, cliente2):
        conta2 = classConta.Conta(11, cliente2, 100, 10000)
        return conta2

    @pytest.fixture #classBanco
    def BancoD(self):
        BancoD = classBanco.Banco()
        return BancoD

    #classConta
    def test_deposita(self, Conta):
        valor_esperado = Conta.deposita(50)
        print(valor_esperado)
        assert valor_esperado == True

    #classConta
    def test_sacar(self, Conta):
        valor_esperado = Conta.sacar(20)
        assert valor_esperado == True

    #classConta
    def test_transfere(self, Conta, conta2):
        valor_esperado = Conta.transfere(Conta, conta2, 30)
        assert valor_esperado == True
    
    #classCadastro
    def test_cadastrarCli(self, cliente):
        valor_esperado = classCadastro.Cadastro().cadastrarCli(cliente)
        assert valor_esperado == True

    #classCadastro
    def test_cadastrarCon(self, Conta):
        valor_esperado = classCadastro.Cadastro().cadastrarCon(Conta)
        assert valor_esperado == True

    #classCadastro
    def test_buscarCli(self, cliente2):
        cpf = cliente2.cpf
        valor_esperado = classCadastro.Cadastro().buscarCli(cpf)
        assert valor_esperado == None

    #classCadastro
    def test_buscarUsuario(self, cliente2):
        valor_esperado = classCadastro.Cadastro().buscarCli(cliente2.usuario)
        assert valor_esperado == None

    #classCadastro
    def test_buscarCon(self, conta2):
        valor_esperado = classCadastro.Cadastro().buscarCon(conta2.numero)
        assert valor_esperado == None

    #classCadastro
    def test_buscarConCli(self, cliente2):
        valor_esperado = classCadastro.Cadastro().buscarConCli(cliente2.usuario)
        assert valor_esperado == None

    #classCadastro
    def test_buscarCliCon(self, cliente2):
        valor_esperado = classCadastro.Cadastro().buscarCliCon(cliente2.usuario)
        assert valor_esperado == None

    @pytest.fixture #classBanco
    def test_criando_conexao(self, BancoD):
        conexao = BancoD.criando_conexao('localhost', 'root', '12345', 'banco')
        assert conexao != None
        return conexao

    #classBanco
    def test_criando_bancodedados(self, test_criando_conexao, BancoD):
        query = "CREATE DATABASE IF NOT EXISTS BANCO"
        valor_esperado = BancoD.criando_bancodedados(test_criando_conexao, query)
        assert valor_esperado == True

    #classBanco
    def test_executando_query(self, test_criando_conexao, BancoD):
        query = "CREATE TABLE IF NOT EXISTS CLIENTE (COD_CLI INT PRIMARY KEY NOT NULL, NOME VARCHAR (50));"
        valor_esperado = BancoD.executando_query(test_criando_conexao, query)
        assert valor_esperado == True

    #classBanco
    def test_Buscar_cliente_bd(self):
        pass

    #classBanco
    def test_buscar_conta_bd(self):
        pass
