import socket

HOST = "127.0.0.1"  # 서버의 hostname 또는 ip addr
PORT = 65432  # 서버에서 열어놓은 포트번호

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")
