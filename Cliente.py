#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket
import threading
from colorama import Fore, Back, Style, init
init()

style = Style.BRIGHT
verde = Fore.GREEN
azul = Fore.BLUE
rojo = Fore.RED
cyan = Fore.CYAN

os.system("clear")

username = input(style + verde +"\nIngresa tu NickName: "+ azul)

host = input("[+] ip del server: ")
port = int(input("[+] Puerto del server: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "@NickName":
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print(style + rojo +"\nOcurrio un Error")
            client.close
            break

def write_messages():
    while True:
        message = style + cyan + f"{username}: {input('')}"+ rojo
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()
