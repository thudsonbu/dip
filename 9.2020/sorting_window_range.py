# Hi, here's your problem today. This problem was recently asked by Twitter:

# Given a list of numbers, find the smallest window to sort such that the whole list will be sorted. If the list is already sorted return (0, 0). You can assume there will be no duplicate numbers.

# Example:
# Input: [2, 4, 7, 5, 6, 8, 9]
# Output: (2, 4)
# Explanation: Sorting the window (2, 4) which is [7, 5, 6] will also means that the whole list is sorted.

def min_window_to_sort(nums):
    mistake = False
    mistake_fixed = True
    biggest_mistake = nums[0]
    first_mistake_pos = len(nums)
    last_mistake_pos = 0

    for i in range(1,len(nums)):
        current_number, previous_num = nums[i], nums[i-1]
        if current_number < previous_num:
            mistake = True
            mistake_fixed = False
            biggest_mistake = previous_num if previous_num > biggest_mistake else biggest_mistake
            first_mistake_pos = i-1 if i-1 < first_mistake_pos else first_mistake_pos
        elif current_number > biggest_mistake and not mistake_fixed:
            last_mistake_pos = i-2
            biggest_mistake = nums[0] - 1
            mistake_fixed = True

    last_mistake_pos = len(nums)-1 if not mistake_fixed else last_mistake_pos

    mistake_fixed = True
    biggest_mistake = nums[len(nums)-1]
    first_mistake_pos_desc = 0
    last_mistake_pos_desc = len(nums)

    for i in reversed(range(0,len(nums)-1)):
        current_number, previous_num = nums[i], nums[i+1]
        if current_number > previous_num:
            mistake = True
            mistake_fixed = False
            biggest_mistake = previous_num if previous_num < biggest_mistake else biggest_mistake
            first_mistake_pos_desc = i+1 if i+1 > first_mistake_pos_desc else first_mistake_pos_desc
        elif current_number > biggest_mistake and not mistake_fixed:
            last_mistake_pos_desc = i+2
            biggest_mistake = nums[len(nums)-1]
            mistake_fixed = True

    last_mistake_pos_desc = 0 if not mistake_fixed else last_mistake_pos_desc

    left = min(last_mistake_pos_desc,first_mistake_pos)
    right = max(first_mistake_pos_desc,last_mistake_pos)

    if mistake:
        return (left,right)
    else:
        return None


print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
print(min_window_to_sort([3, 2, 1, 4, 5, 6, 7]))
print(min_window_to_sort([1, 2, 3, 4, 0, 5, 6]))
# (2, 4)