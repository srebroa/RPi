# Echo server program IPv4 for RPi
import socket

HOST = ''                 # Symbolic name meaning the local host
PORT = 55005              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
try:
   s.bind((HOST, PORT))
except socket.error as msg:
   print 'Error code'
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    print 'I got the following data:', repr(data)
    conn.send(data+"test")
conn.close()


