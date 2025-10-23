# from time import sleep
#
# import requests
#
# sleep(10)
# res = requests.get('http://10.42.0.2:80')
# print(res.json())

import socket

UDP_PORT = 5000
UDP_IP = "10.42.0.2"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b"test udp", (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print(f'data: {data} from {addr}')

split_addr = data.split()
new_addr = (split_addr[0], int(split_addr[1]))
sock.sendto(b"test punch", new_addr)
sock.sendto(b"test punch", new_addr)

data, addr = sock.recvfrom(1024)
print(f'data: {data} from {addr}')
