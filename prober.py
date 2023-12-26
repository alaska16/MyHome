# MyHome Prober v0.1
import logging
import socket

# Temp
import random

# To figure out later: is it better to send all the data in one single "cycle" or should it close the socket every time?

# -- Variables --
t_livingroom = 0
t_room1 = 0
t_room2 = 0

# -- Réseau --
host = "127.0.0.1"
port = "11111"
sender = socket.socket()

try:
    print(f"Connecting to {host}:{port}...")
    sender.connect((host, int(port)))
    print("Connected.")
    while True:
        t_livingroom = input("Input the living room temperature: ").encode()# random.randint(0,40).to_bytes(8, byteorder='big')
        sender.send(t_livingroom)
except ConnectionRefusedError:
    print("Client couldn't connect to the server, please check your connection settings.")
