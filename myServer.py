import socket


try :
    s= socket.socket (socket.AF_INET,socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(100)
    print (s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR))
    s.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(("", 5000))
    s.listen(5)
    connection , adder =s.accept()

    while True :
        data =connection.recv(1024)
        if not data :
            break ;
        print (data.decode("utf-8"))
        connection.send(b'hello word')
except  socket.error as e :
    print (e)

except KeyboardInterrupt:
    print ("oK !")
    