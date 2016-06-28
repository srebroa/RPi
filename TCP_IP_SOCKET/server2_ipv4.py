# Echo server program - send data in loop from Client
import socket
from threading import *

HOST = ''                 # Symbolic name meaning the local host
PORT = 55005              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print('Client sent:', self.sock.recv(1024).decode())
            self.sock.send(b'got it')
			
s.listen(5)
print ('server started and listening')

while 1:
    clientsocket, addr = s.accept()
    print 'Connected by', addr
    data = clientsocket.recv(1024)
    if not data: break
    print 'I got the following data:', repr(data)
    clientsocket.send(data+"test")
clientsocket.close()

