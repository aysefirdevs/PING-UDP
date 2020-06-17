from socket import*
serverSocket=socket(AF_INET,SOCK_DGRAM)
host=''
port=12345
serverSocket.bind((host,port))
while True:
    message, address = serverSocket.recvfrom(1024)
    print("[", message, "]")
    if (message.decode().startswith("ping")):
        serverSocket.sendto("pong".encode(), address)
