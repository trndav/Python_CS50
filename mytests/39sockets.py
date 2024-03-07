# https://www.youtube.com/watch?v=iVZj9a4fog8&list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1&index=7
# TCP or UDP
# Server side

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket
s.bind(('127.0.0.1', 55556)) # Tuple, listen on port

s.listen() 

while True:
    client, address = s.accept() # accept - when client tries to connect
    print("Connected to {}".format(address))
    client.send("You are connected".encode())
    client.close()