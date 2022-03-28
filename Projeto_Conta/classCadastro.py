from classCliente import Cliente
'''Classe cadastro'''
class Cadastro:
    __slots__ = ['_lista_de_pessoas', '_lista_de_contas']

    def __init__(self):
        """ Função inicializadora com os atributos necessários"""
        self._lista_de_pessoas = []
        self._lista_de_contas = []
    
    def cadastrarCli(self,cliente):
        """ Função que cadastra os clientes no banco"""
        existe = self.buscarCli(cliente.cpf)
        if (existe==None):
            self._lista_de_pessoas.append(cliente)
            return True
        else:
            return False

    def cadastrarCon(self, conta):
        """ Função que cadastra as contas no banco"""
        existe = self.buscarCon(conta.numero)
        if (existe==None):
            self._lista_de_contas.append(conta)
            return True
        else:
            return False
    
    def buscarCli(self,cpf):
        """ Função que busca se os clientes existem no banco"""
        for lp in self._lista_de_pessoas:
            if (lp.cpf == cpf):
                return lp
        return None
#busca o usuario de login 
    def buscarUsuario(self, usuario):
        """ Função que busca se um usuario existe no banco"""
        for lp in self._lista_de_pessoas:
            if (lp.usuario == usuario):
                return lp
        return None

    def buscarCon(self, numero):
        """ Função que busca se uma conta existe no banco"""
        for x in self._lista_de_contas:
            if (x.numero == numero):
                return x
        return None
#Busca a conta de um cliente cadastrado
    def buscarConCli(self, usuario):
        x = self.buscarUsuario(usuario)
        if (x != None):
            for y in self._lista_de_contas:
                if (x.cpf == usuario):
                    return x
                else:
                    return None
#Busca o cliente de uma conta
    def buscarCliCon(self, usuario):
        x = self.buscarUsuario(usuario)
        if (x != None):
            for y in self._lista_de_contas:
                if (x.cpf == usuario):
                    return y
                else:
                    return None

