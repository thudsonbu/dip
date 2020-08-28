class board(object):
    def __init__(self):
        self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.x = 1

    def move_x(self, x, y):
        self.board[y][x] == "x"
        win = self.check_win("x")
        self.print_board()
        if win:
            print("Win! \n")


    def move_o(self, x, y):
        self.board[y][x] == "o"
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

    def check_win(self,marker):
        row_match = True
        for row in self.board:
            for item in row:
                if item == marker:
                    continue
                row_match = False
            if row_match:
                return True

        col_match = True
        for column_num in range(0,len(self.board[0])):
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
                if board[location[0]][location[1]] == marker:
                    continue
                diag_match = False
            if diag_match:
                return True

        return False


new_board = board()
new_board.print_board()
