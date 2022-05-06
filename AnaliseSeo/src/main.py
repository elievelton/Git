from classAnalise import Analise

url = input("Digite a url que você deseja analisar: ")
palavra = input('Digite a palavra que deseja buscar: ')

teste = Analise(url, palavra)
teste.capturaInformacoes()
teste.resultados()