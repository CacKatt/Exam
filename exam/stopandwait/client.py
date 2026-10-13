import socket
import time

addr=("127.0.0.1",8000)

client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(addr)

seq=0

for i in range(5):
    msg=input("Enter the msd: ")
    frame=f"{seq}:{msg}"

    while True:
        client.send(frame.encode())
        client.settimeout(2)

        try:
            ack=int(client.recv(1024).decode())

            if ack==seq:
                print("ACK recieved: ",ack)
                print("msg: ",msg)
                seq=1-seq
                break
        except socket.timeout:
            print("Time out")

client.close()