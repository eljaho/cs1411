##Elias Howell | 09/11/2019 | Homework #1
##
##This program takes an entered monetary value, calculates their change,
##  and prints out the # of bills and coins used to make change for said amount
##
##Algorithm:
##  0)Request monetary value from user converted to type float
##  1)Determine # of bills or coins by assigning "currencyType" to "userAmount" divided by "currencyValue"
##  2)Use integer division to avoid a fractional # for bills and coins
##  3)Lastly, subtract "currencyValue" times # of bill or coins from "userAmount"
##  4)Repeat 1-4

userAmount = float(input("Enter an amount of money to be converted to change: $"))

#Determines # of bills and coins through integer division of user amount by currency value
#Then subtracts that from user amount, repeats in descending order
#Dollars
hundreds = userAmount // 100
userAmount = userAmount - (100 * hundreds)
fifties = userAmount // 50
userAmount = userAmount - (50 * fifties)
twenties = userAmount // 20
userAmount = userAmount - (20 * twenties)
tens = userAmount // 10
userAmount = userAmount - (10 * tens)
fives = userAmount // 5
userAmount = userAmount - (5 * fives)
ones = userAmount // 1
userAmount = userAmount - (1 * ones)

#Cents
quarters = userAmount // .25
userAmount = userAmount - (.25 * quarters) + .0001 #quick hack adding ten thousandth to negate rounding error
dimes = userAmount // .10
userAmount = userAmount - (.10 * dimes) + .0001
nickels = userAmount // .05
userAmount = userAmount - (.05 * nickels) + .0001
pennies = userAmount // .01

#Prints # of bills and coins
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