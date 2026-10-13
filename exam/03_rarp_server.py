import socket

# A small static table simulates the server's MAC-to-IP mapping.
TABLE = {
    "AA:BB:CC:DD:EE:01": "192.168.1.10",
    "AA:BB:CC:DD:EE:02": "192.168.1.11",
}

HOST = "127.0.0.1"
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"RARP server listening on {HOST}:{PORT}")

    while True:
        connection, address = server.accept()
        with connection:
            mac = connection.recv(1024).decode().strip().upper()
            print(f"Request from {address}: {mac}")
            ip = TABLE.get(mac, "NOT_FOUND")
            connection.sendall(ip.encode())
