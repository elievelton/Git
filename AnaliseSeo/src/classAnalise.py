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

            for x in quantidades:
                valor = valor + quantidades[x]
            
            return valor
            
    def tratamento(self, elemento):
        return palavras

    def repetir(self, elemento):
        palavras = self.tratamento(elemento)
        repetidas = []
        repetidas = (Counter(palavras).most_common())
        return repetidas

