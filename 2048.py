
#Functions

#grid =[] #remove later!!!!!!!!!!!!!!!!!!!!!!!!
size = 5
def startGame():
    index = 0
    grid = []
    for _ in range(size**2):
        if (index < (size**2)-1):
            grid.append(0)
        else:
            grid.append(2)
        index = index+1
    return grid

def printGrid(grid):
    index = 0
    for _ in range(size):
        for _ in range(size):
            print(grid[index], end="  ")
            index = index + 1
        print("")

#returns a particular column as a list
def getCol(grid, colNum):
    column = []
    index = colNum - 1
    for _ in range(size):
        column.append(grid[index])
        index = index + size
    return column

def rotateAntiClock(grid):
    grid2 = []
    colNum = size
    for _ in range(size):
        col = getCol(grid, colNum)
        for num in col:
            grid2.append(num)
        colNum = colNum-1
    grid[:] = grid2

#returns the number of empty spaces in a given list with a between a starting and ending index inclusive
def empty(row, low_limit, high_limit):
    count = 0
    for i in range(low_limit, high_limit):
        if row[i] == 0:
            count = count+1
    return count



#def moveLeft(grid):


#Main code

grid = startGame()
printGrid(grid)



