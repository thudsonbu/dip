# A chess board is an 8x8 grid. Given a knight at any position (x, y) and a
# number of moves k, we want to figure out after k random moves by a knight, 
# the probability that the knight will still be on the chessboard. Once the 
# knight leaves the board it cannot move again and will be considered off the 
# board.

moves = [ 
  [  1,  2 ],
  [  1, -2 ],
  [ -1, -2 ],
  [ -1,  2 ],
  [  2,  1 ],
  [ -2,  1 ],
  [ -2, -1 ],
  [  2, -1 ]
]

def on_board_probability( x, y, k ):
  valid_moves = valid_knight_moves( x, y, k, 0)

  total_moves = 8 ** k

  return valid_moves / total_moves


def valid_knight_moves(x, y, k, m):

  onboard = ( x < 8 and x > -1 ) and ( y < 8 and y > -1 )

  if ( onboard and ( m == k ) ):
    return 1

  elif ( onboard ):
    count_onboard = 0

    for move in moves:
      count_onboard += valid_knight_moves( x + move[0], y + move[1], k, m + 1 )

    return count_onboard

  return 0

print( on_board_probability( 3, 3, 5 ) )


