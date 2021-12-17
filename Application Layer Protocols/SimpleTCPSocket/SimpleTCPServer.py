# ---------------------- Simple Transmission Control Protocol Server ----------------------- #

# This is a simple UDP sever which receive packet at port 12000
# This server will transform lowercase sentence to uppercase sentence and send it back to the client address

# Import python low-level networking interface
from socket import *

# Specify port number
serverPort = 12000

# Create server socket using IPv4 (AF_INET) and TCP socket (SOCK_STREAM)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign port 12000 to the server socket explicitly
# A packet designated for this IP address at this port will be directed to this socket
serverSocket.bind(('', serverPort))

# This line has the server listen for TCP connection requests from the client.
# The parameter specifies the maximum number of queued connections (at least 1).
serverSocket.listen(1)

# print that the server is now ready to receive connection request
print('The server is ready to receive')

# A while loop enable the server to receive packets from client indefinitely
while True:

    # When a client knocks on this door, the program invokes the accept() method for serverSocket.
    # This will create a new socket called connectionSocket dedicated to this particular client.
    # The client and server then complete the three way handshake.
    # This establishes a TCP connection between clientSocket and connectionSocket.
    connectionSocket, address = serverSocket.accept()

    # When a packet arrive from the TCP connection, the message is decoded and stored in variable sentence
    sentence = connectionSocket.recv(1024).decode()

    # Change sentence to uppercase
    capitalizedSentence = sentence.upper()

    # Send capitalized sentence through the established TCP connection
    connectionSocket.send(capitalizedSentence.encode())

    # This close the current TCP connection
    # The while loop keep the serverSocket available to accept new connection request
    connectionSocket.close()
