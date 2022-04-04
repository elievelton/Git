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
        print("Data de abertura: {}\n".format(self.data_de_abertura.strftime("%Y-%m-%d %H:%")))
        print("transações: \n")
        for t in self.transacoes:
            print("-\n",t)
        
        