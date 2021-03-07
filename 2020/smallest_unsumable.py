# Given a sorted list of positive numbers, find the smallest positive number 
# that cannot be a sum of any subset in the list.

def findSmallest(nums):
    used = []
    Found = False
    num_to_check = 1
    while not Found:
        if num_to_check in nums:
            num_to_check += 1
            continue
        for i in range(1,num_to_check):
            num_1 = i
            num_2 = num_to_check - i
            if num_1 in nums and num_2 in nums:
                break
            if num_1 == num_to_check -1:
                return num_to_check
        num_to_check += 1
        if num_to_check > 1000:
            break
    return "error"

print(findSmallest([1, 2, 3, 8, 7, 9, 10]))