#takes height, width, length, casts input to int
height = int(input("Enter the height of the box in inches: "))
width = int(input("Enter the width of the box in inches: "))
length = int(input("Enter the length of the box in inches: "))

#calculating surface area and volume
surfaceArea = (2 * (height * width)) + (2 * (height * length)) + (2 * (width * length))
volume = height * width * length

#prints SA and volume casted back to str for output
print("The surface area of the box is " + str(surfaceArea) + " inches squared.") 
print("The volume of the box is " + str(volume) + " cubic inches.")

#breaking hwl into ft/inches
heightFt = height // 12
heightIn = height % 12
widthFt = width // 12
widthIn = width % 12
lengthFt = length // 12
lengthIn = length % 12

#printing hwl in ft/inches   
print("The height of the box is: " + str(heightFt) + " ft " + str(heightIn) + " in")
print("The width of the box is: " + str(widthFt) + " ft " + str(widthIn) + " in")
print("The length of the box is: " + str(lengthFt) + " ft " + str(lengthIn) + " in")
