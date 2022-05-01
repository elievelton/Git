from Projeto_Conta.document import classCadastro, classCliente, classConta
from Projeto_Conta.servidor import classBanco

import pytest
from pytest import mark

class TestDocument:

    @pytest.fixture
    def cliente(self):
        cliente = classCliente.Cliente('Bruna', 'rua sao pedro', 10, '20/10/2000', 'gamesbrunaa', 123)
        return cliente

    @pytest.fixture
    def cliente2(self):
        cliente2 = classCliente.Cliente('Weslley', 'rua sao vicente', 11, '17/10/2000', 'wesllyn', 124)
        return cliente2

    @pytest.fixture
    def conta(self):
        cli = self.cliente()
        conta = classConta.Conta(10, cli, 100, 10000)
        return conta

    @pytest.fixture
    def conta2(self):
        cli2 = self.cliente2()
        conta2 = classConta.Conta(11, cli2, 100, 10000)
        return conta2

    @mark.classConta
    def test_deposita(self):
        con = self.conta()
        con.deposita(50)
        valor_esperado = (con.saldo + 50)
        assert valor_esperado == con.saldo

    @mark.classConta
    def test_sacar(self):
        con = self.conta()
        con.sacar(20)
        valor_esperado = (con.saldo - 20)
        assert valor_esperado == con.saldo

    @mark.classConta
    def test_transfere(self):
        con = self.conta()
        con2 = self.conta2()
        con.transfere(con, con2, 30)
        valor_esperado = (con.saldo - 30)
        valor_esperado2 = (con2.saldo + 30)
        assert valor_esperado == con.saldo & valor_esperado2 == con2.saldo
    
    @mark.classCadastro
    def test_cadastrarCli(self):
        cli = self.cliente()
        valor_esperado = classCadastro.Cadastro.cadastrarCli(cli)
        assert valor_esperado == True

    @mark.classCadastro
    def test_cadastrarCon(self):
        con = self.conta()
        valor_esperado = classCadastro.Cadastro.cadastrarCon(con)
        assert valor_esperado == True

    @mark.classCadastro
    def test_buscarCli(self):
        cli = self.cliente()
        valor_esperado = classCadastro.Cadastro.buscarCli(cli.cpf)
        assert valor_esperado == cli.cpf

    @mark.classCadastro
    def test_buscarUsuario(self):
        cli = self.cliente()
        valor_esperado = classCadastro.Cadastro.buscarCli(cli.usuario)
        assert valor_esperado == cli.usuario

    @mark.classCadastro
    def test_buscarCon(self):
        con = self.conta()
        valor_esperado = classCadastro.Cadastro.buscarCon(con.numero)
        assert valor_esperado == con.numero

    @mark.classCadastro
    def test_buscarConCli(self):
        pass

    @mark.classCadastro
    def test_buscarCliCon(self):
        pass

    @mark.classBanco
    def test_criando_conexao(self):
        pass

    @mark.classBanco
    def test_criando_bancodedados(self):
        pass

    @mark.classBanco
    def test_executando_query(self):
        pass

    @mark.classBanco
    def test_lendo_dados(self):
        pass

    @mark.classBanco
    def test_Buscar_cliente_bd(self):
        pass

    @mark.classBanco
    def test_buscar_conta_bd(self):
        pass
