import socket
import threading
from time import ctime

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        req = conn.recv(1024)  # blocking call
        if not req:
            break
        print(f"Received message from {addr}: {req}")
        res = ctime()
        print(f"response message to {addr}: {res}")
        conn.sendall(res.encode('utf-8'))
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()

print(f"Server ready")
while True:
    csock, caddr = server.accept()  # blocking call
    client_thread = threading.Thread(target=handle_client, args=(csock, caddr))
    client_thread.start()