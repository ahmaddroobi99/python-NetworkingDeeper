import socket

pc_name = socket.gethostname()
ipv4 = socket.gethostbyname(pc_name)

print (pc_name)
print (ipv4)

ipv4 = socket.gethostbyname("google.ps")
print (ipv4)

port = 21
service = socket.getservbyport(port )
print  (service)


service_name ="ssh"
port = socket.getservbyname(service_name)
print (port )


data  = 13252544
long_data = socket.htonl(data)
short_data =socket.htons(data)
print (long_data)
print (short_data)

s =socket.socket (socket.AF_INET ,socket.SOCK_STREAM )
s.settimeout(50 )
print (s.gettimeout())


# data ="ahnma d "
# packet_data = socket.inet_aton(data )



ip_address ="127.0.0.1"
packed_ip = socket.inet_aton(ip_address)

print (packed_ip)

from binascii import hexlify
print (hexlify(packed_ip))

ipv4  = socket.inet_ntoa(packed_ip)
print (ipv4)