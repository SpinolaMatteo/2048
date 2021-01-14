
#Functions

size = 5
def startGame():
    index = 0
    grid = []
    for _ in range(size**2):
        if (index < (size**2)-1):
            grid.append(2)
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

#arranges all the empty spaces on the right side and all the numbers on the left
def arrange(grid, low_limit, high_limit):
    numZero = empty(grid, low_limit, high_limit-1)
    count1 = 0
    while count1 <= numZero:
        for i in range(low_limit,high_limit-1):
            if grid[i] == 0:
                grid[i] = grid[i+1]
                grid[i+1] = 0
        count1 = count1+1

def move_row_left(grid, low_limit, high_limit):
    grid_copy = grid[:]
    arrange(grid, low_limit, high_limit)

    for i in range(low_limit, high_limit-1):
        if (grid[i] == grid[i+1]) and (grid[i] != 0):
            grid[i] = 2*grid[i]
            grid[i+1] = 0
    
    arrange(grid, low_limit, high_limit)
    if(grid_copy == grid):
        return False
    return True

#moves the whole grid left
def moveLeft(grid):
    c = False
    changed = False
    #I use "changed" to determine if the grid changed after a move to the left or if the move did not do anything
    for i in range(size):
        low_limit = i*size
        high_limit = low_limit + size
        c = move_row_left(grid, low_limit, high_limit)
        if(c):
            changed = True
    return changed

#Main code

grid = startGame()
printGrid(grid)

moveLeft(grid)
printGrid(grid)



