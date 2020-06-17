import time
import socket
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port=12345
sure=1
clientSocket.settimeout(sure)
file=open("targethosts.txt","r")

a=1
for host in file:
    host=host.strip()
    print("#",a,".  Hedef..:" + host)
    a+=1
    sayac = 0
    while sayac < 5:
        sayac += 1
        message = "ping"
        try:
            start = time.time()
            clientSocket.sendto(message.encode('UTF-8'), (host, port))
            gelen = clientSocket.recvfrom(1024)
            end = time.time()
            print("#", sayac, ".  -->UDP..:" + str(gelen))
            print("#", sayac, ".  <--RTT..:" + "{:8.3f}".format((end - start)) + "ms")
        except socket.timeout:
            print("Paket kaybı")

clientSocket.close()