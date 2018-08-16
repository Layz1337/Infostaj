#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import socket

def sender(host = 'localhost', port = 8080):
    try:
        sendersock = socket.socket()
        sendersock.connect((host, port))
        number = input('Please enter a number.\n')
        sendersock.send(str(number).encode('utf-8'))
        data = sendersock.recv(1024).decode('utf-8')
        return(data)
    except ConnectionRefusedError:
        print('Connection refused')
    except ConnectionResetError:
        print('Connection Reset')
    finally:
        sendersock.close()

if __name__ == "__main__":
    while True:
        print(sender())
