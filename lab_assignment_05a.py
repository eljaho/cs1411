##Elias Howell | 10/09/2019 | Lab Assignment #5a
##
##Program asks for the user's first and last name, uses these values to generate a username and password
##Algorithm:
##  0)Requests username and password
##  1)Validates that first and last name are valid alphabetic strings
##  2)Utilizes indices to assign username as a string consisting of first letter of first name and the first
##      seven letters of the last name
##  3)Utilizes indices to assign password as a string consisting of last two letters of the last name * 2
##      + the first three letters of the first name + 8 followed by the first letter of the user's last name
##  4)Prints the assigned values for username and password

firstName = input("Enter your first name in all lowercase: ").strip()
lastName = input("Enter your last name in all lowercase: ").strip()

while firstName.isalpha() == False or lastName.isalpha() == False:
    print("\nInvalid entry, must be alphabetic string.\n")
    firstName = input("Enter your first name in all lowercase: ").strip()
    lastName = input("Enter your last name in all lowercase: ").strip()

username = (firstName[:1] + lastName[:7]).lower()
password = (lastName[-2:] * 2 + firstName[:3] + '8' + lastName[:1]).lower()
print("Your username is: " + username)
print("your password is: " + password)