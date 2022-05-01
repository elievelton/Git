from Projeto_Conta.servidor import *
from Projeto_Conta.document import *
from Projeto_Conta import *

from pytest import mark

@mark.main_servidor
def test_cadastrar_conta():
    pass

@mark.main_servidor
def test_cadastrar_cliente():
    pass

@mark.main_servidor
def test_login():
    pass

@mark.main_servidor
def test_sacar():
    pass

@mark.main_servidor
def test_depositar():
    pass

@mark.main_servidor
def test_transferir():
    pass

@mark.main_servidor
def test_extrato():
    pass

@mark.main_servidor
def test_historico():
    pass

@mark.main_servidor
def test_menu_depositar():
    pass

@mark.main_servidor
def test_menu_saque():
    pass

@mark.main_servidor
def test_menu_transferir():
    pass

@mark.main_servidor
def test_voltar():
    pass

@mark.main_cliente
def test_envia():
    pass

@mark.main_cliente
def test_sair():
    pass

@mark.main_cliente
def test_operacao():
    pass

