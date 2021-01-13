
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
    return grid2



        


#Main code
size = 5
grid = startGame()
printGrid(grid)
grid = rotateAntiClock(grid)
print("")
printGrid(grid)

grid = rotateAntiClock(grid)
print("")
printGrid(grid)

grid = rotateAntiClock(grid)
print("")
printGrid(grid)

grid = rotateAntiClock(grid)
print("")
printGrid(grid)