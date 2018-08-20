#! /usr/bin/python3
# -*- coding: UTF-8 -*-
import socket


def answer(number):
    """
    Функция, возвращающая результат факторизации целого числа
    """
    if number == 1:
        return [1]
    elif number < 1:
        raise ValueError
    delit = list()
    d = 2
    while d*d <= number:
        while number%d == 0:
            number = int(number/d)
            delit.append(d)
        d += 1
    if number > 1:
        delit.append(number)
    return delit 


def listener(port = 8080):
    """
    Функция, создающая сокет "на прослушивание".

    listener(<port>) -- где переменная port задает порт для создания сокета
    """
    serversock = socket.socket()
    serversock.bind(("", port))
    serversock.listen(10)
    while True:
        conn, addr = serversock.accept()
        conn.settimeout(60)
        try:
            data = int(conn.recv(1024).decode('utf-8'))
            data = answer(data)
            conn.send(str(data).encode('utf-8'))
        except ValueError:
            conn.send('Invalid number. Try again.\n'.encode('utf-8'))
        except Exception as exc:
            print(exc)
        finally:
            conn.close()

if __name__ == "__main__":
    listener()
