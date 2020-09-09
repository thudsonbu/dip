def is_knight_on_board(x,y,k):
    total_theoretical_moves = 8**k
    current_postion = []
    current_postion.append(x)
    current_postion.append(y)
    all_possible_moves = get_valid_moves(current_postion,k)
    return len(all_possible_moves) / total_theoretical_moves

def get_valid_moves(position, k):
    if k == 0:
        return []
    valid_moves = check_valid_moves(position)
    length = len(valid_moves)
    for i in range(length):
        move = valid_moves[i]
        valid_moves += get_valid_moves(move,k-1)
    return valid_moves

def check_valid_moves(input_position):
    x = input_position[0]
    y = input_position[1]
    moves = [[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1]]
    valid_moves = []
    for move in moves:
        valid_x = False
        valid_y = False
        if x + move[0] >= 0 and x + move[0] <= 7:
            valid_x = True
        if y + move[1] >= 0 and y + move[1] <= 7:
            valid_y = True
        if valid_x and valid_y:
            new_cor = []
            new_cor.append(x + move[0])
            new_cor.append(y + move[1])
            valid_moves.append(new_cor)
    return valid_moves

print(is_knight_on_board(4,4,1))
print(is_knight_on_board(0,0,1))
print(is_knight_on_board(0,0,2))