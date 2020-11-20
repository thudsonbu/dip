# Given an integer n, generate the n-th row of the Pascal's Triangle.

# brute force
def pascals_triangle_row(n):
    len = n + 1
    triangle = [[1] * i for i in range(1, len)] # add sub lists

    for i in range(n): # triangle level
        for j in range(1, i): # triangle level pos
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    return triangle[-1]

print(pascals_triangle_row(6))

# memory conservation
def pascals_triangle_row2(n):
    row = [1] * n

    for i in range(n):
        last = row[0]
        for j in range(1, i):
            temp = row[j]
            row[j] = last + row[j]
            last = temp

    return row

print(pascals_triangle_row(6))


