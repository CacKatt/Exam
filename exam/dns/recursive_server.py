address=("127.0.0.1",8000)

ROOT=("127.0.0.1",8001)

def ask(domain,server_addr):
     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(TIMEOUT)
        sock.sendto(domain.encode(), server_address)
        data, _ = sock.recvfrom(1024)
        data=data.decode()
        ip,port=data.split(":")
        return zip(ip,int(port))

server=socket.socket(socket.AF_INET,socket.socket.SOCK_DGRAM)
server.bind(address)

while True:
    query,client=server.recvfrom(1024)
    domain=query.decode().strip().lower()

    try:
        print("1")
        tld_addr=ask(domain,ROOT)
        if tld_addr=="NOT FOUND":
            print("2")
            print("TLD not found")
        else:
            print("3")
            auth_addr=ask(domain,tld_addr)
            if auth_addr=="NOT FOUND":
                print("AUTH not found")
            else:
                answer=ask(domain,auth_addr)
        print(4)
    except socket.timeout:
        print("timeout try again")
        answer="ERROR"
    server.sendto(answer.decode(),client)