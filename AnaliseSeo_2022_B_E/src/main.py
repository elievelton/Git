from classAnalise import Analise
'''
    Main feito apenas para coletar os inputs e 
    recebe os dados para analise
'''
url = input("Digite a url que você deseja analisar: ")
palavra = input('Digite a palavra que deseja buscar: ')

teste = Analise(url, palavra)
teste.capturaInformacoes()
teste.resultados()