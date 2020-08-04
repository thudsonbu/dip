#Given a list of numbers of size n, where n is greater than 3, find the maximum and minimum of 
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


print(find_max_min([3,5,1,2,4,8]))