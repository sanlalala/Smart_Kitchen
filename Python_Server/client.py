#!/usr/bin/env python3

import socket
import pickle

HOST = '192.168.178.52'  # The server's hostname or IP address
PORT = 65432            # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    event = ["384192513797", "U_1_0"]
    data = pickle.dump(event)
    s.sendall(data)
    data = s.recv(1024)

print('Received', repr(data))