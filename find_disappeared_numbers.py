# Given an array of integers of size n, where all elements are between 1 and n inclusive, 
# find all of the elements of [1, n] that do not appear in the array. Some numbers may 
# appear more than once.

# Example:
# Input: [4,5,2,6,8,2,1,5]
# Output: [3,7]

def findDisappearedNumbers(nums):
    num_list = [i for i in range(1,len(nums))]
    for num in nums:
        try:
            num_list.remove(num)
        except:
            continue
    return num_list

def findDisappearedNumbers2(nums):
    for i in range(len(nums)):
      index = abs(nums[i])-1
      nums[index] = -abs(nums[index])
    return [index for index, n in enumerate(nums, start=1) if n > 0]

print(findDisappearedNumbers([4,5,2,6,8,2,1,5]))
print(findDisappearedNumbers2([4,5,2,6,8,2,1,5]))