##Elias Howell | 10/09/2019 | Lab Assignment #5b
##
##Program asks the user for a number and prints out the three letter abbreviation for corresponding month
##Algorithm:
##  0)Requests number input
##  1)Validates input is valid month number 1-12 and is an integer
##  2)Uses month number as an index, subtracting 1 to start from 0 counts 3 indices * number for each month
##  3)Prints the abbreviation for chosen month

monthString = "JanFebMarAprMayJunJulAugSepOctNovDec"

num = input("Enter a number that corresponds to a month of the year (1–12): ").strip()

while num.isdigit() == False or (int(num) < 1 or int(num) > 12):
    if num.isdigit() == False:
        print("\nInput must be an integer.\n")
    elif int(num) < 1 or int(num) > 12:
        print("\nInput must be between 1-12 as there are only 12 months in a year.\n")
    num = input("Enter a number that corresponds to a month of the year (1–12): ").strip()

print("An abbreviation for the month chosen is " + monthString[(int(num) - 1) * 3:3 * int(num)])