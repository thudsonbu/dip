# Given an array of integers, arr, where all numbers occur twice except one 
# number which occurs once, find the number. Your solution should ideally be 
# O(n) time and use constant extra space.

def find_single(nums):
    # sum numbers in array with twins
    sum_twins = 0
    for num in nums:
        sum_twins += num
    # cast array with twins to set to eliminate duplicates
    twins_set = set(nums)
    # sum array without twins 
    sum_set = 0
    for num in twins_set:
        sum_set += num
    # multiply sum * 2
    sum_set = sum_set * 2
    # subtract second sum from first sum revealing single num
    difference = sum_set - sum_twins
    return difference

def find_single2(nums):
    # running product of XOR
    nums_sum = 0
    # for each num in nums
    for num in nums:
        # take the XOR of the sum and num
        nums_sum ^= num
        # if the num is within the product it will be reduced to zero
    return nums_sum

numbers_array = [1, 1, 3, 4, 4, 5, 6, 5, 6]

print(find_single(numbers_array))
print(find_single2(numbers_array))