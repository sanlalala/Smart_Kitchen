#!/usr/bin/env python3

import socket
import pickle
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

HOST = '192.168.0.30'  # The server's hostname or IP address
PORT = 65432            # The port used by the server

while True:
    try:
        id, text = reader.read()

    finally:
        GPIO.cleanup()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        event = [str(id), "U_1_0"]
        data = pickle.dumps(event)
        s.sendall(data)
        data = s.recv(1024)

    print('Received', repr(data))
    time.sleep(1)
