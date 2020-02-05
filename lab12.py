def main():
	fileName = input("Enter the name of the file you wish to open/read: ")
	data = readFile(fileName)
	validity, name = palindromeTest(data, fileName)
	isPalindrome(validity, name)
	print("All data sets complete.\n")

def readFile(fileName):
	with open(fileName, "r") as myFile:
		for line in myFile:
			return line.strip(), fileName

def palindromeTest(data, fileName):
	data = str(data)
	print("Current sentence/word: " + data)

	#Strip punctuation
	data = data.strip('?')
	data = data.strip('!')
	data = data.strip('.')

	palindromeTest(tuple(data), next(fileName))

	#Lowercase, remove spaces, and reverse string for comparison
	if data.lower().replace(' ', '') == data[::-1].lower().replace(' ', ''):
		return 1, data
	else:
		return 0, data

	palindromeTest(data, fileName)

def isPalindrome(validity, name):
	if validity == True:
		print(name + " IS a valid palindrome.\n")
	else:
		print(name + " IS NOT a valid palindrome.\n")

main()