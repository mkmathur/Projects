''' 
Change Return Program

The user enters a cost and then the amount of money given in dollars.  The program 
will figure out the change and the number of quarters, dimes, nickels, pennies needed 
for the change.

'''
import sys
from decimal import *

coins = ['quarters', 'dimes', 'nickels', 'pennies']
values = {'quarters' : 25, 'dimes' : 10, 'nickels' : 5, 'pennies' : 1}

def main(cost, given):
	change = given - cost
	print("change: ${0}".format(format(change/100, '.2f')))
	nums = {'quarters' : 0, 'dimes' : 0, 'nickels': 0, 'pennies' : 0}
	for coin in coins:
		if(change >= values[coin]):
			nums[coin] += int(change / values[coin])
			change = change % values[coin]
	for coin in coins:
		print("{0}: {1}".format(coin, nums[coin]))

if __name__ == "__main__":
	c = Decimal(sys.argv[1])
	g = Decimal(sys.argv[2]) 
	main(c*100, g*100)
