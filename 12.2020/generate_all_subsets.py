# Given a list of unique numbers, generate all possible subsets without duplicates. 
# This includes the empty set as well.

def generateAllSubsets(nums):
    result = [[]]
    
    for num in nums:
        temp = []
        for x in result:
            temp.append(x)
            temp.append([*x, num])

        result = temp

    return result


print(generateAllSubsets([1, 2, 3]))


def insertRight( nums, base ):
    result = []
    idx = 0

    while idx < len(nums):
        new = base + [nums[idx]]
        result.append(new)

        if idx == 0:
            nextResult = insertRight( nums[1:], new )

        idx += 1

    return result + nextResult