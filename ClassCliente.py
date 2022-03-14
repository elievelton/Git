class Cliente:
    
    __slots__ = ['_nome', '_endereco','_cpf','_nascimento']
    
    def __init__(self,nome,endereco,cpf,nascimento):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._nascimento = nascimento

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

    @nome.setter
    def nome(self,novo_valor):
        self._nome = novo_valor
    @endereco.setter
    def endereco(self,novo_valor):
        self._endereco = novo_valor