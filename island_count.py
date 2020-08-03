def count_islands(grid, x, y):
    # Check if land to right or down if there is not = new island
    islands = 0
    for row in range(0,y):
        for col in range(0,x):
            if grid[row][col] == 1:
                if row == y-1 and col == x-1:
                    islands += 1
                elif row == y-1:
                    if grid[row][col+1] == 0:
                        islands += 1
                elif col == x-1:
                    if grid[row+1][col] == 0:
                        islands += 1
                else:
                    if grid[row+1][col] == 0 and grid[row][col+1] == 0:
                        islands += 1
    return islands

print(count_islands([[1, 1, 0, 0, 0],
                     [0, 1, 0, 0, 1],
                     [1, 0, 0, 1, 1],
                     [0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 1]],5,5))