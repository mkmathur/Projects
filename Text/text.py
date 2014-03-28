# Reverse a String - Enter a string and the program will reverse it and print it out.

def reverse(str):
	return str[::-1]

# Check if Palindrome - Checks if the string entered by the user is a palindrome.
# That is that it reads the same forwards as backwards like “racecar”
def isPalindrome(str):
	return str == reverse(str)
