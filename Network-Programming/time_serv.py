import socket
import time

BUFS = 4096 #buffer size

ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP socket
ssock.bind(('', 10000)) #bind to all interfaces on port 10000
ssock.listen()  #queue size 5 by default
ssock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse address

print(f"Server ready")
try:
    while True:
        print("Waiting for new connection...")
        csock, caddr = ssock.accept() #blocking call
        print(f"Connection by {caddr}")
        req = csock.recv(BUFS) #blocking call
        req_str = req.decode('utf-8')
        while req_str != "quit":
            print("Request from client:", req_str)
            if (req_str == "time"):
                res = time.ctime()
            else:
                res = "Invalid Command"
            print("Response to client:", res)
            csock.send(bytes(res,"utf-8"))

            req = csock.recv(BUFS) #blocking call
            req_str = req.decode('utf-8')
except KeyboardInterrupt:
    print(f"\nServer end...")