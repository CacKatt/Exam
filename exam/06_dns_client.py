import socket

SERVER = ("127.0.0.1", 5300)
domain = input("Enter domain (e.g. www.example.com): ").strip().lower()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.settimeout(5)
    client.sendto(domain.encode(), SERVER)
    try:
        answer, _ = client.recvfrom(1024)
        answer = answer.decode()
        if answer == "NOT_FOUND":
            print("Domain not found in this demo DNS database.")
        elif answer == "DNS_ERROR":
            print("DNS lookup failed. Check that all servers are running.")
        else:
            print("Resolved IP address:", answer)
    except socket.timeout:
        print("Timed out. Check that the recursive DNS server is running.")
