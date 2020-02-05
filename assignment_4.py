##Elias Howell | 11/17/2019 | Assignment #4
##
##Program takes a file selected by the user and creates a maze from the file.
##	The program then solves said maze by finding the correct path through trial and error
##  'S' is the starting point and 'E' is the end of the maze.
##
##Algorithm:
##  0)Get the file name from the user, make sure file exists, valid, and not empty
##
##  1)Make a maze by reading the file into a list of strings, splitting newlines, removing ''
##      Take the elements within that list and create another list from each element resulting in list of lists
##      If error is encountered during maze creation print error
##
##  2)Get the starting location (S) for the given maze using getStartPoint()
##      If start point doesn't exist print error
##
##  3)Get ending location (E) for the given maze using getEndPoint()
##      If end point doesn't exist print error
##
##  4)Navigate the maze using navigation()
##		navigation() uses a series of conditionals to determine if a surrounding point
##		is a valid path by manipulating indices for comparison using increments of -1, +1 
##      vertically or horizontally.
##		Example: maze[y][x - 1] would check the element of the index west of (x,y)
##		maze[y + 1][x] would check the element of the index south of (x,y)
##
##	5)For each conditional check inside navigate() the corresponding arrow replaces ' '
##		representing the direction the maze solver took
##
##  6)If navigation hits a dead end the solver backtracks the steps it took until
##      it finds another path to take.
##      Backtracking: retraces steps by following past footprints until it reaches another open path
##          it hasn't taken, if no white space or arrows left to traverse, the maze is unsolvable
##
##	7)If next index check is 'E' the maze has been solved, breaks infinite loop
##
##TO DO LIST - Note: Current incarnation of this maze solver solves the easy mazes, doesn't solve the newest files
##  1)Deal with mazes with no walls, index out of range error, still debugging, strange because it should only be reading ' '
##      thus walls shouldn't matter
##
##  2)Handle and print the rest of the errors, I've already finished file not found, empty file, and unsolvable maze errors.
##      Still need to handle No start, No end, and invalid characters errors
##
##  3)Handles jagged mazes as long as the maze is entirely enclosed, still trying to debug the index out of range error
##
##  4)Fix the arrow direction footprint when a turn is made to meet proper output requirements (not yet sure if semantically sensible with my method of navigation)

import time

def main():
    maze = makeMaze(getFileName())
    xStart, yStart = getStartPoint(maze)
    getBoundaries(maze)
    getEndPoint(maze)
    navigation(xStart, yStart, maze)

#Get the file name from the user, prints error if file not found
def getFileName():
    try:
        fileName = input("Enter the name of the file you wish to open/read: ")
        fileName = open(fileName, "r")
        return fileName
    except FileNotFoundError:
        print("\nError: Specified file does not exist.\n")

#Creates a maze from user's chosen file by creating a list of lists
def makeMaze(file):
    maze = []
    for line in file:
        line = line.split('\n')
        if '' in line: #Removes empty list if '' in line of file after split
            line.remove('')
        maze.append(list(line))
        counter = 0
    for line in maze:
        for element in line:
            maze[counter] = (list(element))
            counter += 1

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

#Get boundaries of the created maze
def getBoundaries(maze):
    print(len(maze))

#Prints iteration of maze
def printMaze(maze):
    for i in maze:
        line = ''.join(i)
        print(line)
    print()
    time.sleep(.01)

#Navigates the maze by comparing starting coordinates to coordinates of NSEW using
#the element 'E' as a coordinate sentinel value to break when encountered
#Backtracks by retracing steps taken to find another open path if it reaches a dead end
def navigation(xStart, yStart, maze):
    y = yStart
    x = xStart

    #While at current position, if either north south east or west directions result in 'E' the maze has been solved
    while not maze[y - 1][x] == 'E' and not maze[y + 1][x] == 'E' and not maze[y][x - 1] == 'E' and not maze[y][x + 1] == 'E':
        #Go North
        if maze[y - 1][x] == ' ':
            maze[y - 1][x] = '^'
            y -= 1
        #Go South
        elif maze[y + 1][x] == ' ':
            maze[y + 1][x] = 'v'
            y += 1
        #Go West
        elif maze[y][x - 1] == ' ':
            maze[y][x - 1] = '<'
            x -= 1
        #Go East
        elif maze[y][x + 1] == ' ':
            maze[y][x + 1] = '>'
            x += 1
        #Must be a dead end, backtrack now
        else:
            #While maze directions aren't resulting in either a path (' ') or a wall ('#')
            while maze[y][x] != ' ' or maze[y][x] != '#':
                if maze[y - 1][x] == ' ' or maze[y + 1][x] == ' ' or maze[y][x - 1] == ' ' or maze[y][x + 1] == ' ':
                    break
                #Retrace eastward tracks
                elif maze[y][x] == '>':
                    maze[y][x] = '.'
                    x -= 1
                    printMaze(maze)
                #Retrace southward tracks
                elif maze[y][x] == 'v':
                    maze[y][x] = '.'
                    y -= 1
                    printMaze(maze)
                #Retrace westward tracks
                elif maze[y][x] == '<':
                    maze[y][x] = '.'
                    x += 1
                    printMaze(maze)
                #Retrace northward tracks
                elif maze[y][x] == '^':
                    maze[y][x] = '.'
                    y += 1
                    printMaze(maze)
                #Unsolvable maze as solver took every possible path, retraced all steps, and back to start
                elif maze[y][x] == 'S':
                    print("\nError: No route could be found from start to end. Maze unsolvable.\n")
                    quit()

        printMaze(maze)

main()