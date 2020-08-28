class board(object):
    def __init__(self):
        self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.x = 1

    def move_x(self, x, y):
        if self.board[y][x] != "-":
            print("Position taken")
            return False
        self.board[y][x] = "x"
        win = self.check_win("x")
        self.print_board()
        if win:
            print("Win! \n")


    def move_o(self, x, y):
        if self.board[y][x] != "-":
            print("Position taken")
            return False
        self.board[y][x] = "o"
        win = self.check_win("o")
        self.print_board()
        if win:
            print("Win! \n")

    def print_board(self):
        for row in self.board:
            print_row = "| "
            for item in row:
                print_row += item + " | "
            print(print_row)
        print("")

    def check_win(self,marker):

        for row in self.board:
            row_match = True
            for item in row:
                if item == marker:
                    continue
                row_match = False
            if row_match:
                return True

        
        for column_num in range(0,len(self.board[0])):
            col_match = True
            for row_num in range(0,len(self.board[0])):
                if self.board[row_num][column_num] == marker:
                    continue
                col_match = False
            if col_match:
                return True

        diagonal_locations = [[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]]

        for direction in diagonal_locations:
            diag_match = True
            for location in direction:
                if self.board[location[0]][location[1]] == marker:
                    continue
                diag_match = False
            if diag_match:
                return True

        return False


new_board = board()
new_board.move_o(0,0)
new_board.move_o(0,1)
new_board.move_o(0,2)

new_board = board()
new_board.move_x(1,0)
new_board.move_x(1,1)
new_board.move_x(1,2)

new_board = board()
new_board.move_o(0,0)
new_board.move_o(1,1)
new_board.move_o(2,2)

new_board = board()
new_board.move_x(0,2)
new_board.move_x(1,1)
new_board.move_x(2,0)