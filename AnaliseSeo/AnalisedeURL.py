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
    
    titulo = res.findAll("h3", {"class": "post-title"})# pegando o título
    texto = res.findAll("div", {"class": "post-body"}) # pegando o corpo do texto


    #mostrando o que tem dentro da variavel 
    for tag in titulo:
        print(tag.getText())
    
    for tag in texto:
        print(tag.getText())

 