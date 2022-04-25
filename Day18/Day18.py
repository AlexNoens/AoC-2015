import numpy as np

def open_input():
    f = open("Day18/input.txt","r")
    clean_raw = []
    rows = 0
    for line in f:
        rows += 1
        clean_raw.append(line.strip())
    i = 0
    j = 0
    grid = np.zeros((rows, len(clean_raw[0])))
    for line in clean_raw:
        for point in line:
            if(point == "\n"):
                continue
            if(point == "#"):
                grid[i][j] = 1
            j +=1
        j = 0
        i += 1
    return grid, rows, len(clean_raw[0])

grid, rows, cols = open_input()

def neighbors(matrix, rowNumber, colNumber):
    result = 0
    for rowAdd in range(-1, 2):
        newRow = rowNumber + rowAdd
        if newRow >= 0 and newRow <= len(matrix)-1:
            for colAdd in range(-1, 2):
                newCol = colNumber + colAdd
                if newCol >= 0 and newCol <= len(matrix)-1:
                    if newCol == colNumber and newRow == rowNumber:
                        continue
                    if matrix[newRow][newCol] == 1:
                        result += 1
    return result

def check_neighbours(i,j,grid):
    count = neighbors(grid, i, j)
    if grid[i][j] == 1:
        return count == 2 or count == 3
    else:
        return count == 3

def is_corner(i,j,grid):
    shape = grid.shape
    if i == 0 and j == 0:
        return True
    if i == 0 and j == shape[0] -1:
        return True
    if i == shape[1]-1 and j == 0:
        return True
    if i == shape[1]-1 and j == shape[0] -1:
        return True
    return False

shape = grid.shape
grid[0][0] = 1
grid[0][shape[0] -1] = 1
grid[shape[1]-1][0] = 1
grid[shape[1]-1][shape[0] -1] = 1

for steps in range(0,100):
    old_grid = grid.copy()
    for i in range(0,rows):
        for j in range(0,cols):
            if is_corner(i,j,grid):
                continue
            if check_neighbours(i,j,old_grid):
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    print("STEP:", steps)
    print(grid)


count = 0
for i in range(0,rows):
    for j in range(0,cols):
        if grid[i][j] == 1:
            count += 1

print("LIGHTS THAT ARE ON:", count)
