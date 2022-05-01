from Projeto_Conta.servidor import *
from Projeto_Conta import *

from pytest import mark

class TestServidor:

    @mark.main_servidor
    def test_cadastrar_conta(self):
        pass

    @mark.main_servidor
    def test_cadastrar_cliente(self):
        pass

    @mark.main_servidor
    def test_login(self):
        pass

    @mark.main_servidor
    def test_sacar(self):
        pass

    @mark.main_servidor
    def test_depositar(self):
        pass

    @mark.main_servidor
    def test_transferir(self):
        pass

    @mark.main_servidor
    def test_extrato(self):
        pass

    @mark.main_servidor
    def test_historico(self):
        pass

    @mark.main_servidor
    def test_menu_depositar(self):
        pass

    @mark.main_servidor
    def test_menu_saque(self):
        pass

    @mark.main_servidor
    def test_menu_transferir(self):
        pass

    @mark.main_servidor
    def test_voltar(self):
        pass

    @mark.main_cliente
    def test_envia(self):
        pass

    @mark.main_cliente
    def test_sair(self):
        pass

    @mark.main_cliente
    def test_operacao(self):
        pass

