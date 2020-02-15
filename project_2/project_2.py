##Elias Howell | 11/17/2019 | Project #2
##
##Program takes a file selected by the user and creates a maze from the file.
##	The program then solves said maze by finding the correct path through trial and error
##  'S' is the starting point and 'E' is the end of the maze.
##
##Algorithm:
##  0)Get the file name from the user, make sure file exists, valid, and not empty
##  1)Make a maze by reading the file into a list of strings, splitting newlines, removing ''
##      Take the elements within that list and create another list from each string resulting in list of lists
##  2)Get the starting location for the given maze using getStartPoint()
##  3)Navigate the maze using navigation()
##		navigation() uses a series of conditionals to determine if a surrounding point
##		is a valid path by manipulating indices for comparison using increments of -1, +1 
##      vertically or horizontally.
##		Example: maze[y][x - 1] would check the element of the index west of (x,y)
##		maze[y + 1][x] would check the element of the index south of (x,y)
##	4)For each conditional check inside navigate() the corresponding arrow replaces ' '
##		representing direction the maze solver took
##  5)If navigation hits a dead end the solver backtracks the steps it took until
##      it finds another path to take.
##      Backtracking: retraces steps by following past footprints until it reaches another open path
##          it hasn't taken, if no white space or arrows left to traverse, the maze is unsolvable
##	6)If next index check is 'E' the maze has been solved, breaks loop


def main():
    maze = makeMaze(getFileName())

    #If start or end point does not exist, prints error and quits
    doesStartExist = 'S' in (i for row in maze for i in row)
    doesEndExist = 'E' in (i for row in maze for i in row)
    if doesStartExist == False:
        print("\nError: No start position found.\n")
        quit()
    if doesEndExist == False:
        print("\nError: No end position found.\n")
        quit()

    xStart, yStart = getStartPoint(maze)
    xEnd, yEnd = getEndPoint(maze)
    navigation(xStart, yStart, maze)

#Get the file name from the user, prints error if file not found
def getFileName():
    try:
        fileName = input("Enter the name of the file you wish to open/read: ")
        fileName = open(fileName, "r")
        return fileName
    except FileNotFoundError:
        print("\nError: Specified file does not exist.\n")
        quit()

#Creates a maze from user's chosen file by creating a list of lists
def makeMaze(file):
    maze = []
    for line in file:
        line = line.split('\n')
        if '' in line:
            line.remove('')
        maze.append(list(line))
        counter = 0
    for line in maze:
        for element in line:
            maze[counter] = (list(element))
            counter += 1
    lineCounter = 0
    #Entire block is to prevent invalid characters in maze, informs user if it contains an invalid character
    for line in maze:
        lineCounter += 1
        for element in line:
            if element != " " and element != "#" and element != "S" and element != "E":
                print("\nError: Maze contains invalid characters. Line " + str(lineCounter) + " contains invalid character '" + element + "'.\n")
                quit()

    #If file is empty resulting in empty maze
    if maze == []:
        print("\nError: Specified file contains no maze.\n")
        quit()

    return maze

#Finds the x and y coordinates of the starting point in a maze (S)
def getStartPoint(maze):
    row = 0
    for rows in range(0, len(maze) - 1):
        if 'S' in maze[row]:
            x = maze[row].index('S')
            y = row
            return x, y;
        row += 1

#Finds the x and y coordinates of the ending point in a maze (E)
def getEndPoint(maze):
    row = 0
    for rows in range(0, len(maze) - 1):
        if 'E' in maze[row]:
            x = maze[row].index('E')
            y = row
            return x, y;
        row += 1

#Prints iteration of maze
def printMaze(maze):
    for i in maze:
        line = ''.join(i)
        print(line)
    print()

#Navigates the maze by comparing starting coordinates to coordinates of NSEW in a loop.
#The loop breaks if the next possible step is equal to 'E'
#Backtracks by retracing steps taken to find another path if it reaches a dead end
def navigation(xStart, yStart, maze):
    y = yStart
    x = xStart

    yBound = len(maze)
    for i in maze:
        xBound = len(i)
    yBound -= 1
    xBound -= 1

    #While at current position, if either north south east or west directions result in 'E' the maze has been solved
    while not maze[y - 1][x] == 'E' and not maze[y + 1][x] == 'E' and not maze[y][x - 1] == 'E' and not maze[y][x + 1] == 'E':
        if not y != yBound or not x != xBound or not y > 0 or not x > 0:
            #Retrace northward tracks
            if maze[y + 1][x] == '^':
                maze[y][x] = '.'
                y += 1
                printMaze(maze)
            #Retrace eastward tracks
            elif maze[y][x - 1] == '>':
                maze[y][x] = '.'
                x -= 1
                printMaze(maze)
            #Retrace southward tracks
            elif maze[y - 1][x] == 'v':
                maze[y][x] = '.'
                y -= 1
                printMaze(maze)
            #Retrace westward tracks
            elif maze[y][x + 1] == '<':
                maze[y][x] = '.'
                x += 1
                printMaze(maze)
            #Unsolvable maze as solver took every possible path, retraced all steps, and back to start
            else:
                print("\nError: No route could be found from start to end. Maze unsolvable.\n")
                quit()
        #Go North
        elif maze[y - 1][x] == ' ':
            maze[y][x] = '^'
            y -= 1
        #Go South
        elif maze[y + 1][x] == ' ':
            maze[y][x] = 'v'
            y += 1
        #Go West
        elif maze[y][x - 1] == ' ':
            maze[y][x] = '<'
            x -= 1
        #Go East
        elif maze[y][x + 1] == ' ':
            maze[y][x] = '>'
            x += 1
        #Must be a dead end, backtrack now
        else:
            #While maze directions aren't resulting in either a path (' ') or a wall ('#')
            while maze[y][x] == ' ' or maze[y][x] != ' ' and maze[y][x] != '#':
                if maze[y - 1][x] == ' ' or maze[y + 1][x] == ' ' or maze[y][x - 1] == ' ' or maze[y][x + 1] == ' ':
                    break
                #Retrace eastward tracks
                elif maze[y][x - 1] == '>':
                    maze[y][x] = '.'
                    x -= 1
                    printMaze(maze)
                #Retrace southward tracks
                elif maze[y - 1][x] == 'v':
                    maze[y][x] = '.'
                    y -= 1
                    printMaze(maze)
                #Retrace westward tracks
                elif maze[y][x + 1] == '<':
                    maze[y][x] = '.'
                    x += 1
                    printMaze(maze)
                #Retrace northward tracks
                elif maze[y + 1][x] == '^':
                    maze[y][x] = '.'
                    y += 1
                    printMaze(maze)
                #Unsolvable maze as solver took every possible path, retraced all steps, and back to start
                else:
                    print("\nError: No route could be found from start to end. Maze unsolvable.\n")
                    quit()

        printMaze(maze)
        #North final
        if maze[y - 1][x] == 'E':
            maze[y][x] = '^'
        #South final
        elif maze[y + 1][x] == 'E':
            maze[y][x] = 'v'
        #West final
        elif maze[y][x - 1] == 'E':
            maze[y][x] = '<'
        #East final
        elif maze[y][x + 1] == 'E':
            maze[y][x] = '>'
        maze[yStart][xStart] = 'S'

    printMaze(maze)

main()