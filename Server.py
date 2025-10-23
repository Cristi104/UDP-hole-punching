# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return "test ok"
# app.run(host="0.0.0.0", port=80)
#

import socket

UDP_PORT = 5000
UDP_IP = "0.0.0.0"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

addr1 = None
addr2 = None

while True:
    data, addr = sock.recvfrom(1024)
    print(f'data: {data} from {addr}')
    if addr1 is None:
        addr1 = addr
    elif addr1 is not addr and addr2 is None:
        addr2 = addr

    if addr1 is not None and addr2 is not None:
        sock.sendto(f"{addr1[0]} {addr1[1]}".encode('utf-8'), addr2)
        sock.sendto(f"{addr2[0]} {addr2[1]}".encode('utf-8'), addr1)
        addr1 = None
        addr2 = None

