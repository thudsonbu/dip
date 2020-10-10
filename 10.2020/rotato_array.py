# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given an array and an integer k, rotate the array by k spaces. Do this without generating a new array and without using extra space.

# Here's an example and some starter code

def rotate_list(nums, k):
    old_pos = 0
    old_num = nums[old_pos]
    new_pos = get_pos(old_pos, len(nums), k)
    new_num = nums[new_pos]
    for num in nums:
        


def get_pos(pos, len, k):
    new_pos = pos + k
    if new_pos > len:
        return new_pos - k
    else:
        return new_pos

a = [1, 2, 3, 4, 5]
rotate_list(a, 2)
print(a)
# [3, 4, 5, 1, 2]