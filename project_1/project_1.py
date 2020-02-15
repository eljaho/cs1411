##Elias Howell | 11/1/2019 | Project #1
##
##Program solves a predetermined maze, a list of lists; '#' represents walls, ' ' represents a path.
##	'S' is the starting point of the maze and 'E' is the end
##
##Algorithm:
##  0)Get the starting location for the given maze using getStartPoint()
##  1)Get the ending location for the given maze using getEndPoint()
##  2)Navigate the maze using the start and end points through navigation()
##		navigation() uses a series of conditionals to determine if a surrounding point
##		is a valid path by manipulating indices for comparison using increments of -1, +1 vertically or
##		horizontally.
##		Example: maze[y][x - 1] would check the element of the index west of (x,y)
##		maze[y + 1][x] would check the element of the index south of (x,y)
##	3)For each conditional check in navigate() the corresponding arrow replaces ' '
##		representing direction the maze solver took
##	4)If next index check is 'E' the maze has been solved, breaks infinite loop

def main():
    maze = [['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
    		['#','#',' ',' ',' ',' ',' ',' ',' ','#','#',' ',' ',' ',' ','#','#','#',' ','S'],
    		['#','#',' ','#','#','#','#','#',' ',' ',' ',' ','#','#',' ',' ',' ',' ',' ','#'],
    		['#','#',' ',' ',' ',' ','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
    		['#','#','#','#','#',' ','#','#','#','#','#','#',' ',' ',' ',' ',' ',' ','#','#'],
    		['#','#','#','#','#',' ',' ',' ',' ',' ','#','#',' ','#','#','#','#',' ','#','#'],
    		['#','#','#','#','#',' ','#','#','#',' ','#','#',' ','#','#','#','#',' ',' ','E'],
    		['#','#','#','#','#',' ','#','#','#',' ','#','#',' ','#','#','#','#','#','#','#'],
    		['#',' ',' ',' ',' ',' ','#','#','#',' ',' ',' ',' ','#','#','#','#','#','#','#'],
    		['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]

    xStart, yStart = getStartPoint(maze)
    xEnd, yEnd = getEndPoint(maze)
    navigation(xStart, yStart, xEnd, yEnd, maze)

#Finds the x and y coordinates of the starting point in a maze
def getStartPoint(maze):
    row = 0
    for rows in range(0, len(maze) - 1):
        if 'S' in maze[row]:
            x = maze[row].index('S')
            y = row
            return x, y;
        row += 1

#Finds the x and y coordinates of the ending point in a maze
def getEndPoint(maze):
    row = 0
    for rows in range(0, len(maze) - 1):
        if 'E' in maze[row]:
            x = maze[row].index('E')
            y = row
            return x, y;
        row += 1

#Navigates the maze by comparing starting coordinates to coordinates of NSEW in an infinite loop.
#If the coordinates representing an element equal to 'E' the infinite loop breaks
def navigation(xStart, yStart, xEnd, yEnd, maze):
    while True:
    	#West
        if maze[yStart][xStart - 1] == ' ':
            if maze[yStart - 1][xStart - 1] == ' ':
                maze[yStart][xStart - 1] = '^'
            elif maze[yStart + 1][xStart - 1] == ' ':
                maze[yStart][xStart - 1] = 'v'
            else:
                maze[yStart][xStart - 1] = '<'
            xStart -= 1
        elif maze[yStart][xStart - 1] == 'E':
            break
        #East
        elif maze[yStart][xStart + 1] == ' ':
            if maze[yStart - 1][xStart + 1] == ' ':
                maze[yStart][xStart + 1] = '^'
            elif maze[yStart + 1][xStart + 1] == ' ':
                maze[yStart][xStart + 1] = 'v'
            else:
                maze[yStart][xStart + 1] = '>'
            xStart += 1
        elif maze[yStart][xStart + 1] == 'E':
            break
        #South
        elif maze[yStart + 1][xStart] == ' ':
            if maze[yStart + 1][xStart - 1] == ' ':
                maze[yStart + 1][xStart] = '<'
            elif maze[yStart + 1][xStart + 1] == ' ':
                maze[yStart + 1][xStart] = '>'
            else:
                maze[yStart + 1][xStart] = 'v'
            yStart += 1
        elif maze[yStart + 1][xStart] == 'E':
            break
        #North
        elif maze[yStart - 1][xStart] == ' ':
            if maze[yStart - 1][xStart - 1] == ' ':
                maze[yStart - 1][xStart] = '<'
            elif maze[yStart - 1][xStart + 1] == ' ':
                maze[yStart -1][xStart] = '>'
            else:
                maze[yStart - 1][xStart] = '^'
            yStart -= 1
        elif maze[yStart - 1][xStart] == 'E':
            break
        for i in maze:
            line = ''.join(i)
            print(line)
        print()

main()
