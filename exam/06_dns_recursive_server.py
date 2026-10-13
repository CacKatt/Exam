import socket

HOST, PORT = "127.0.0.1", 5300
ROOT = ("127.0.0.1", 5301)
TIMEOUT = 3


def ask(server_address, domain):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(TIMEOUT)
        sock.sendto(domain.encode(), server_address)
        data, _ = sock.recvfrom(1024)
        return data.decode()


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as recursive:
    recursive.bind((HOST, PORT))
    print(f"Recursive DNS server listening on {HOST}:{PORT}")

    while True:
        query, client = recursive.recvfrom(1024)
        domain = query.decode().strip().lower()
        print("\\nRecursive resolver received:", domain)

        try:
            print("1. Asking root server...")
            tld_address = ask(ROOT, domain)

            if tld_address == "NOT_FOUND":
                answer = "NOT_FOUND"
            else:
                host, port = tld_address.split(":")
                print("2. Asking TLD server...")
                auth_address = ask((host, int(port)), domain)

                if auth_address == "NOT_FOUND":
                    answer = "NOT_FOUND"
                else:
                    host, port = auth_address.split(":")
                    print("3. Asking authoritative server...")
                    answer = ask((host, int(port)), domain)

            print("4. Returning result to client:", answer)
        except (socket.timeout, OSError, ValueError) as error:
            answer = "DNS_ERROR"
            print("DNS lookup failed:", error)

        recursive.sendto(answer.encode(), client)
