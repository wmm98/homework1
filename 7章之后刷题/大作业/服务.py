import socket
import threading
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind(('localhost', 5550))
serverSock.listen(5)
print('Sever', socket.gethostbyname('localhost'), 'listening')

userDict = dict()
numlist = list()


def forward(connectionNum, sentends):
    for user in numlist:
        if user.fileno() != connectionNum:
            user.send(sentends.encode())

def receiveThread(clientConnection, connectionNum):
    nickName = clientConnection.recv(1024).decode()
    userDict[clientConnection.fileno()] = nickName
    numlist.append(clientConnection)
    print('clientConnection', connectionNum, 'has a nickName :', nickName)
    while True:
        try:
            receiveMessage = clientConnection.recv(1024).decode()
            if receiveMessage:
                print(userDict[connectionNum], ': ', receiveMessage)
                forward(connectionNum, userDict[connectionNum]+' :' + receiveMessage)
        except(OSError, ConnectionError):
            pass
            clientConnection.close()
            return

while True:
    connectionSocket, addr = serverSock.accept()
    connectionSocket.send('welcome to server!')
    mythread = threading.Thread(target=receiveThread, args=(connectionSocket.fileno()))
    mythread.setDaemon(True)
    mythread.start()
