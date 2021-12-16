# ---------------------- Simple User Datagram Protocol Client ---------------- #

# This is a simple UDP client which send message to a UDP server hosted at 192.168.0.1 port 12000
# This client will send lowercase sentence to the server and receive uppercase sentence from the server

# Import python low-level networking interface
from socket import *

# Specify server hostname and port number
serverName = '192.168.0.53'
serverPort = 12000

# Create client socket using IPv4 (AF_INET) and UDP socket (SOCK_DGRAM)
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get message from keyboard
message = input('Input lowercase sentence:')

# message.encode() converts the message from string type to byte type
# clientSocket.sendto() send the encoded message, attached the destination address to the message
# and then send the resulting packet into the client socket
# the client then wait for a reply from the server
clientSocket.sendto(message.encode(), (serverName, serverPort))

# When the client receives a packet at the client socket, the packet data is put into modifiedMessage variable
# The packet source is put into serverAddress variable
# recvfrom() take the buffer size 2048 as input
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Decode and print the message from the UDP server
print(modifiedMessage.decode())

# Close the socket and terminate the process
clientSocket.close()
