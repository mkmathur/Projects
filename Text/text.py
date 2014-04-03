# Reverse a String - Enter a string and the program will reverse it and print it out.

def reverse(str):
	return str[::-1]

# Check if Palindrome - Checks if the string entered by the user is a palindrome.
# That is that it reads the same forwards as backwards like “racecar”
def isPalindrome(str):
	return str == reverse(str)

# Count Vowels - Enter a string and the program counts the number of vowels in the text.
def countVowels(str):
	vowel_counts = {'a':0, 'e':0, 'i':0, 'o':0, 'y':0}
	for c in str.lower():
		if c in vowel_counts.keys():
			vowel_counts[c] += 1
	print(vowel_counts)
