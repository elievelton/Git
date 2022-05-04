from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import requests


try:
    
    url = 'https://www.cataimagem.com/2019/03/moderninha-pro-ou-sumup-total-qual-devo.html'
    html = urlopen(url)
    
    
except HTTPError as e:
    print(e)
except URLError:
    print("Dominio digitado incorretamente")
else:
    res = BeautifulSoup(html.read(),"html5lib")
    
    titulo = res.findAll("h3", {"class": "post-title"})# pegando o título do texto
    titulo_da_pagina =res.findAll("title")
    texto = res.findAll("div", {"class": "post-body"}) # pegando o corpo do texto
    link = res.select("body a" ) #pega os titulos dos links
    h2 = res.findAll("h2")# pega tudo que tiver em H2 que são os topicos do texto
    head = res.findAll("description") #pega o cabeçario de um site



    #mostrando o que tem dentro da variavel 
    print("------------------------------------Titulo----------------------------------------------")
    for tag in titulo:
        print(tag.getText())
    print("------------------------------------Corpo do texto----------------------------------------------")
    for tag in texto:
        print(tag.getText())
    print("------------------------------------Titulo dos links----------------------------------------------")
    for tag in link:
        print(tag)# mostra o link
        print(tag.getText()) #mostra o titulo
    print("------------------------------------Tag H2----------------------------------------------")
    for tag in h2:
        print(tag.getText())
    print("------------------------------------Tag Head----------------------------------------------")
    for tag in head:
        print(tag.getText())
    print("------------------------------------Titulo da pagina----------------------------------------------")
    print(titulo_da_pagina)

 