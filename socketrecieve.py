import socket
phone = socket.socket()
addr = (socket.gethostname(), 9000)
phone.bind(addr)
phone.listen(3)
while True:
	try:
		conn, callid = phone.accept()
		message = bytes.decode(conn.recv(1024))
		conn.send("r".encode("UTF-8"))
		print("Call from {0}: {1}".format(callid, message))
	except KeyboardInterrupt:
		conn.close()
		phone.close()
		break
	except:
		conn.close()
		phone.close()
		break
		
		

