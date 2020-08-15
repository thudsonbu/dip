# You are given an array of integers, and an integer K. Return the subarray which sums to K.
#  You can assume that a solution will always exist.

def find_sum(nums, target):
    current_sum = 0
    sub_array = []
    for num in nums:
        current_sum += num
        sub_array.append(num)
        while current_sum > target:
            current_sum -= sub_array.pop(0)
        if current_sum == target:
            return sub_array

def find_continuous_k(list, k):
    previous = dict()
    sum = 0
    # sublist starting at the zeroth position work.
    previous[0] = -1
    for last_idx, item in enumerate(list):
        sum += item
        previous[sum] = last_idx
        first_idx = previous.get(sum - k)
        if first_idx is not None:
            return list[first_idx + 1:last_idx + 1]
    return None

print(find_sum( [1,3,2,5,7,2], 14))
print(find_continuous_k( [1,7,3,2,5,2], 14))

    