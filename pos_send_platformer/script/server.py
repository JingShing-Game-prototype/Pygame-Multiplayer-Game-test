import socket
from _thread import *
import sys

server = socket.gethostbyname(socket.gethostname())
# using socket.gethostbyname(socket.gethostname()) automatically find ip
# server = ""
# use ipconfig in cmd to find your own ip in ipv4
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
# 2 client to connet to my server
print("Waiting for a connection, Server Started")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tuple):
    return str(tuple[0]) + "," + str(tuple[1])

pos = [(0, 0), (100, 100)]

def threaded_client(connection, player):
    # connection.send(str.encode("Connected"))
    connection.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(connection.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                reply = pos[player-1]
                # player start at 1. pos start at 0.
                print("Received: ", data)
                print("Sending: ", reply)

            connection.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost Connection")
    connection.close()

current_player = 0
while True:
    connection, address = s.accept()
    print("Connected to: ", address)

    start_new_thread(threaded_client, (connection, current_player))
    current_player += 1