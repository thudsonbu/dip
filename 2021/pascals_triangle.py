# pascals trianlg is a tiranle where all numbers are the sum of the two numbers
# above it.

# given in integer n, generate the nth rown of pascals triangle

def pascal_triangle_row(n):
  if n == 1:
    return [1]

  row = []

  while True:
    # add ones to each side
    row.insert(0,1)
    row.append(1)

    if len(row) == n:
      break

    # combine each adjacent pair
    new_row = []
    for i in range( 0, len(row) - 1 ):
      new_row.append( row[i] + row[i+1] )

    row = new_row
  
  return row

print( pascal_triangle_row(4) )