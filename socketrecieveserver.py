
import socket
phone = socket.socket()
addr = (socket.gethostname(), 1738)
phone.bind(addr)
phone.listen(3)
while True:
	try:
		conn, callid = phone.accept()
		message = bytes.decode(conn.recv(1024))
		conn.send("r".encode("UTF-8"))
		conn.close()
		phone.connect("vampy-cs-8", 1738)
		phone.send(message.encode("UTF-8"))
		phone.connect("vampy-cs-16", 1738)
		phone.send(message.encode("UTF-8"))
		phone.connect("vampy-cs-7", 1738)
		phone.send(message.encode("UTF-8"))
		print("Call from {0}: {1}".format(callid, message))
	except KeyboardInterrupt:
		conn.close()
		phone.close()
		break
	except:
		conn.close()
		phone.close()
		break
		
		

