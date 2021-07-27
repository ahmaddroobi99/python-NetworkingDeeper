import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1",5000))

    while True:
        data =str(input("data >"))
        s.send(data.encode("utf-8"))
        s.sendto(data.encode("utf-8"),("127.0.0.1",5000))
        print (s.recvfrom(1024))
    s.close()

except  socket.error as e:
    print(e)

except KeyboardInterrupt:
    print("oK !")
