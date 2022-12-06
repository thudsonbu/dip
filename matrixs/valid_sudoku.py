import math

nilVal = '.'

class Solution:
    def isValidSudoku(self, board):
        return self.checkRows(board) and self.checkBoxes(board) and self.checkColumns(board)

    def checkRows(self, board):
        for r in range(len(board)):
            row = board[r]
            seen = set()

            for i in range(len(row)):
                ch = row[i]

                if ch == nilVal:
                    continue

                preLen = len(seen)

                seen.add(ch)

                if preLen == len(seen):
                    return False

        return True

    def checkColumns(self, board):
        for c in range(len(board[0])):
            seen = set()

            for i in range(len(board)):
                ch = board[i][c]

                if ch == nilVal:
                    continue

                preLen = len(seen)

                seen.add(ch)

                if preLen == len(seen):
                    return False

        return True

    def checkBoxes(self, board):
        xOffset = 0
        yOffset = 0
        cellSize = math.floor(len(board) / 3)

        for i in range(1, 10):
            seen = set()

            for r in range(yOffset, (yOffset + cellSize)):
                for c in range(xOffset, (xOffset + cellSize)):
                    ch = board[r][c]

                    if ch == nilVal:
                        continue

                    preLen = len(seen)

                    seen.add(ch)

                    if preLen == len(seen):
                        print(ch, r, c)
                        return False

            if i % 3 == 0:
                xOffset = 0
                yOffset += 3
            else:
                xOffset += 3

        return True

sol = Solution()

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

board2 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6","5",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

assert sol.isValidSudoku(board) == True
assert sol.isValidSudoku(board2) == False
