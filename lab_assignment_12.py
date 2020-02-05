def main():

	palindromeTest(fetchReadFile())
	print("All data sets complete.\n")

def fetchReadFile():
	fileName = input("Enter the name of the file you wish to open/read: ")

	#Create list of records one record per line
	with open(fileName, "r") as myFile:
		listOfDat = myFile.read().splitlines()
	return listOfDat

def palindromeTest(data):
	for i in data:
		print("Current sentence/word: " + i)

		#Strip punctuation
		i = i.strip('?')
		i = i.strip('!')
		i = i.strip('.')

		#Lowercase, remove spaces, and reverse string for comparison
		if i.lower().replace(' ', '') == i[::-1].lower().replace(' ', ''):
			print(i + " IS a valid palindrome.\n")
		else:
			print(i + " IS NOT a valid palindrome.\n")

main()