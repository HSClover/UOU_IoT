import socket
from time import ctime

BUFF = 4096 #buffer size
SERV = ("localhost", 10000) #server address

csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP socket
csock.connect(SERV) #connect to server

req = "time"

try:
    while req != "quit":
        csock.send(req.encode('utf-8'))
        res = csock.recv(BUFF) #blocking call
        print("Server Response: %s" % res.decode('utf-8'))

        req = input("New request:")
        print("New request:%s" % req)
    csock.send(req.encode('utf-8'))
    csock.close()
except KeyboardInterrupt:
    print("Program end...")
    csock.close()