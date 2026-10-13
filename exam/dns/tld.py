import socket

HOST, PORT = "127.0.0.1", 8002
AUTH_ADDRESS = "127.0.0.1:8003"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
server.bind((HOST, PORT))
print(f"TLD DNS server listening on {HOST}:{PORT}")
while True:
    query, client = server.recvfrom(1024)
    domain = query.decode().strip().lower()
    print("TLD received:", domain)
    if domain.endswith(".com"):
        server.sendto(AUTH_ADDRESS.encode(), client)
    else:
        server.sendto(b"NOT_FOUND", client)
