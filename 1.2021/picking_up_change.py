# Given a 2d n x m matrix where each cell has a certain amount of change on the
# floor, your goal is to start from the top left corner mat[0][0] and end in the
# bottom right corner max[n-1][m-1] with the most amount of change. You can only
# move either left or down.

def traceroute( x, y, mat ):

  if ( len( mat[0] ) - 1) > x:
    right_sum = traceroute( x + 1, y, mat ) + mat[y][x]
  else:
    right_sum = mat[y][x]

  if ( len( mat ) - 1 ) > y:
    down_sum = traceroute( x, y + 1, mat ) + mat[y][x]
  else:
    down_sum = mat[y][x]

  return max( right_sum, down_sum )

mat = [
  [0, 3, 0, 2],
  [1, 2, 3, 3],
  [6, 0, 3, 2]
]

assert traceroute( 0, 0, mat ) == 13