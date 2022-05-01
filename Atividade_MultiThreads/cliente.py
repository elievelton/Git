import socket


ip = 'localhost'
port = 5000
addr = ((ip, port))  # neste ponto está sendo definido a tupla de endereços
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

while True:
    mensagem = input("Digite a mensagem para enviar para o servidor: ")
    client_socket.send(mensagem.encode())  # mensagem codificada e enviada
    print('Mensagem Recebida: '+client_socket.recv(1024).decode())
    if mensagem == 'sair':
        break
client_socket.close()  # Fechando a conexao
