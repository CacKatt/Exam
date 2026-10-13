import ipaddress

ip=input("Enter the ip address: ")
prefix=input("Enter the prefix: ")

network=ipaddress.ip_network(ip+'/'+prefix,strict=False)

first=network.network_address+1
last=network.broadcast_address-1

print(first)
print(last)