#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import socket
serversock = socket.socket()


def answer(number):
    delit = list()
    d = 2
    while d*d <= number:
        while number%d == 0:
            number = number/d
            delit.append(d)
        i += 1
    if n > 1:
        delit.append(n)
    return delit 


def listener():
    #Устанавливаем порт, создаем сокет
    port = 8080
    serversock.bind(("", port))
    #Указываем количество соединений в очереди подключений
    serversock.listen(10)
    while True:
        #Принимаем соединение
        conn, addr = serversock.accept()
        #Устанавливаем таймаут ожидания для принимаемых данных
        conn.settimeout(1)
        try:
            #Принимаем информацию от клиента и конвертируем ее в int для проверки корректности
            data = int(conn.recv(1024).decode('utf-8'))
            #Применяем функцию answer, отправляем результат в байтах
            data = answer(data)
            conn.send(str(data).encode('utf-8'))
        #Исключение для проверки кореектности вводимых клиентом данных
        except ValueError:
            conn.send('Invalid number. Try again.'.encode('utf-8'))
        #Исключение для прочих непредвиденных проблем
        except Exception as exc:
            print(exc)
        #Закрываем соединение и выходим из цикла
        finally:
            conn.close()
            break
