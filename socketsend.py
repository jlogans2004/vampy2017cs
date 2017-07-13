import socket
import time
import turtle
while True:
	port = input("What is the port you're trying to connect to?")
	cpu = input("What computer do you want to connect to? 2-17\n")
	alias = input("What do you want your alias to be?")
	while True:
		try:
			msg = (alias + ": " + input("What is the message that you want to send?\n"))
			data = msg.encode("UTF-8")
			phone = socket.socket()
			address = ("vampy-cs-" + str(cpu), int(port))
			phone.connect(address)
			phone.send(data)
			phone.close()
			time.sleep(0.5)
		except ConnectionRefusedError:
			print("yo u cant connect")
		except KeyboardInterrupt:
			phone.close()
			break
