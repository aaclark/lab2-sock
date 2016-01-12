#!/bin/usr/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.1", 12345))

request = "GET / HTTP/1.0\n\n"

sock.sendall(request)

done = False

while not done:
    part = sock.recv(2048)
    if (part):
        print part
    else:
        done = True
