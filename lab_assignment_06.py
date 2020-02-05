##Elias Howell | 10/16/2019 | Lab Assignment 6
##
##This program takes an entered monetary value, calculates their change,
##  and prints out the # of bills and coins used to make change for said amount
##
##Algorithm:
##  0)Request monetary value from user converted to type float
##  1)Validates that userAmount is valid floating point
##  1)Determine # of bills or coins by assigning "currencyType" to "userAmount" divided by "currencyValue"
##  2)Use integer division to avoid a fractional # for bills and coins
##  3)Lastly, subtract "currencyValue" times # of bill or coins from "userAmount"
##  4)Repeat 1-4

def main():
    userAmount = input("Enter an amount of money to be converted to change: $")

    #Validates userAmount is a valid floating point
    while userAmount.isdigit() == False and '.'  not in userAmount:
        print("Invalid entry. Must be a floating point value.")
        userAmount = input("Enter an amount of money to be converted to change: $")
        
    makeChange(float(userAmount))

#Determines # of bills and coins through integer division of user amount by currency value
#Then subtracts that from user amount, repeats in descending order then prints number of bills and coins
def makeChange(userAmount):
    hundreds, userAmount = divide(userAmount, 100)
    fifties, userAmount = divide(userAmount, 50)
    twenties, userAmount = divide(userAmount, 20)
    tens, userAmount = divide(userAmount, 10)
    fives, userAmount = divide(userAmount, 5)
    ones, userAmount = divide(userAmount, 1)
    quarters, userAmount = divide(userAmount, .25)
    dimes, userAmount = divide(userAmount, .10)
    nickels, userAmount = divide(userAmount, .05)
    pennies, userAmount = divide(userAmount, .01)

    #Cast from float to int to remove decimal, then to str for concatenation
    print("\n\nHand the customer the following amounts of each: ")
    print("$100 x " + str(int(hundreds)))
    print("$50  x " + str(int(fifties)))
    print("$20  x " + str(int(twenties)))
    print("$10  x " + str(int(tens)))
    print("$5   x " + str(int(fives)))
    print("$1   x " + str(int(ones)))
    print("25¢  x " + str(int(quarters)))
    print("10¢  x " + str(int(dimes)))
    print("5¢   x " + str(int(nickels)))
    print("1¢   x " + str(int(pennies)))

#Determines # of bills and coins through integer division of user amount by currency value
#Then subtracts that from user amount, repeats in descending order
def divide(userAmount, currencyValue):
    numOfCurrency = userAmount // currencyValue
    userAmount = userAmount - (currencyValue * numOfCurrency) + .0001
    return numOfCurrency, userAmount

main()
