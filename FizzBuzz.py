x = 1
import time
while True:
	if x%15 == 0:
		print("FizzBuzz")
	elif x%3 == 0:
		print("Fizz")
	elif x%5 == 0:
		print("Buzz")
	else:
		print(x)
	x+=1
	x*=x*x
	
