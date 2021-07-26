import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 7000
    s.setblocking(1)
    s.bind((host, port))
    s.listen(5)
    connection, adder = s.accept()
    print("print connection fro {0}".format(adder[0]))
    while True:

        data = connection.recv(2365)
        print(data.decode("utf-8"))

except socket.error as e:
    print(e)
