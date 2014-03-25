''' 
Coin Flip Simulation 
Simulates flipping a single weighted coin however many times the user decides. 
Records the outcomes and count the number of tails and heads. 

Takes two arguments: probability of heads and number of flips.
'''

import sys
import random

# Simulates n tosses of a coin with probability of heads p. 
# Prints the number of heads and tails. 
def main(p, n):
    heads = 0
    for i in range(0, n):
    	heads += singleFlip(p)
    print("{0} heads, {1} tails".format(heads, n - heads))

# Given the probability of heads, simulates
# a coin flip and returns 1 if the coin comes
# up heads, or 0 if it comes up tails
def singleFlip(p):
	if random.random() < p:
		return 1
	else:
		return 0

if __name__ == "__main__":
	p = float(sys.argv[1])
	n = int(sys.argv[2])
	main(p, n)





