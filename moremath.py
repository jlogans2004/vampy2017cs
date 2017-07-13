import math
def nchooseK(n, k):
	'''
	(n over k) n choose K function- n!/K!(n-K)!
	'''
	answer = math.factorial(n)/(math.factorial(k) * math.factorial(n-k))
	print(answer)
	
def gcd(a, b):
	'''
	Greatest common divisor for a and b where a > b > 0.
	'''
	if a < b:
		a, b = b, a
	def _solver(a, b):
		if b == 0:
			return a
		else:
			return _solver(b, a % b)
	return _solver(a, b)
