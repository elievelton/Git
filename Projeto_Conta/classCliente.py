'''Classe CLiente'''

class Cliente:
    
    __slots__ = ['_nome', '_endereco','_cpf','_nascimento', '_usuario', '_senha']
    
    def __init__(self, nome, endereco, cpf, nascimento, usuario, senha):
        """ Função inicializadora com os atributos necessários"""
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._nascimento = nascimento
        self._usuario = usuario #adicionado
        self._senha = senha #adicionado

    @property
    def nome(self):
        return self._nome

    @property
    def endereco(self):
        return self._endereco

    @property
    def cpf(self):
        return self._cpf

    @property
    def nascimento(self):
        return self._nascimento

    @property
    def usuario(self):
        return self._usuario

    @property
    def senha(self):
        return self._senha

    @nome.setter
    def nome(self,novo_valor):
        self._nome = novo_valor

    @endereco.setter
    def endereco(self,novo_valor):
        self._endereco = novo_valor