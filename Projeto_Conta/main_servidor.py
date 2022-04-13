import socket

def aceita_conexoes():
    """Esse loop aguarda eternamente(infinito) requerimentos de possíveis clientes"""
    pass

def trata_cliente(client):  # Recebe o socket do cliente como argumento
    """Lida com uma única conexão de cliente."""
    pass

host = 'localhost' #Criando o nome do Host (aquele que vai receber os pedidos do cliente)
port = 8000 #Definindo número de porta
addr = (host, port) #Tupla que armazena o endereço e numero de porta

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket e define o tipo de conexao e o tipo do protocolo de comunicaço
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicializa o socket, para que possamos usar a porta novamente
serv_socket.bind(addr) #define o endereço do servidor
serv_socket.listen(10)

print('\nAGUARDANDO CONEXAO...')
conexao, c = serv_socket.accept() # servidor aguarda uma conexao

msg_recebida = ''
while(msg_recebida != 'encerrar'):
    msg_recebida = conexao.recv(1024).decode()
    print(f'{msg_recebida}')
    operacao = msg_recebida.split(',')

    if(operacao[0] == 1): #cadastrar conta
        pass
    elif(operacao[0] == 2): #cadastrar cliente
        pass
    elif(operacao[0] == 3): #logar
        pass
    elif(operacao[0] == 4): #ver dados
        pass
    elif(operacao[0] == 5): #sacar
        pass
    elif(operacao[0] == 6): #depositar
        pass
    elif(operacao[0] == 7): #transferir
        pass
    elif(operacao[0] == 8): #extrato
        pass
    elif(operacao[0] == 9): #historico
        pass
    else:
        conexao.send('1, Operação Inválida!'.encode())
    
conexao.send('1, Conexão Encerrada!!!'.encode())
serv_socket.close()
