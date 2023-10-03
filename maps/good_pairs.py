from collections import defaultdict
from typing import List

# Given an array of integers nums, return the number of good pairs. A pair (i,
# j) is called good if nums[i] == nums[j] and i < j.


def num_good_pairs(nums: List[int]) -> int:
    counts = defaultdict(int)
    ans = 0

    for num in nums:
        ans += counts[num]
        counts[num] += 1

    return ans


assert num_good_pairs([1, 2, 3, 1, 1, 3]) == 4
assert num_good_pairs([1, 1, 1, 1]) == 6
assert num_good_pairs([1, 2, 3]) == 0
