import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import main_servidor, tratamento

from pytest import mark

class TestServidor:

    @mark.tratamento
    def test_v_int(self):
        valor_esperado = tratamento.v_int(50)
        assert valor_esperado == 50

    @mark.tratamento
    def test_v_float(self):
        valor_esperado = tratamento.v_float(50.5555)
        assert valor_esperado == 50.5555

    @mark.tratamento
    def test_trata_data(self):
        valor_esperado = tratamento.trata_data('20/10/2000')
        valor_esperado == '2000/10/20'

    @mark.tratamento
    def test_valida_cpf(self):
        valor_esperado = tratamento.valida_cpf('04093918325')
        assert valor_esperado == True

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

