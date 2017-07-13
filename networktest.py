import socket
host = ""
port = 8083
s = socket.socket()
information  = (host, port)
s.bind(information)
s.listen(8)
connection, address = s.accept()
print("Connection Accepted")
while True:
	data = connection.recv(1024)
	print(data[:-2].decode('utf-8'))
