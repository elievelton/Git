from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

from collections import Counter

class Analise:

    __slots__ = ['_url', '_palavra']

    def __init__(self, url, palavra):
        """ Função inicializadora com os atributos necessários"""
        self._url = url
        self._palavra = palavra

    @property
    def url(self):
        return self._url

    @property
    def palavra(self):
        return self._palavra

    def capturaInformacoes(self):
        informacoes = []
        try:
            html = urlopen(self._url)
        except HTTPError as e:
            print(e)
        except URLError:
            print("Dominio digitado incorretamente")
        else:
            res = BeautifulSoup(html.read(),"html5lib")
            titulo = res.findAll("h3", {"class": "post-title"})# pegando o título do texto body
            informacoes.append(titulo)
            titulo_da_pagina =res.findAll("title") #pega o titulo da pagina
            informacoes.append(titulo_da_pagina)
            texto = res.findAll("div", {"class": "post-body"}) # pegando o corpo do texto
            informacoes.append(texto)
            texto2 = res.findAll("p")
            informacoes.append(texto2)
            link = res.select("body a" ) #pega os titulos dos links
            informacoes.append(link)
            h2 = res.findAll("h2")# pega tudo que tiver em H2 que são os topicos do texto
            informacoes.append(h2)
            img = res.select("img") #pega o codigo de uma imagem ou varias imagens. Precisa tratar pegando tudo que tive <img alt"aqui fica o titulo da imagem
            informacoes.append(img)
            description = res.findAll("meta", {"property": "og:description"}) # pegando a descrição da pagina
            informacoes.append(description)
            
            quantidades = []
            for elemento in informacoes:
                aux = self.repetir(elemento)
                quantidades.append(aux)

            length = len(quantidades)
            valor = 0

            for x in range(length):
                valor = valor + quantidades[x]
            
            return valor
            
    def tratamento(self, elemento):
        d = list()
        for linha in elemento:
            linha = linha.strip() #Remove os espaços no incio e final da string
            linha = linha.lower() #converte todas a string para minusculo
            linha = linha.translate(linha.maketrans(",", linha.punctuation)) #remove pontuações
            d = linha.split("") #divide uma string em uma lista onde cada palavra é um item e coloca um espaço
        return d

    def repetir(self, elemento):
        palavras = self.tratamento(elemento)
        text = (Counter(palavras)) #conta os elemntos de uma string
        repetidas = text[self._palavra] #contagem da palavra escolhida
        return repetidas

