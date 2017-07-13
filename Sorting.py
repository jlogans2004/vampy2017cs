import random
def bubble(items):
	for t in range(len(items)-1):
		for i in range(len(items)-1):
			if items[i] > items[i+1]:
				items[i], items[i+1] = items[i+1], items[i]
def reverseBubble(items):
	for t in range(len(items)-1):
		for i in range(len(items)-1):
			if items[i] < items[i+1]:
				items[i], items[i+1] = items[i+1], items[i]
def mergeSort(items):
	if len(items) < 2:
		return None
	mid = int(len(items)/2)
	left = []
	right = []
	for i in range(mid):
		left.append(items[i])
	for i in range(mid, len(items)):
		right.append(items[i])
	mergeSort(left)
	mergeSort(right)
	#zipper
	L = 0
	R = 0	
	M = 0
	while L < len(left) and R < len(right):
		if left[L] < right[R]:
			items[M] = left[L]
			L += 1
			M += 1
		else:
			items[M] = right[R]
			R += 1
			M += 1
	while L < len(left):
		items[M] = left[L]
		L += 1
		M += 1
	while R < len(right):
		items[M] = right[R]
		R += 1
		M += 1
def cupidShuffle(items):			
	for i in range(len(items)):
		index = random.randint(i, len(items)-1)
		items[i], items[index] = items[index], items[i]
			



