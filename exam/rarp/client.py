import socket

mac=input("Enter the mac address: ").strip().upper()

IP="127.0.0.1"
PORT=8000
ADDRESS=(IP,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(mac.encode(),ADDRESS)
data,addr=client.recvfrom(1024)

print(f"IP {data.decode()}")
client.close()