'''Classe Conta'''
from classHisto import Historico

class Conta:
    
    _contador_de_contas = 0
    __slots__ = ['_numero', '_titular', '_saldo', '_limite','historico']
    
    def __init__(self, numero, cliente, saldo ,limite):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
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
        return self._titular

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def limite(self):
        return self._limite
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @limite.setter
    def limite(self, limite):
        self._limite = limite
      
    def deposita(self, novo_valor):
        if(novo_valor!=None):
            self._saldo += novo_valor            
            self.historico.transacoes.append("Depositou o valor de: {}".format(novo_valor))
        else:
            return False


    def sacar(self, novo_valor):
        if (self._saldo < novo_valor):
            return False
        else:
            self._saldo -= novo_valor
            self.historico.transacoes.append("Sacou o valor de: {}".format(novo_valor))
            return True
    
    def transfere(self, saida,destino, valor):
        retirou = self.deposita(valor)
        saida.sacar(valor)
        if (retirou == False):
            return False
        else:            
            self.historico.transacoes.append("Transferiu o valor de: {} para a conta {}".format(valor, destino.numero))
            return True
    
    def extrato(self):
        self.historico.transacoes.append("Tirou extrato - Saldo de: {}".format(self.saldo))
        return("Numero: {} \nsaldo: {}".format(self.numero, self.saldo))