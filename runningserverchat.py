import threading
import socket
import time
phone = socket.socket()
port = input("What port do you want to connect to?")
addr = (socket.gethostname(), int(port))
phone.bind(addr)
phone.listen(16)
def server():
	while True:
		try:
			conn, callid = phone.accept()
			message = bytes.decode(conn.recv(1024))
			conn.send("r".encode("UTF-8"))
			conn.close()
			print("Call from {0}: {1}".format(callid, message))
		except KeyboardInterrupt:
			conn.close()
			phone.close()
			break
		except:
			conn.close()
			phone.close()
			break
def client():
	cpu = input("What computer do you want to connect to? 2-17\n")
	alias = input("What do you want your alias to be?")
	while True:
		try:
			msg = (alias + ": " + input("What is the message that you want to send?\n"))
			data = msg.encode("UTF-8")
			phone = socket.socket()
			address = ("vampy-cs-" + str(cpu), int(port))
			phone.connect(address)
			phone.sendall(data)
			phone.close()
			time.sleep(0.5)
		except ConnectionRefusedError:
			print("yo u cant connect")
		except KeyboardInterrupt:
			phone.close()
			break
t1 = threading.Thread(target = server)
t2 = threading.Thread(target = client)
t1.start()
t2.start()
t1.join()
t2.join()
print("Shutting down.")
		
		

