
#Functions

#grid =[] #remove later!!!!!!!!!!!!!!!!!!!!!!!!

def startGame(size):
    index = 0
    grid = []
    for _ in range(size**2):
        if (index < (size**2)-1):
            grid.append(0)
        else:
            grid.append(2)
        index = index+1
    return grid

def printGrid(grid, size):
    index = 0
    for _ in range(size):
        for _ in range(size):
            print(grid[index], end="  ")
            index = index + 1
        print("")

#returns a particular column as a list
def getCol(grid, size, colNum):
    column = []
    rowNum = 1
    
    for _ in range(size):
        index = rowNum*colNum - 1
        column.append(grid[index])
        rowNum = rowNum + 1
    return column

#def rotateAntiClock(grid, size):



        


#Main code
size = 5
grid = startGame(size)
printGrid(grid, size)
print(getCol(grid, size, 5))