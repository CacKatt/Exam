import socket

HOST, PORT = "127.0.0.1", 8003
RECORDS = {
    "www.example.com": "93.184.216.34",
    "mail.example.com": "192.0.2.25",
}

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))
    print(f"Authoritative DNS server listening on {HOST}:{PORT}")
    while True:
        query, client = server.recvfrom(1024)
        domain = query.decode().strip().lower()
        print("Authoritative server received:", domain)
        answer = RECORDS.get(domain, "NOT_FOUND")
        server.sendto(answer.encode(), client)
