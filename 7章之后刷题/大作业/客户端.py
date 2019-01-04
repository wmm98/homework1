import socket
import threading
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(('服务器ip ', 5550))
print(clientSock.recv(1024).decode())
nickName = input('input you nickname: ')
clientSock.send(nickName.encode())

def sendThread():
    while True:
        try:
            sentends = input()
            clientSock.send(sentends.encode())
        except ConnectionError:
            print('Server closed this connection! or Server is closed!')

def receiveThread():
    while True:
        try:
            sentends = clientSock.recv(1024)
            if sentends:
                print(sentends.decode())
            else:
                pass
        except ConnectionError:
            print("Server closed this connection! or Server is closed!")

th1 = threading.Thread(target=sendThread)
th2 = threading.Thread(target=receiveThread)
threads = [th1, th2]
for t in threads:
    t.setDaemon(True)
    t.start()
t.join()