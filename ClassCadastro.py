from ClassCliente import Cliente
cliente = Cliente
class Cadastro:
    __slots__ = ['_lista_de_pessoas']
    def __init__(self):
        self._lista_de_pessoas =[]
    
    def cadastrar(self,cliente):
        existe = self.buscar(cliente.cpf)
        if (existe == None):
            self._lista_de_pessoas.append(cliente)
            return True
        else:
            return False
    
    def buscar(self,cpf):
        for lp in self._lista_de_pessoas:
            if lp.cpf ==cpf:
                return lp
        return None