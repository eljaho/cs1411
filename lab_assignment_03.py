#Initialization of celestial body
celestialBody = 1

#Entered weight in pounds
weight = float(input("\nEnter your weight or 0 to exit: "))

#Provides continuous loop until user exits
while celestialBody > 0 or celestialBody < 12:

    #Valid weight check, or exit 0 check
    while weight <= 0:
        if weight == 0:
            print("Thanks for using the program.")
            quit()
        else:
            print("\nInvalid entry for weight.")
            weight = float(input("\nEnter a valid weight greater than 0: "))

    #Text menu
    print("""
\n****************
0)Quit Program:
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
12)Enter A Different Weight:
****************\n""")

    #Initial celestial selection
    celestialBody = int(input("Enter the corresponding number for the celestial body you want to calculate your weight on, 0 to exit, or 12 to re-enter weight: "))

    #Validity check for correct celestial selection
    while celestialBody < 0 or celestialBody > 12:
        print("\nInvalid entry.")
        celestialBody = int(input("\nEnter a valid integer between 0 and 12: "))

    #Exits program
    if celestialBody == 0:
        print("\nThanks for using the program.")
        quit()

    #Validity check for new weight entered
    elif celestialBody == 12:
        weight = float(input("Enter your weight or 0 to exit: "))
        while weight <= 0:
            if weight == 0:
                print("Thanks for using the program.")
                quit()
            else:
                print("\nInvalid entry for weight.")
                weight = float(input("\nEnter a valid weight greater than 0: "))

    #Valid celestial body calculation
    elif celestialBody == 1:
        newWeight = round(weight, 0)
        print("\nYour weight on Earth in pounds is",int(newWeight))
    elif celestialBody == 2:
        newWeight = round(weight * 2.36, 0)
        print("\nYour weight on Jupiter in pounds is",int(newWeight))
    elif celestialBody == 3:
        newWeight = round(weight * 1.12, 0)
        print("\nYour weight on Neptune in pounds is",int(newWeight))
    elif celestialBody == 4:
        newWeight = round(weight * .889, 0)
        print("\nYour weight on Uranus in pounds is",int(newWeight))
    elif celestialBody == 5:
        newWeight = round(weight * .378, 0)
        print("\nYour weight on Mercury in pounds is",int(newWeight))
    elif celestialBody == 6:
        newWeight = round(weight * .916, 0)
        print("\nYour weight on Saturn in pounds is",int(newWeight))
    elif celestialBody == 7:
        newWeight = round(weight * .907, 0)
        print("\nYour weight on Venus in pounds is",int(newWeight))
    elif celestialBody == 8:
        newWeight = round(weight * .071, 0)
        print("\nYour weight on Pluto in pounds is",int(newWeight))
    elif celestialBody == 9:
        newWeight = round(weight * 27.9, 0)
        print("\nYour weight on the Sun in pounds is",int(newWeight))
    elif celestialBody == 10:
        newWeight = round(weight * .166, 0)
        print("\nYour weight on the Moon in pounds is",int(newWeight))
    else:
        newWeight = round(weight * .377, 0)
        print("\nYour weight on Mars in pounds is",int(newWeight))
