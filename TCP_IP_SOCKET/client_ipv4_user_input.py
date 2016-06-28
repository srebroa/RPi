# Echo client program for IPv4 only - sending user input to the server
import socket

HOST = '192.168.0.12'    # The remote host (RPi IP)
PORT = 55005             # The same port as used by the server
socksize = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
try:
   s.connect((HOST, PORT))
   #recvdata = s.recv(socksize)
   #print(recvdata)
except socket.error as msg:
   print 'Error code: ' + str(msg[0]) + 'Msg ' + str(msg[1])
   #s.close()

print("Type data to send")   
while(1): #Setting a loop
    userInput = raw_input(">")
    s.send(userInput)
    #recvdata = s.recv(socksize)
    #print 'Received data:', repr(recvdata)
    #print(recvdata)


