# -*- coding: utf-8 -*-

__author__ = "Elievelto $ Bruna"
__copyright__ = "Copyright 2022, Por mim"
__credits__ = ["Elievelto"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "eu também"
__email__ = "suporte@gamesbruna.com"
__status__ = "Production"

import json

dic = dict()
arquivo = open('notas.txt', 'r')
linhas = arquivo.readlines()


def calculaMedia(dic):
    '''
        Fução para tirar a média dos alunos
    '''
    for key, val in dic.items():
        dic[key] = sum(val)/3
    return dic
# ------------------------------------------------------------------------------------------------


def remover(dic):
    '''
    Remove todos os elementos que possuem nota menor que 8.0
    '''
    newDic = {key: dic[key] for key in dic if dic[key] > 8.0}
    return newDic
# ------------------------------------------------------------------------------------------------


for linha in linhas:
    alunos = linha.split()
    nome = alunos[0]
    nota = alunos[1:4]  # de onde começa e quantas notas irei pegar
    dic.update([(nome, nota)])
    dic[nome] = [float(nota) for nota in dic[nome]]
dic = calculaMedia(dic)


dic2 = dict(sorted(dic.items(), reverse=True, key=lambda x: x[1]))

for key, val in dic2.items():
    print(key, ":", round(dic2[key], 1))

dic3 = remover(dic2)

'''
Gravo em um arquivo novo chamado data apenas os 3 alunos com maiores médias
'''
with open('data.json', 'w') as fp:
    json.dump(dic3, fp, sort_keys=False, indent=4)

with open('data.json', 'r') as fp:
    data = json.load(fp)
print("\n")
print("Alunos que passaram com a Média mais alta")
print(data)

if __name__ == "__main__":
    print("Documentando")
