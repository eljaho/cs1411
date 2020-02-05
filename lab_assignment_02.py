#Entered weight in pounds
weight = float(input("Enter your weight: "))

#Checking for validity
if weight <= 0:
    print("\nInvalid entry for weight.")
    quit()

#Text menu
print("""*****************
1)Earth:
2)Jupiter:
3)Neptune:
4)Uranus:
5)Mercury:
6)Saturn:
7)Venus:
8)Pluto:
9)Sun:
10)Moon:
11)Mars
*****************""")

#Celestial selection
celestialBody = int(input("Enter the corresponding number for the celestial body you want to calculate your weight on: "))

#Validity check
if celestialBody < 1 or celestialBody > 11:
    print("Invalid entry for corresponding celestial body number.")
    quit()

#Chosen celestial body calculation
if celestialBody == 1:
    weight = round(weight, 0)
    print("Your weight on Earth in pounds is",int(weight))
elif celestialBody == 2:
    weight = round(weight * 2.36, 0)
    print("Your weight on Jupiter in pounds is",int(weight))
elif celestialBody == 3:
    weight = round(weight * 1.12, 0)
    print("Your weight on Neptune in pounds is",int(weight))
elif celestialBody == 4:
    weight = round(weight * .889, 0)
    print("Your weight on Uranus in pounds is",int(weight))
elif celestialBody == 5:
    weight = round(weight * .378, 0)
    print("Your weight on Mercury in pounds is",int(weight))
elif celestialBody == 6:
    weight = round(weight * .916, 0)
    print("Your weight on Saturn in pounds is",int(weight))
elif celestialBody == 7:
    weight = round(weight * .907, 0)
    print("Your weight on Venus in pounds is",int(weight))
elif celestialBody == 8:
    weight = round(weight * .071, 0)
    print("Your weight on Pluto in pounds is",int(weight))
elif celestialBody == 9:
    weight = round(weight * 27.9, 0)
    print("Your weight on the Sun in pounds is",int(weight))
elif celestialBody == 10:
    weight = round(weight * .166, 0)
    print("Your weight on the Moon in pounds is",int(weight))
else:
    weight = round(weight * .377, 0)
    print("Your weight on Mars in pounds is",int(weight))
