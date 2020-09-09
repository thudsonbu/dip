# Hi, here's your problem today. This problem was recently asked by Google:

# A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number of moves k, 
# we want to figure out after k random moves by a knight, the probability that the knight will 
# still be on the chessboard. Once the knight leaves the board it cannot move again and will be 
# considered off the board.

def is_knight_on_board(x,y,k):
    total_theoretical_moves = 8**k
    all_possible_moves = get_valid_moves(x,y,k)
    return len(all_possible_moves) / total_theoretical_moves

def get_valid_moves(x,y,k):
    valid_moves = check_valid_moves(x,y)
    if k > 1:
        sub_moves = []
        for move in valid_moves:
            sub_moves += get_valid_moves(move[0],move[1],k-1)
        return valid_moves + sub_moves
    return valid_moves

def check_valid_moves(x,y):
    moves = [[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1]]
    valid_moves = []
    for move in moves:
        if x + move[0] in range(0,8) and y + move[1] in range(0,8):
            new_cor = [x + move[0], y + move[1]]
            valid_moves.append(new_cor)
    return valid_moves

print(is_knight_on_board(4,4,1))
print(is_knight_on_board(0,0,1))
print(is_knight_on_board(0,0,2))