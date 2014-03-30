from sieve import *

MAX = 100
s = Sieve(MAX)
primes = s.getPrimes()

def main():
	i = 0
	ans = "y"
	while ans.startswith(("y", "Y")):
		if i < len(primes):
			print(primes[i])
		else:
			p = primes[i - 1]
			while not isPrime(p):
				p += 2
			primes.append(p)
			print(p)
		i += 1
		ans = input('Generate next prime? ')

def isPrime(n):
	for p in primes:
		if n % p == 0:
			return False
	return True

if __name__ == "__main__":
	main()


