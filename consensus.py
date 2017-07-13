import socket
import threading
import turtle
import graph
import time
import MMMMM
import random

mycolor = "#{0:06x}".format(random.randint(0x000000, 0xffffff))
mycpu = int(input("What is your computer number? "))

def COLMSG(cpu, color):
	"""
	Returns a properly formatted COLMSG message for the given cpu and color.
	"""
	return "COLMSG\t{0}\t{1}\t{2}".format(cpu, time.time(), color)
		

def CMDMSG(color):
	"""
	Returns a properly formatted CMDMSG message for the given color.
	"""
	return "CMDMSG\t{0}".format(color)

def client():
	"""
	Run a heartbeat telling my neighbors what my color is.
	"""
	global mycolor
	global mycpu
	while True:
		for N in graph.neighbors[mycpu]:
			msg = COLMSG(mycpu, mycolor)
			addr = ("vampy-cs-"+str(N), 8080)
			data = msg.encode("UTF-8")
			phone = socket.socket()
			try:
				print("Client: Sending a COLMSG to {0}".format(N))
				phone.connect(addr)
				phone.send(data)
				phone.close()
			except ConnectionRefusedError:
				pass # do nothing
				
			time.sleep(.1)
			
		time.sleep(10)

def server():
	global mycolor
	global mycpu
	addr  = (socket.gethostname(), 8080)
	store = socket.socket()
	store.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	store.bind(addr)
	store.listen(128)
	turtle.resetscreen()
	turtle.bgcolor(mycolor)
	clrdic = {}
	# 1. create a socket for port 8080
	# 2. listen for 128 that'll be good
	# 3. turtle
	# 4. when we get a COLMSG from neighbor n with color c and time t:
	#	1. if n not in clrdic or t > clrdic[n][1]:
	#		1. clrdic[n] = (c, t)
	#	2. if len(clrdic) = len(my neighbors):
	#		1. find the recommended color x
	#		2. send a CMDMSG to my neighbors for color x who aren't already x
	# 5. when we get a CMDMSG with color c:
	#	1. change mycolor to c
	#	2. update the turtle bg
	#	3. send a COLMSG to my neighbors
	while True:
		phone, cid = store.accept()
		msg = bytes.decode(phone.recv(1024))
		phone.close()
		data = msg.strip().split("\t")
		header = data[0]
		print("Server: Received the msg: {0}".format(msg))
		if header == "COLMSG":
			cpu = int(data[1])
			utime = float(data[2])
			color = data[3]
			if cpu not in clrdic or clrdic[cpu][0] < utime:
				clrdic[cpu] = (utime, color)
				if len(clrdic) == len(graph.neighbors[mycpu]):
					poscols = [mycolor]
					for N in graph.neighbors[mycpu]:
						if N in clrdic: # and clrdic[N][1] != mycolor:
							poscols.append(clrdic[N][1])
						
					cmdcol = MMMMM.mode(poscols)
					if cmdcol is not None:
						mycolor = cmdcol
						for N in graph.neighbors[mycpu]:
							if N in clrdic and clrdic[N][1] != cmdcol:
								print("Server: Sending a CMDMSG to {0}: {1}".format(N, cmdcol))
								msg = CMDMSG(cmdcol)
								addr = ("vampy-cs-"+str(N), 8080)
								data = msg.encode("UTF-8")
								phone = socket.socket()
								try:
									phone.connect(addr)
									phone.send(data)
									phone.close()
								except ConnectionRefusedError:
									pass # do nothing
				
								time.sleep(.1)
				
		elif header == "CMDMSG":
			mycolor = data[1]
			turtle.bgcolor(mycolor)
			for N in graph.neighbors[mycpu]:
				print("Server: Sending a COLMSG to {0}".format(N))
				msg = COLMSG(mycpu, mycolor)
				addr = ("vampy-cs-"+str(N), 8080)
				data = msg.encode("UTF-8")
				phone = socket.socket()
				try:
					phone.connect(addr)
					phone.send(data)
					phone.close()
				except ConnectionRefusedError:
					pass # do nothing
				time.sleep(0.1)

def begin():
	t1 = threading.Thread(target=server)
	t2 = threading.Thread(target=client)
	t1.start()
	t2.start()
	print("The threads should now be running.")
	t1.join()
	t2.join()
	print("How did this happen?")

