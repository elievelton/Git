from classCliente import Cliente

class Cadastro:
    __slots__ = ['_lista_de_pessoas', '_lista_de_contas']

    def __init__(self):
        self._lista_de_pessoas = []
        self._lista_de_contas = []
    
    def cadastrarCli(self,cliente):
        existe = self.buscarCli(cliente.cpf)
        if (existe==None):
            self._lista_de_pessoas.append(cliente)
            return True
        else:
            return False

    def cadastrarCon(self, conta):
        existe = self.buscarCon(conta.numero)
        if (existe==None):
            self._lista_de_contas.append(conta)
            return True
        else:
            return False
    
    def buscarCli(self,cpf):
        for lp in self._lista_de_pessoas:
            if (lp.cpf == cpf):
                return lp
        return None
        
    def buscarUsuario(self,usuario):
        for lp in self._lista_de_pessoas:
            if (lp.usuario == usuario):
                return lp
        return None

    def buscarCon(self, numero):
        for x in self._lista_de_contas:
            if (x.numero == numero):
                return x
        return None