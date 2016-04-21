# Echo client program for IPv4 only
import socket

HOST = '192.168.0.14'    # The remote host (RPi IP)
PORT = 55005             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('7778888')
data = s.recv(1024)
s.close()
print 'Received test number:', repr(data)


