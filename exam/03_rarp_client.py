import socket

HOST = "127.0.0.1"
PORT = 5001

mac = input("Enter MAC address (e.g. AA:BB:CC:DD:EE:01): ").strip().upper()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(mac.encode())
    answer = client.recv(1024).decode()

if answer == "NOT_FOUND":
    print("No IP mapping found for that MAC address.")
else:
    print("IP address:", answer)
