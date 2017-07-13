import functools

num_plusses = 0

@functools.lru_cache(maxsize=None)
def bad_fib(n):
	global num_plusses
	if n < 2:
		return n
	elif n == 2:
		return 1
	else:
		num_plusses += 1
		return bad_fib(n-1) + bad_fib(n-2)
		
def best_fib(N):
	if N < 2:
		return N
	if N == 2:
		return 1
	fib1 = 1
	fib2 = 0
	fib  = 1
	for i in range(2, N+1):
		fib = fib1 + fib2
		fib2 = fib1
		fib1 = fib
	return fib

