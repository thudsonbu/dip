#You are given an array of integers. Return the length of the longest consecutive elements 
# sequence in the array. For example, the input array [100, 4, 200, 1, 3, 2] has the longest 
# consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.


# MEH time complexity solution
def findSequence(nums):
    nums = sorted(nums)
    longest = 0
    count = 1
    for i in range(1,len(nums)):
        if nums[i-1] == nums[i]-1:
            count += 1
            longest = max(count, longest)
        else:
            count = 1
    return longest

print(findSequence([100,4,200,1,3,2]))

# MEH space complexity solution
def findSequence2(nums):
    max_len = 0
    bounds = dict()
    for num in nums:
        print(bounds)
        if num in bounds:
            continue
        left_bound, right_bound = num, num
        if num - 1 in bounds:
            left_bound = bounds[num - 1][0]
        if num + 1 in bounds:
            right_bound = bounds[num + 1][1]
        bounds[num] = left_bound, right_bound
        bounds[left_bound] = left_bound, right_bound
        bounds[right_bound] = left_bound, right_bound
        max_len = max(right_bound - left_bound + 1, max_len)
    return max_len       

print(findSequence2([100,4,200,1,3,2]))