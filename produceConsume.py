import threading
import random
import time
fruit = []
def produce():
	global fruit
	while True:
		try:
			tempfruit = random.randint(0, 100)
			fruit.append(tempfruit)
			print("I made fruit #{0}".format(tempfruit))
			time.sleep(random.uniform(0.000000000000000000000000000000000000000000001, 0.05))
		except:
			print(len(fruit))
def consume():
	global fruit
	while True:
		try:
			if len(fruit) > 0:
				tempfruit = fruit.pop(0)
				print("I ate fruit #{0}".format(tempfruit))
				time.sleep(random.uniform(0.0000001, 0.1))
		except:
			print(len(fruit))
t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t3 = threading.Thread(target=consume)
t1.start()
t2.start()
t3.start()
print("The threads should now be running.")
t1.join()
t2.join()
t3.join()
print("The threads should now be done")
