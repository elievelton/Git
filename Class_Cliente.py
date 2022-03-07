class Cliente:
    
    __slots__ = ['_nome', '_sobre_nome','_cpf']
    
    def __init__(self,nome,sobre_nome,cpf):
        self._nome = nome
        self._sobre_nome = sobre_nome
        self._cpf = cpf

    @property

    def nome(self):
        return self._nome

    @property

    def sobre_nome(self):
        return self._sobre_nome

    @property

    def cpf(self):
        return self._cpf

    @nome.setter
    def nome(self,novo_valor):
        self._nome = novo_valor
    @sobre_nome.setter
    def sobre_nome(self,novo_valor):
        self._sobre_nome = novo_valor
    @cpf.setter
    def cpf(self,novo_valor):
        self._cpf = novo_valor