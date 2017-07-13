def old_exponent(n, k):
	"""
	n is base, k is exponent
	"""
	answer = 1
	for i in range(k):
		answer *= n
	print(answer)
def newExponent(n, k):
	"""
	n is base, k is exponent
	"""
	print("newExponent({0}, {1})".format(n, k))
	if k == 1: 
		return n
	elif k == 0:
		return 1
	left = int(k/2)
	right = k - left
	return newExponent(n, left) * newExponent(n, right)

