import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', 1309))

while True:
    message, address = serverSocket.recvfrom(1)
    message = message.upper()
    serverSocket.sendto(message, address) 
