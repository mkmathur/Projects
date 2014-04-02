def factorial(n):
	result = 1
	for i in range(2,n+1):
		result = result * i
	return result

def recursive_factorial(n):
	if n <= 1:
		return 1
	else:
		return n * recursive_factorial(n-1)
