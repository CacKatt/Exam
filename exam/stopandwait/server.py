import socket
import time
import random

addr=("127.0.0.1",8000)

server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(addr)
server.listen(1)

conn,addr=server.accept()

expected=0

while True:
    data=conn.recv(1024)
    if not data:
        break
    seq,msq=data.decode().split(":")
    seq=int(seq)
   
    if seq==expected:
        print("recived seq",seq)
        expected=1-expected
    if random.random()<0.80:
        conn.send(str(1-expected).encode())

conn.close()
server.close()