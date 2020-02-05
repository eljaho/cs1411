<<<<<<< HEAD
##Elias Howell | 09/11/2019 | Homework #2
=======
##Elias Howell | 10/12/2019 | Homework #2
>>>>>>> b82501bc3b2bd82ace4e34e3e25081126f2ef417
##
##This program accepts a date as a string in MM/DD/YYYY form. 
##It then determines if the syntax is valid and prints the date to the user in American form
##  
##
##Algorithm:
##  0)Request input from user
##  1)Determines if syntax for MM/DD/YYYY is in correct format by checking number of '/'
##      if not correct, prints error message informing user of syntax error
##  2)Use index/slicing to find location of '/' and use as delimiter for assignment of month/day/year variables
##  3)Strip leading zeroes for clear output
##  3)Determines if month/day/and year are correct integer values that make sense
##      Example: only 31 days in Dec, for February checks leap year for 29 days, 28 days if not leap
##      Example: no negative month/day values, negative years valid for BCE
##  4)Associates integer month with a string name of month, and number of days associated with said month
##  5)Prints American form of date, or if month/year/day error prints corresponding error

#User enters date
date = input("Enter a date in month/day/year format: ")

#Prints a syntax error if date doesn't have 2 '/' formatting MM/DD/YYYY or if the other values besides '/' aren't digits and doesn't contain '-'
if date.count('/') != 2 or date.replace('/', '').isdigit() == False and '-' not in date:
    print("Syntax Error: You supplied an incorrect date format. Please use only numeric values for the month, day and year and use only the ‘/’ character as a delimiter.")
    quit()

#Utilizes slicing and indexing to find where '/' is located in date and reads string for month, day, and year starting from '/' (+ 1 to move to index after previous '/')
month = date[0 : date.index('/')]
date = date[date.index('/') + 1 : len(date)]
day = date[0 : date.index('/')]
date = date[date.index('/') + 1 : len(date)]
year = date

#Strips leading zeroes from day and year for output
day = day.lstrip("0")
year = year.lstrip("0")

#Associates month name with month number, chronologically, and assigns number of days in each month including a check for leap years
if int(month) == 1:
    monthName = "January"
    monthDays = 31
elif int(month) == 2:
    monthName = "February"
    if int(year) % 400 == 0 or int(year) % 4 == 0 and not int(year) % 100 == 0: #Leap year check
        monthDays = 29
    else:
        monthDays = 28
elif int(month) == 3:
    monthName = "March"
    monthDays = 31
elif int(month) == 4:
    monthName = "April"
    monthDays = 30
elif int(month) == 5:
    monthName = "May"
    monthDays = 31
elif int(month) == 6:
    monthName = "June"
    monthDays = 30
elif int(month) == 7:
    monthName = "July"
    monthDays = 31
elif int(month) == 8:
    monthName = "August"
    monthDays = 31
elif int(month) == 9:
    monthName = "September"
    monthDays = 30
elif int(month) == 10:
    monthName = "Octobor"
    monthDays = 31
elif int(month) == 11:
    monthName = "November"
    monthDays = 30
elif int(month) == 12:
    monthName = "December"
    monthDays = 31

#Prints error if year isn't a non-zero numeric value, ignores '-' character for BCE
if year.isdigit() == False and '-' not in year or int(year) == 0:
    print("Year Error: You supplied an incorrect value for year. Please use only non-zero numeric values to represent the year.")
    quit()
#Prints error if month isn't a numeric value between 1 and 12
elif month.isdigit() == False or int(month) < 1 or int(month) > 12:
    print("Month Error: You supplied an incorrect value for month. Please use only numeric values in the range of 1 (January) through 12 (December) to represent the month.")
    quit()
#Prints error if day isn't a numeric value greater than 1 or if day entered is greater than number of days in specified month
elif day.isdigit() == False or int(day) < 1 or int(day) > monthDays:
    print("Day Error: You supplied an incorrect value for day. The month of " + monthName + " only contains days in the range of 1 through " + str(monthDays) + " for the specified year, " + str(year) + ".")
    quit()

print("You entered the date", monthName, day + ",", year)
