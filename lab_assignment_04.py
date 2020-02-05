##Elias Howell | 10/02/2019 | Lab Assignment #4
##
##Program takes status of buttons and outputs prank configured status of hallway lights
##Algorithm:
##  0)Requests individual button on/off status
##  1)Validates input to ensure input is on or off
##  2)Decides whether or not a hallway light should be on or off according to prank settings
##  3)Prints hallway light output to screen

#Initialization of button status
B1 = input("Enter the state of B1 (on|off): ")
B1 = B1.upper()
B2 = input("Enter the state of B2 (on|off): ")
B2 = B2.upper()
B3 = input("Enter the state of B3 (on|off): ")
B3 = B3.upper()
B4 = input("Enter the state of B4 (on|off): ")
B4 = B4.upper()

#Input validation for button status
while not ((B1 == "ON" or B1 == "OFF") and (B2 == "ON" or B2 == "OFF") and (B3 == "ON" or B3 == "OFF") and (B4 == "ON" or B4 == "OFF")):
    print("\nOne of your inputs were invalid. Input must be 'on' or 'off' it isn't case sensetive.\n")
    B1 = input("Enter the state of B1 (on|off): ")
    B1 = B1.upper()
    B2 = input("Enter the state of B2 (on|off): ")
    B2 = B2.upper()
    B3 = input("Enter the state of B3 (on|off): ")
    B3 = B3.upper()
    B4 = input("Enter the state of B4 (on|off): ")
    B4 = B4.upper()

#Decides whether or not a hallway light is ultimately on or off
if (B1 == "ON" and B4 == "OFF") or (B1 == "OFF" and B4 == "ON"):
    nwStatus = "ON"
else:
    nwStatus = "OFF"
if (B2 == "ON" and B3 == "OFF") or (B2 == "OFF" and B3 == "ON"):
    neStatus = "ON"
else:
    neStatus = "OFF"
if (B1 == "ON" and B3 == "OFF") or (B1 == "OFF" and B3 == "ON"):
    seStatus = "ON"
else:
    seStatus = "OFF"
if (B2 == "ON" and B4 == "OFF") or (B2 == "OFF" and B4 == "ON"):
    swStatus = "ON"
else:
    swStatus = "OFF"

#Print light status
print("\n\nLight status for NW Hallway:", nwStatus)
print("Light status for NE Hallway:", neStatus)
print("Light status for SE Hallway:", seStatus)
print("Light status for SW Hallway:", swStatus)
