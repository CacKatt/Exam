import socket

SERVER=("127.0.0.1",8000)

domain=input("Enter the domain name: ").strip().lower()

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.settimeout(5)
client.sendto(domain.encode(),SERVER)
try:
    data,addr=client.recvfrom(1024)
    data=data.decode()
    if data=="NOT FFOUND":
        print("NOT FOUND")
    elif data=="DNS_ERROR":
        print("DNS lookup failed. Check that all servers are running.")
    else:
        print("Resolved IP address:",data)
except socket.timeout:
    print("Timed out. Check that the recursive DNS server is running.")