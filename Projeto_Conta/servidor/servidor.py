import socket
import threading

from main_servidor import cliente_Thread

host = 'localhost' #Criando o nome do Host (aquele que vai receber os pedidos do cliente)
port = 8000 #Definindo número de porta
addr = (host, port) #Tupla que armazena o endereço e numero de porta

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket e define o tipo de conexao e o tipo do protocolo de comunicaço
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicializa o socket, para que possamos usar a porta novamente
serv_socket.bind(addr) #define o endereço do servidor
serv_socket.listen(10)

print('\nAGUARDANDO CONEXAO...')

while True:
    conex, c = serv_socket.accept() # servidor aguarda uma conexao

    sinc = threading.Lock()
    New_Thread = cliente_Thread(c, conex, sinc)
    New_Thread.start()