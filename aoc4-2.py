# grid = '''..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.'''

# grid = grid.split('\n')

with open('input4.txt', 'r') as file:
    grid = file.readlines()

for i in range(0, len(grid)):
    strlength = len(grid[i])
    if i == len(grid)-1:
        continue
    grid[i] = grid[i][0:strlength-1]    

def removedot(alist):
    while '.' in alist:
        alist.remove('.')
    return alist

def getsurrounding(grid, r, c):
    newlist = [ grid[r-1][c-1], grid[r-1][c], grid[r-1][c+1], \
    grid[r][c-1], grid[r][c+1], \
    grid[r+1][c-1], grid[r+1][c], grid[r+1][c+1] ]
    return removedot(newlist)

def getlside(grid, r, c):
    newlist = [grid[r-1][c], grid[r-1][c+1], grid[r][c+1], grid[r+1][c], grid[r+1][c+1]]
    return removedot(newlist)

def getrside(grid, r, c):
    newlist = [grid[r-1][c-1], grid[r-1][c], grid[r][c-1], grid[r+1][c-1], grid[r+1][c]]
    return removedot(newlist)

def gettopside(grid, r, c):
    newlist = [grid[r][c-1], grid[r][c+1], grid[r+1][c-1], grid[r+1][c], grid[r+1][c+1]]
    return removedot(newlist)

def getbotside(grid, r, c):
    newlist = [ grid[r-1][c-1], grid[r-1][c], grid[r-1][c+1], grid[r][c-1], grid[r][c+1]]
    return removedot(newlist)


newcount = -1
totcount = 0

while newcount != 0:
    newcount = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if grid[row][col] == '.':
                continue
            if row == 0 or row == len(grid)-1:
                if col == 0 or col == len(grid[row])-1:
                    grid[row] = grid[row][:col] + '.' + grid[row][col+1:]
                    newcount += 1
                    totcount += 1
                    continue
            
            if row == 0:
                rolls = gettopside(grid, row, col)
            elif row == len(grid)-1:
                rolls = getbotside(grid, row, col)
            elif col == 0:
                rolls = getlside(grid, row, col)
            elif col == len(grid[row]) - 1:
                rolls = getrside(grid, row, col)
            else:
                rolls = getsurrounding(grid, row, col)
            if len(rolls) < 4:
                grid[row] = grid[row][:col] + '.' + grid[row][col+1:]
                newcount += 1
                totcount += 1
                #print(row, col, count)

print(totcount)
            
        
