# Given a list of numbers of size n, where n is greater than 3, find the maximum and minimum of 
# the list using less than 2 * (n - 1) comparisons.

def find_max_min(nums):
    comparison_limit = 2 * (len(nums) -1)
    comparisons = 0
    # max and min
    nums_max = nums_min = nums[0]
    # iterate through nums
    for i in range(1,len(nums)):
        number = nums[i]
        comparisons += 1
        if number > nums_max:
            nums_max = number
            continue
        elif number < nums_min:
            nums_min = number
        comparisons += 1
        
    return nums_max, nums_min, comparisons, comparison_limit

def find_max_min_better(nums):
    comparisons = 0
    max_comparisons = 2 * ( len(nums) -1)
    # if there is an odd number of numbers set start to be the last number
    comparisons += 1
    if (len(nums) % 2) == 1: 
        nums_min = nums_max = nums[-1]
    # if even set start numbers to be first number
    else:
        nums_min = nums_max = nums[0]
    while len(nums) > 1:
        # take chunk of two numbers
        two_nums = nums[0:2]
        # compare the two numbers
        comparisons += 1
        if two_nums[0] > two_nums[1]:
            higher = two_nums[0]
            lower = two_nums[1]
        else:
            higher = two_nums[1]
            lower = two_nums[0]
        # compare the lower of the two to the min
        comparisons += 1
        if lower < nums_min:
            # if its lower change min
            nums_min = lower
        # compare the higher of the two to the max
        comparisons += 1
        if higher > nums_max:
            # if its higher change the max
            nums_max = higher
        nums = nums[2::]
    return nums_max, nums_min, comparisons, max_comparisons


print(find_max_min([3,5,1,2,4,8,3,6,3,5,7,4,2,1]))
print(find_max_min_better([3,5,1,2,4,8,3,6,3,5,7,4,2,1]))