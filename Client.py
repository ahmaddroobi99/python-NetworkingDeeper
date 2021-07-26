import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 7000
s.connect((host, port))
while True :
    data =str(input("data > "))
    s.send(data.encode("utf-8"))
    

s.close()
