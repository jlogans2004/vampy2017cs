import math
P = int(input("How many data sets are you doing?\n"))
numbers = []
K = []
for p in range(P):
	index = (input("What is the next line of input?"))
	numbers.append(int(index[2:]))
	K.append((index[0]))
for num in numbers:
	numPrime = True
	happyPrime = True
	if num <= 1:
		print("{0} {1} NO".format(num, K[0]))
	else:
		for i in range(1, int(math.sqrt(num))):
			if num % i == 0:
				numPrime = True
			else:
				numPrime = False
				if happyPrime == True:
					print("{0} {1} NO".format(K[originalNum], originalNum))
					happyPrime = False
			
		originalNum = num
		happyPrime = False
		if numPrime == True:
			num = [str(num)]
			j = 0
			x = 0
			for i in range(len(num[j])):
				num.append(int(num[0][i])**2)
				x += int(num[0][i])**2
			num.pop(0)	
			x, num = num, x
			j += 1
			for y in range(100):
				x = 0
				j = 0
				num = [str(num)]
				for i in range(len(num[j])):
					num.append(int(num[0][i])**2)
					x += int(num[0][i])**2
				num.pop(0)
				x, num = num, x
				j += 1
				if num == 1 and happyPrime == False:
					happyPrime = True
					print("{0} {1} YES".format(K[originalNum], originalNum))
			if num != 1 and happyPrime == False:
				print("{0} {1} YES".format(K[originalNum], originalNum))
