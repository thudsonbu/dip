# Hi, here's your problem today. This problem was recently asked by Twitter:

# Given an integer, check if that integer is a palindrome.

# def is_palindrome(n):
#   # Fill this in.

# print is_palindrome(1234321)
# # True
# print is_palindrome(1234322)
# # False

import math

def check_int_palendrom(num):
    if num == 0:
        return True
    k = int(math.log10(num))
    divisor = 10**k
    while num > 0:
        first_digit = num // divisor
        last_digit = num % 10
        if first_digit != last_digit:
            return False
        num = num % divisor
        num = num // 10
        divisor /= 100
    return True


def check_int_palendrom2(num):
    if num == 0:
        return True
    store = num
    zeros = 1
    while num >= zeros:
        zeros = zeros * 10
    zeros /= 10
    new_zeros = 1
    reversed_num = 0
    while num > 0:
        next_digit = int(num/zeros)
        reversed_num += next_digit*new_zeros
        num -= next_digit * zeros
        new_zeros *= 10
        zeros /= 10
    return reversed_num - store == 0

    # substract from itself reversed

def check_int_palendrom3(num):
    if num == 0:
        return True
    num = str(num)
    reverse_position = -1
    for position in range(0,int(len(num)/2)):
        if num[position] == num[reverse_position]:
            reverse_position -= 1
        else:
            return False
    return True



print("True " + str(check_int_palendrom(12321)))
print("False " + str(check_int_palendrom(12322)))
print("True " + str(check_int_palendrom(1)))
print("True " + str(check_int_palendrom(123321)))
print("True " + str(check_int_palendrom(0)))

print("True " + str(check_int_palendrom2(12321)))
print("False " + str(check_int_palendrom2(12322)))
print("True " + str(check_int_palendrom2(1)))
print("True " + str(check_int_palendrom2(123321)))
print("True " + str(check_int_palendrom2(0)))

print("True " + str(check_int_palendrom3(12321)))
print("False " + str(check_int_palendrom3(12322)))
print("True " + str(check_int_palendrom3(1)))
print("True " + str(check_int_palendrom3(123321)))
print("True " + str(check_int_palendrom3(0)))