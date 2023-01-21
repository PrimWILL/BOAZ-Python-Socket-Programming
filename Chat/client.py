# Python program to implement client side of chat room.
import socket
import select
import sys


HOST = "127.0.0.1"
PORT = 65432  # listen 할 port 번호 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        sockets_list = [sys.stdin, s]
        read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

        for socks in read_sockets:
            if socks == s:
                message = socks.recv(1024)
                print(str(message, 'utf-8'))
            else:
                message = sys.stdin.readline()

                s.send(bytes(message, 'utf-8'))
                sys.stdout.write("<You>")
                sys.stdout.write(message)
                sys.stdout.flush()

