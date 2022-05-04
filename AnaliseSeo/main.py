from classAnalise import Analise

url = input("Digite a url que você deseja analisar: ")
palavra = input('Digite a palavra que deseja buscar: ')

teste = Analise(url, palavra)

print(type(teste))