import socket

# local server port
UDP_PORT = 5000
UDP_IP = "0.0.0.0"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

addr1 = None
addr2 = None

while True:

    # get public ip and open port from peers
    data, addr = sock.recvfrom(1024)
    print(f'data: {data} from {addr}')
    if addr1 is None:
        addr1 = addr
    elif addr1 is not addr and addr2 is None:
        addr2 = addr

    # once both peers connect send each the other's public ip and port
    if addr1 is not None and addr2 is not None:
        sock.sendto(f"{addr1[0]}:{addr1[1]}".encode('utf-8'), addr2)
        sock.sendto(f"{addr2[0]}:{addr2[1]}".encode('utf-8'), addr1)
        addr1 = None
        addr2 = None

