# ------------------ Simple Transmission Control Protocol Client ----------------- #

# This is a simple TCP client which send message to a UDP server hosted at 192.168.0.1 port 12000
# This client will send lowercase sentence to the server and receive uppercase sentence from the server

# Import python low-level networking interface
from socket import *

# Specify server hostname and port number
serverName = '192.168.0.53'
serverPort = 12000

# Create client socket using IPv4 (AF_INET) and TCP socket (SOCK_STREAM)
clientSocket = socket(AF_INET, SOCK_STREAM)

# Before the client will be able to send data to the TCP server, the client first need to establish a TCP connection
# The connect function of clientSocket execute the three way handshake and establish a TCP connection with server
clientSocket.connect((serverName, serverPort))

# Get message from keyboard
message = input('Input lowercase sentence:')

# The client send the encoded message through the TCP connection that is already established with the server
# Unlike UDP, we do not need to specify the server socket address
clientSocket.send(message.encode())

# When a packet arrive from the TCP connection, the message is stored in variable modifiedSentence
modifiedSentence = clientSocket.recv(1024)

# Print the decoded message
print('From Server: ', modifiedSentence.decode())

# Close the socket, hence close the TCP connection with the server
clientSocket.close()
