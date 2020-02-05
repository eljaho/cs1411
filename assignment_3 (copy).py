##Elias Howell | 10/24/2019 | Homework #3


#Compares two lists and returns a list of items shared by the two
def similar_items(list1, list2):
    listOfItems = []
    for item in list1:
        if item in list2:
            listOfItems.append(item)
    return listOfItems

#Compares two lists and returns a list of items not shared by the two
def unique_items(list1, list2):
    listOfItems = []
    for item in list1:
        if item not in list2:
            listOfItems.append(item)
    return listOfItems

#Takes the sum of all items in a list
def sum_items(myList):
    summationOfItems = 0
    for item in myList:
        summationOfItems += item
    return summationOfItems

#Takes the product of all items in a list
def multiply_items(myList):
    productOfItems = 1
    for item in myList:
        productOfItems *= item
    return productOfItems

#Finds and returns the smallest value in a list
def minimum_item(myList):
    minValue = myList[0]
    for item in myList:
        if item < minValue:
            minValue = item
    return minValue

#Finds and returns the largest value in a list
def maximum_item(myList):
    maxValue = myList[0]
    for item in myList:
        if item > maxValue:
            maxValue = item
    return maxValue
