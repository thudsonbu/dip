# Hi, here's your problem today. This problem was recently asked by Microsoft:

# Given a list of sorted numbers (can be both negative or positive), return the list of numbers squared in sorted order.

# Begin from the negative and positve sides appending which has higher absolute value squared
def square_numbers2(nums):
    sorted_list = []
    # For each number in nums append the higher of start and end and get a new start or end
    for i in range(len(nums)):
        start = nums[0]
        end = nums[-1]
        if start*start > end*end:
            sorted_list.insert(0, start*start)
            nums.pop(0)
        else:
            sorted_list.insert(0, end*end)
            nums.pop(-1)
    return sorted_list

# Begin from the negative and positve sides appending which has higher absolute value squared
def square_numbers(nums):
    sorted_list = []
    start = nums.pop(0)
    end = nums.pop(-1)
    # For each number in nums append the higher of start and end and get a new start or end
    for i in range(len(nums)):
        if start*start > end*end:
            sorted_list.insert(0, start*start)
            start = nums.pop(0)
        else:
            sorted_list.insert(0, end*end)
            end = nums.pop(-1)
    # When length 0 is reached two numbers will still remain as start and end and must be added
    if start*start > end*end:
        sorted_list.insert(0, start*start)
        sorted_list.insert(0, end*end)
    else:
        sorted_list.insert(0, end*end)
        sorted_list.insert(0, start*start)
    return sorted_list



print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
print(square_numbers2([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]
