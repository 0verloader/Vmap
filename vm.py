import socket

TCP_IP = 'localhost'
TCP_PORT = 1302
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', TCP_PORT))
s.listen(1)

conn, addr = s.accept()
while 1:
    print "hrthe"
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    conn.send(data)  # echo
conn.close()
