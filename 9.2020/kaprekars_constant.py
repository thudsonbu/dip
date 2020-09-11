# Hi, here's your problem today. This problem was recently asked by Facebook:

# Kaprekar's Constant is the number 6174. This number is special because it has the property where for any 4-digit number that has 2 or more unique digits, if you repeatedly apply a certain function it always reaches the number 6174.

# This certain function is as follows:
# - Order the number in ascending form and descending form to create 2 numbers.
# - Pad the descending number with zeros until it is 4 digits in length.
# - Subtract the ascending number from the descending number.
# - Repeat.

# Given a number n, find the number of times the function needs to be applied to reach Kaprekar's constant. Here's some starter code:

KAPREKAR_CONSTANT = 6174

def num_kaprekar_iterations(n):
    count = 0
    while not n == 6174:
        n = sort_descending_padded(n) - sort_ascending(n)
        count += 1
    return count

def sort_descending_padded(n):
    descending = sorted([n for n in str(n)], reverse=True)
    while len(descending) < 4:
        descending.append('0')
    return int("".join(descending))

def sort_ascending(n):
    ascending = sorted([n for n in str(n)])
    return int(''.join(ascending))



print(sort_descending_padded(13))
print(sort_ascending(1242527542))
print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)