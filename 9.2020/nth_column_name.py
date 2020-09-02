# Hi, here's your problem today. This problem was recently asked by Apple:

# In many spreadsheet applications, the columns are marked with letters. 
# From the 1st to the 26th column the letters are A to Z. Then starting from 
# the 27th column it uses AA, AB, ..., ZZ, AAA, etc.

def nth_col_name(num):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    if num <= 26:
        return letters[num-1]

    out = ""
    increment = 1
    while num > increment*26:
        increment *= 26

    letter = -1
    while True:
        while num > increment:
            num = num - increment
            letter += 1
        out += letters[letter]
        if increment == 1:
            break
        increment /= 26
        letter = 0
    return out

print(nth_col_name(1))
print(nth_col_name(5))
print(nth_col_name(26))
print(nth_col_name(27))
print(nth_col_name(28))
print(nth_col_name(52))
print(nth_col_name(53))
print(nth_col_name(677))
print(nth_col_name(1000))
