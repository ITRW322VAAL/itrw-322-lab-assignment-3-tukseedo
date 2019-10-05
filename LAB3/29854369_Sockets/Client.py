#!/usr/bin/env python 3

import socket

HOST = '127.0.0.1' # The server's hostname or IP
POST = 9999 # The port used by the Server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, Server')
    data = s.recv(1024)

print('Received', repr(data))
