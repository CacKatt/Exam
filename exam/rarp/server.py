import socket
import re

Table={
    "AA:BB:CC:DD:EE:01": "192.168.1.10",
    "AA:BB:CC:DD:EE:02": "192.168.1.11",
}

IP="127.0.0.1"
PORT=8000
ADDRESS=(IP,PORT)

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# server.sendto(mac.encode(),ADDRESS)
server.bind(ADDRESS)
data,addr=server.recvfrom(1024)
mac=data.decode()
# print(f"IP {data}")
pattern=r"^([0-9A-F]{2}:){5}[0-9A-F]{2}$"
if re.match(pattern,mac):
    data=Table.get(mac,"NOT FOUND")
    
else:
    data="INVALID"
server.sendto(data.encode(),addr)
server.close()