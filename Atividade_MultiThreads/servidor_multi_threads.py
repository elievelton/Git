import socket
import threading


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientSocket,sinc):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        self.sinc = sinc
        print('Nova conexão: ', clientAddress)

    def run(self):
        print('Conectado de : ', clientAddress)
        msg = ''
        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()
            self.csocket.send(msg.encode())
            print('Para o cliente : ', msg)
            if msg == 'sair':
                break

            print('Cliente com endereço ',clientAddress,'Foi conectado')

if __name__=='__main__':
    localhost = ''
    port = 5000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.bind((localhost,port))
    print('Servidor iniciado!')
    print("Aguardando nova conexão..")
    while True:
        server.listen(10)
        clientsock,clientAddress = server.accept()
        sinc = threading.Lock()
         
        novathread =ClientThread(clientAddress,clientsock,sinc)
        novathread.start()