import threading
import random
import time
import MMMMM
ints = []

def intsort(beginrangearray, stoprangearray):
	for x in range(beginrangearray, stoprangearray):
		ints.append(random.randint(1, 10000))
t1 = threading.Thread(target = intsort(0, 25))
t2 = threading.Thread(target = intsort(26, 50))
t3 = threading.Thread(target = intsort(51, 75))
t4 = threading.Thread(target = intsort(76, 100))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print("Maximum: {0}, Minimum: {1}, Mode: {2}, Mean: {3}".format(max(ints), min(ints), MMMMM.mode(ints), MMMMM.mean(ints)))
