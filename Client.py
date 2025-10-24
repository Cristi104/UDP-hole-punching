import select
import socket

# server information
UDP_PORT = 5000
UDP_IP = "10.42.0.2"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))
local_addr = sock.getsockname()
print(f"Client started on local address {local_addr}")

# send a dummy message to server in order to open up an external port and get the public ip to the server
sock.sendto(b"test udp", (UDP_IP, UDP_PORT))

# receive other peer's data from the server
data, addr = sock.recvfrom(1024)
print(f'data: {data} from {addr}')
split_addr = data.decode().split(":")
new_addr = (split_addr[0], int(split_addr[1]))

connected = False
sock.setblocking(False)
while not connected:

    # send punches to peer's public ip and previously open port
    print(f"sending to {new_addr}")
    sock.sendto(b"test punch", new_addr)

    # if data is received it means that the peer got through the local nat
    ready = select.select([sock], [], [], 3)
    if ready[0]:
        data, addr = sock.recvfrom(1024)
        print(f'data: {data} from {addr}')
        connected = True

sock.setblocking(True)

# send one last message as a confirmation
sock.sendto(b"punched?", new_addr)
data, addr = sock.recvfrom(1024)
print(f'data: {data} from {addr}')
