
# You are given two strings, A and B. Return whether A can be shifted some number of times to get B.

# Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get 
# B. A = abc and B= acb should return false.

def is_shifted(a, b):
    for i in range(len(b)):
        if b == a:
            return True
        b = b[-1] + b[0:-1]
    return False

def is_shifted2(a, b):
    if len(a) != len(b):
        return False
    return b in a + a

print(is_shifted('abcde', 'cdeab'))

# both solutions are O(N)^2 time worst case.