# -*- coding: utf-8 -*-
'''Classe Historico'''


import datetime
class Historico:
    def __init__(self):
        """ Função inicializadora com os atributos necessários"""
        self.data_de_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        """ Função para imprimir as transacões presente na lista criada"""
        print("Data de abertura: {}".format(self.data_de_abertura))
        print("transações: ")
        for t in self.transacoes:
            print("-",t)
        