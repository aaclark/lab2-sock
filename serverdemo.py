#!/bin/usr/python

import socket, os
from random import randint

def forward(recv, send):
# fix with poll() or select()
    recv.setblocking(0);
    try:
        part = recv.recv(2048)
    except IOError, exception:
        if exception.errno == 11:
            part = None
        else:
            raise
    if (part):
       send.sendall(part)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
''' # get random port to connect
serverPort = randint(12000,12500);
print serverPort;
'''
serverPort = 12000;
serverSocket.bind(("0.0.0.0", serverPort));
# let server reuse ports
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
serverSocket.listen(5);

while True:
    (inSocket, address) = serverSocket.accept();
    print str(address);

    child = os.fork();
    if(child != 0):
# in socket-accepting process 
        continue

# else in child process
    outSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    outSocket.connect(("www.google.com", 80))

    done = False
    while not done:
        forward(inSocket, outSocket);
        forward(outSocket, inSocket);

