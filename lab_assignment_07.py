##Elias Howell | 10/23/2019 | Lab Assignment #7
##
##Program takes an atomic number and prints the element's data
##Algorithm:
##  0)Requests atomic number
##  1)Validates input to ensure 1-10
##  2)Utilizes lists for element data
##  3)Prints element data

def main():
    printElementData()

def printElementData():

    selectedElement = 10

    while selectedElement != 0:

        selectedElement = input("Enter an atomic number (Zero to quit): ")

        #Validates that the atomic number is a valid integer between 1 and 10
        while selectedElement.isdigit() == False or int(selectedElement) not in range(0, 11):
            print("Invalid input, must be an integer value between 1-10.")
            selectedElement = input("Enter an atomic number (Zero to quit): ")
        
        selectedElement = int(selectedElement)
        if selectedElement == 0:
            quit()

        #Each element in list represents piece of data
        elementData = [
            ["Hydrogen", "H", 1, 1.0079, "Non-metallic", 1, 1, 0],
            ["Helium", "He", 2, 4.0026, "Noble Gas", 2, 2, 0],
            ["Lithium", "Li", 3, 6.94, "Alkali Metal", 3, 3, 0],
            ["Beryllium", "Be", 4, 9.0122, "Alkaline Earth Metal", 4, 4, 0],
            ["Boron", "B", 5, 10.81, "Metalloid", 5, 5, 0],
            ["Carbon", "C", 6, 12.011, "Non-metallic", 6, 6, 0],
            ["Nitrogen", "N", 7, 14.007, "Non-metallic", 7, 7, 0],
            ["Oxygen", "O", 8, 15.999, "Non-metallic", 8, 8, 0],
            ["Fluorine", "F", 9, 18.998, "Non-metallic", 9, 9, 0],
            ["Neon", "N", 10, 20.180, "Noble Gas", 10, 10, 0],
            ]

        #Prefix for output 
        prefixOutput = ["Element: ", "Symbol: ", "Atomic Number: ", "Atomic Mass: ", "Classification: "]

        #Loops to print all the selected elements data
        for i in range (0, len(prefixOutput)):
            print(prefixOutput[i] + str(elementData[selectedElement - 1][i]))
        print(str(elementData[selectedElement -1][0]) + " has " + str(elementData[selectedElement -1][5]) + " electron(s), " + str(elementData[selectedElement -1][6]) + " proton(s)," + " and " + str(elementData[selectedElement -1][7]) + " neutron(s).\n")

main()