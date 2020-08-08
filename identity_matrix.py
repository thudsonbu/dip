# Create a function that takes an integer n and returns the identity matrix of n x n 
# dimensions. For this challenge, if the integer is negative, return the mirror image 
# of the identity matrix of n x n dimensions.. It does not matter if the mirror image 
# is left-right or top-bottom.

def id_mtrx(n):
    matrix = []
    try:
        # create blank matrix
        for i in range(0,abs(n)):
            new_arr = [0 for item in range(0,abs(n))]
            matrix.append(new_arr)
        # add ones
        if n < 0:
            one_location = 0
            for y in range(0,abs(n)):
                one_location -= 1
                matrix[y][one_location] = 1
        else:
            one_location = 0
            for y in range(0,abs(n)):
                matrix[y][one_location] = 1
                one_location += 1
    except:
        matrix = "Error"
    return matrix

print(id_mtrx(-2))