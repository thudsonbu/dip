# PROBLEM STATEMENT:
# Given an integer, reverse the digits. Do not cover the integer into a string and reverse it.

def reverse_integer(num):
    result = 0
    negative = 1

    if num < 0:
        negative = -1
        num *= -1

    while num > 0:
        result = result * 10 + num % 10
        num //= 10

    return negative * result


print(reverse_integer(135))
print(reverse_integer(-135))