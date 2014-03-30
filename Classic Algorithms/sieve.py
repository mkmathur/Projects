from collections import deque

class Sieve:
	def __init__(self, limit):
		self.limit = limit
		self.candidates = deque([x for x in range(2,limit)])
		self.primes = deque([])
		self.findPrimes()

	def findPrimes(self):
		while self.candidates:
			p = self.candidates.popleft()
			self.primes.append(p)
			size = len(self.candidates)
			for i in range(0, size):
				n = self.candidates.popleft()
				if n % p != 0:
					self.candidates.append(n)

	def getPrimes(self):
		return list(self.primes)
