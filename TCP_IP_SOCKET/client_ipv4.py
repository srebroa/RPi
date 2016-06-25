# Echo client program for IPv4 only
import socket

HOST = '192.168.0.11'    # The remote host (RPi IP)
PORT = 55005             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
try:
   s.connect((HOST, PORT))
   s.send('7778888')
except socket.error as msg:
   print 'Error code: ' + str(msg[0]) + 'Msg ' + str(msg[1])
data = s.recv(1024)
s.close()
print 'Received test number:', repr(data)


