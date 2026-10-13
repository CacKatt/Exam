
import ipaddress

ip = input("Enter IP address: ")
prefix = int(input("Enter prefix: "))

network = ipaddress.ip_network(ip + "/" + str(prefix), strict=False)

first = network.network_address + 1
last = network.broadcast_address - 1

print("Network Address:", network.network_address)
print("Broadcast Address:", network.broadcast_address)
print("First Usable IP:", first)
print("Last Usable IP:", last)
