#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import socket

def sender():
    sendersock = socket.socket()
    port = 8080
    sendersock.connect(('localhost', port))
    number = input('Please enter a number.\n')
    sendersock.send(str(number).encode('utf-8'))
    data = sendersock.recv(1024).decode('utf-8')
    return(data)
    sendersock.close()

if __name__ == "__main__":
    while True:
        print(sender())
