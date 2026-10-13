import socket

HOST, PORT = "127.0.0.1", 5301
TLD_ADDRESS = "127.0.0.1:5302"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))
    print(f"Root DNS server listening on {HOST}:{PORT}")
    while True:
        query, client = server.recvfrom(1024)
        domain = query.decode().strip().lower()
        print("Root received:", domain)
        # In this teaching example, all queries are referred to the .com TLD server.
        server.sendto(TLD_ADDRESS.encode(), client)
