from ClassHisto import Historico
class Conta:
    
    _contador_de_contas = 0
    __slots__ = ['_numero', '_titular','saldo', '_limite','historico']
    
    def __init__(self,numero,cliente,saldo,limite):
        self._numero = numero
        self._titular = cliente
        self.saldo = saldo
        self._limite = limite
        self.historico = Historico()
        Conta._contador_de_contas += 1

    @staticmethod
    def get_contador_de_contas():
        return print("Total de contas criadas até agora é de: {} Contas".format(Conta._contador_de_contas))
    
    @property
    
    def numero(self):
        return self._numero
        
    @property
    
    def titular(self):
        return self._numero
    
    @property
    
    def limite(self):
        return self._numero
    
    @numero.setter
    def numero(self, novo_valor):
        self._numero = novo_valor
    @titular.setter
    def titular(self, novo_valor):
        self._titular = novo_valor
    @limite.setter
    def limite(self, novo_valor):
        self._limite = novo_valor
    
    
    def deposita(self, novo_valor):
        self.saldo += novo_valor
        self.historico.transacoes.append("Depositou o valor de: {}".format(novo_valor))
                                         
    def sacar(self, novo_valor):
        if (self.saldo < novo_valor):
            return False
        else:
            self.saldo -= novo_valor
            self.historico.transacoes.append("Sacou o valor de: {}".format(novo_valor))
            return False
    
    def transfere(self, destino, valor):
        retirou = self.sacar(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("Transferiu o valor de: {} para a conta {}".format(valor, destino.numero))
            return True
    
    def extrato(self):
        print("Numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append("Tirou extrato - Saldo de: {}".format(self.saldo))