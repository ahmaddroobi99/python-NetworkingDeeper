import socket

pc_name = socket.gethostname()
ipv4 = socket.gethostbyname(pc_name)

print (pc_name)
print (ipv4)

ipv4 = socket.gethostbyname("google.ps")
print (ipv4)
