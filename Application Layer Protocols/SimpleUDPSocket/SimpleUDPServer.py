# ---------------------- Simple User Datagram Protocol Server ---------------- #

# This is a simple UDP sever which receive packet at port 12000
# This server will transform lowercase sentence to uppercase sentence and send it back to the client address

# Import python low-level networking interface
from socket import *

# Specify port number
serverPort = 12000

# Create server socket using IPv4 (AF_INET) and UDP socket (SOCK_DGRAM)
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign port 12000 to the server socket explicitly
# A packet designated for this IP address at this port will be directed to this socket
serverSocket.bind(('', serverPort))

# A while loop enable the server to receive packets from client indefinitely
while True:

    # When the server receives a packet at its socket, the packet data is put into message variable
    # The packet source is put into clientAddress variable which will later be used as return address
    # The variable clientAddress contain both the client IP address and port number
    # recvfrom() take the buffer size 2048 as input
    message, clientAddress = serverSocket.recvfrom(2048)

    # Print the received message
    print(message.decode())
    
    # The message is decoded and transformed to uppercase
    modifiedMessage = message.decode().upper()

    # modifiedMessage.encode() converts the message from string type to byte type
    # serverSocket.sendto() send the encoded message, attached the client address to the message
    # and then send the resulting packet into the server socket
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

