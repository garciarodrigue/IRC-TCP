#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket
import threading
from colorama import Fore, Back, Style, init
init()

stylo = Style.BRIGHT
verde = Fore.GREEN
rojo = Fore.RED
amarillo = Fore.YELLOW
cyan = Fore.CYAN
azul = Fore.BLUE
magenta = Fore.MAGENTA

os.system("clear")

host = input(f"{amarillo}[+] ip server:{rojo} ")
port = int(input(f"{amarillo}[+] Puerto:{rojo} "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()
print(stylo + azul + f"Server Corriendo en {verde}{host}{rojo} : {verde}{port} ")


clients = []
usernames = []

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)

def handle_messages(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            username = usernames[index]
            broadcast(f"{verde}ServerBot: {cyan}{username} {rojo}Desconectado".encode('utf-8'))
            clients.remove(client)
            usernames.remove(username)
            client.close()
            break

def receive_connections():
    while True:
        client, address = server.accept()

        client.send("@NickName".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)
    
        print(azul + f"\n{verde}{username} {rojo}Conectado a {amarillo}{str(address)}")

        message = f"\n{verde}ServerBot: {azul}{username} {verde}Se Conecto Al Chat!{Fore.MAGENTA}\n".encode('utf-8')
        broadcast(message, client)
        client.send(f"\n{cyan}Te has conectado al Server{Fore.MAGENTA}\n".encode('utf-8'))
        
        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()
receive_connections()


