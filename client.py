#! /usr/bin/python3
# -*- coding: UTF-8 -*-
import socket
def sender(hostname = 'localhost', port = 8000):
    """
    Функция для отправки сообщения и принятия ответа  от сервера.
    Ответ возвращается в виде строки.
    
    Использование:
    sender(<host>, <port>) -- host это адрес сервера,
                              по умолчанию имеет значение 'localhost';
                              port это порт сервера,
                              по умолчанию имеет значение 8000
    """
    try:
        sendersock = socket.socket()
        sendersock.connect((hostname, port))
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
