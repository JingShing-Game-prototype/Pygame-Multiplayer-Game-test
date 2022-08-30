import socket
from _thread import *
from player import Player
import pickle

server = socket.gethostbyname(socket.gethostname())
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
# 2 client to connet to my server
print("Waiting for a connection, Server Started")

players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]

def threaded_client(connection, player):
    connection.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(connection.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                # reply = players[(player+1)%2]
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                # player start at 1. pos start at 0.
                print("Received: ", data)
                print("Sending: ", reply)

            connection.sendall(pickle.dumps(reply))
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