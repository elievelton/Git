import datetime

class Historico:
    def __init__(self):
        self.data_de_abertura = datetime.datetime.today()
        self.transacoes = []
        
    def imprime(self):
        #print("Data de abertura: {}".format(self.data_de_abertura))
        #print("transações: ")
        #for t in self.transacoes:
            #print("-",t)
        return self.transacoes