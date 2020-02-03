#!/usr/bin/env python3

import socket
from threading import Thread
import time
import pickle


class SocketServer(Thread):

    def __init__(self, host, port, myKitchen):
        self.host = host
        self.port = port
        self.kitchen = myKitchen
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.host, self.port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        data = pickle.loads(data)
                        print(data)
                        self.kitchen.updateTool(data)
                        data = pickle.dumps(data)
                        conn.sendall(data)

