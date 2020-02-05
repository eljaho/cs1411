##Elias Howell | 11/13/2019 | Lab Assignment 10

def main():
	openedFile = getFileName()
	newList = getFileContents(openedFile)
	print(newList)
	#countOccurence(newList)

	openedFile.close()

#Gets the file name from the user
def getFileName():
	while True:
		try:
			fileName = input("Enter the name of the file you wish to open/read: ")
			fileName = open(fileName, "r")
			return fileName
		except FileNotFoundError:
			print("\nThat file doesn't exist.\n")

#Gets the contents of the file and manipulates lists to create list of values for the future dictionary
def getFileContents(fileName):
	listOfLists = []
	newList = []
	for line in fileName:
		line = line.split()
		if line != []:
			listOfLists.append(line)
	for sublist in listOfLists:
		for item in sublist:
			item = item.strip(',')
			item = item.strip('.')
			item = item.strip('-')
			newList.append(item)
	return newList

#Builds a dictionary from the new list and sorts the dictionary based on descending order of each value
def countOccurence(newList):
	myDict = {}
	for word in newList:
		if word.lower() in myDict:
			myDict[word.lower()] += 1
		else:
			myDict[word.lower()] = 1
	myDictSorted = sorted(myDict, key=myDict.get, reverse=True)
	for i in myDictSorted:
		print(i,myDict[i])


main()