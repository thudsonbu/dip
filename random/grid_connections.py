# Hi, here's your problem today. This problem was recently asked by Uber:

# Find the maximum number of connected squares in a grid.

class Grid:
    def __init__(self, grid):
        self.grid = grid

    def max_connected_colors(self):
        row, column, max_con = 0, 0, 0 # keep track of place

        while True: # iterate through grid row by row
            item = self.grid[row][column]

            if item == 1: # if we find a
                con = self.find_connections(row,column) # get connection count
                max_con = max(max_con, con) # set max if higher then current max

            # move to next spot
            if column < len(self.grid[row])-1: 
                column += 1
            elif row < len(self.grid)-1:
                row += 1
                column = 0
            else: 
                break

        return max_con

    def find_connections(self, row, column):
        self.grid[row][column] = 0 # zero out so not recounted
        right_con, bottom_con, left_con, top_con = 0, 0, 0, 0
        
        if column < len(self.grid[row])-1 and self.grid[row][column+1] == 1:# if right exists and is con
            right_con = self.find_connections(row, column+1) # get connection count
        
        if row < len(self.grid)-1 and self.grid[row+1][column] == 1: # if bottom exists and is con
            bottom_con = self.find_connections(row+1, column) # get connection count

        if column > 0 and self.grid[row][column-1] == 1:# if left exists and is con
            left_con = self.find_connections(row, column-1) # get connection count

        if row > 0 and self.grid[row-1][column] == 1:# if top exists and is con
            top_con = self.find_connections(row-1, column) # get connection count

        return right_con + left_con + bottom_con + top_con + 1 # return all found connections plus one for self

# TEST
grid = [[1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 1, 0, 0]]

print(Grid(grid).max_connected_colors())
