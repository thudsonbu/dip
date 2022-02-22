# Hi, here's your problem today. This problem was recently asked by Uber:

# You are given a list of n numbers, where every number is at most k indexes away from its properly sorted index. Write a sorting algorithm (that will be given the number k) for this list that can solve this in O(n log k)

# Example:
# Input: [3, 2, 6, 5, 4], k=2
# Output: [2, 3, 4, 5, 6]
# As seen above, every number is at most 2 indexes away from its proper sorted index.

# Here's a starting point:
import heapq

def sort_partially_sorted(nums, k):
    length = len(nums)
    heapq.heapify(nums)
    out = []
    for num in range(length):
        out.append(heapq.heappop(nums))
    return out

def sort_partially_sorted2(nums, k):
    h = []
    sorted = []
    k += 1
    for n in nums[:k]:
        heapq.heappush(h,n)
    for n in nums[k:]:
        sorted.append(heapq.heapreplace(h, n))
    while len(h) > 0:
        sorted.append(heapq.heappop(h))
    return sorted

print(sort_partially_sorted([3, 2, 6, 5, 4], 2))
print(sort_partially_sorted2([3, 2, 6, 5, 4], 2))
