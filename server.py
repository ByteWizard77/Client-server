import socket
s = socket.socket()
print('Socket succesfully created')
port = 1234
s.bind(('', port))
print(f'socket binded to port{port}')
s.listen(5)
print(f'Socket now listening')
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    message = ('Thank you for connecting')
    c.send(message.encode())
    c.close()
    