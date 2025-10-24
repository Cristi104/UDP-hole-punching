import select
import socket

UDP_PORT = 5000
UDP_IP = "10.42.0.2"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))
local_addr = sock.getsockname()
print(f"Client started on local address {local_addr}")
sock.sendto(b"test udp", (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print(f'data: {data} from {addr}')

split_addr = data.decode().split(":")
new_addr = (split_addr[0], int(split_addr[1]))
connected = False

sock.setblocking(False)
while not connected:
    print(f"sending to {new_addr}")
    sock.sendto(b"test punch", new_addr)
    ready = select.select([sock], [], [], 3)
    if ready[0]:
        data, addr = sock.recvfrom(1024)
        print(f'data: {data} from {addr}')
        connected = True

sock.setblocking(True)


sock.sendto(b"punched?", new_addr)
data, addr = sock.recvfrom(1024)
print(f'data: {data} from {addr}')
