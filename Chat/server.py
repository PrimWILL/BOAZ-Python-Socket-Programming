import socket
from _thread import *


def clientthread(conn, addr):
    conn.send(b"Welcome to BOAZ chatroom!")
    while True:
        try:
            message = conn.recv(1024)
            if message:
                str_message = str(message, 'utf-8')
                print(f"<{addr[0]}> {str_message}")

                message_to_send = f"<{addr[0]}> {str_message}"
                broadcast(message_to_send, conn)
            else:
                print(f"<{addr[0]}> disconnected")
                remove(conn)
                break
        except:
            continue

def broadcast(message, conn):
    for clients in list_of_clients:
        if clients != conn:
            try:
                clients.send(bytes(message.strip(), 'utf-8'))
            except:
                clients.close()
                remove(clients)
 
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


HOST = "127.0.0.1"
PORT = 65432  # listen 할 port 번호 
list_of_clients = []
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # IPv4, TCP
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((HOST, PORT))
    s.listen(10)
 
    while True:
        conn, addr = s.accept()
        list_of_clients.append(conn)
    
        print (addr[0] + " connected")
        start_new_thread(clientthread,(conn, addr))    
 