'''
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
'''

import sys
from sieve import *

def main(n):
	factors = factorize(n)
	print(factors)

def factorize(n):
	s = Sieve(n+1)
	primes = s.getPrimes()
	factors = []
	i = 0
	while n > 1:
		while n % primes[i] == 0:
			factors.append(primes[i])
			n = n / primes[i]
		i = i + 1
	return factors

if __name__ == "__main__":
	n = int(sys.argv[1])
	main(n)
