import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', 1309))

while True:
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()
    if rand >= 4:
        serverSocket.sendto(message, address) 
