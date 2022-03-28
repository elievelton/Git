# -*- coding: utf-8 -*-
from audioop import reverse
import string
import json
'''Verificando quantas palavras se repetem no arquivo '''
def remover(dic):
    '''
    Remove todos os elementos que possuem repeticoes menores que 16
    '''
    newDic = {key: dic[key] for key in dic if dic[key] > 16}
    return newDic

text = open("fabula.txt", "r") 
d = dict() 
for linha in text: 
    
    linha = linha.strip() #Remove os espaços no início e no final da string    
    linha = linha.lower() #converte todas as strings para minusculo    
    linha = linha.translate(linha.maketrans("", "", string.punctuation)) #remove palavras com pontuação    
    lista_de_palavras = linha.split(" ") #Divid uma string em uma lista onde cada palavra é um item de lista e coloca um espaço
  
    #Verificando cada palavra com a palavra seguinte
    for palavra in lista_de_palavras: 
        if palavra in d: 
              d[palavra] = d[palavra] + 1
        else: 
              d[palavra] = 1
              
dic2 = dict(sorted(d.items(),reverse =True, key=lambda d:d[1])) #ordeno as palavras em forma descrecente de acordo com a chave que são as repetições
cont = 0
#dic3 = remover(dic2)
print("As 3 palavras que mais se repetem são:\n")

#gravando em um arquivo json
with open('repetem.json', 'w') as fp:
    json.dump(dic2, fp, sort_keys=False, indent=4)

for key in list(dic2.keys()): 
    if(cont<3):   #Mostro apenas as 3 primeiras posições
        print(key, ":", dic2[key])
        cont+=1
text.close()
