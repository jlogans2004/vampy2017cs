#!/usr/bin/python3

import _thread
import time
import threading

counter = 0
lock = threading.Lock()
def counterWork(name, delay):
	global counter
	while counter < 1000000000000000000000000000000000000000000000000000000000000000000000000:
		time.sleep(delay)
		lock.acquire()
		counter += 1
		print("Count: {0}, Thread: {1}".format(counter, name[7:]))
		lock.release()
_thread.start_new_thread(counterWork, ("Thread 1", 0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000001))
_thread.start_new_thread(counterWork, ("Thread 2", 0.01))
_thread.start_new_thread(counterWork, ("Thread 3", 0.010))
_thread.start_new_thread(counterWork, ("Thread 4", 0.019))
_thread.start_new_thread(counterWork, ("Thread 5", 0.091))
_thread.start_new_thread(counterWork, ("Thread 6", 0.0000001))
_thread.start_new_thread(counterWork, ("Thread 7", 0.0001))
_thread.start_new_thread(counterWork, ("Thread 8", 0.011))
_thread.start_new_thread(counterWork, ("Thread 9", 0.051))
_thread.start_new_thread(counterWork, ("Thread 10", 0.001))
_thread.start_new_thread(counterWork, ("Thread 11", 0.091))
_thread.start_new_thread(counterWork, ("Thread 12", 0.0001))
_thread.start_new_thread(counterWork, ("Thread 13", 0.0001))
_thread.start_new_thread(counterWork, ("Thread 14", 0.001))
_thread.start_new_thread(counterWork, ("Thread 15", 0.01))
