import math

class Solution:
	def search_insert(self, nums, target):
		if len(nums) == 0:
			return 0

		if target <= nums[0]:
			return 0

		if target > nums[len(nums) - 1]:
			return len(nums)

		low = 0
		high = len(nums) - 1

		while low < high - 1:
			center = math.floor((high - low)/2) + low
			num = nums[center]

			if num == target:
				return center
			elif num > target:
				high = center
			elif num < target:
				low = center

		return low + 1

sol = Solution()

assert sol.search_insert([1,3,4,5], 2) == 1
assert sol.search_insert([1,2,3,4], 0) == 0
assert sol.search_insert([1,2,3,4,5], 4) == 3
assert sol.search_insert([1,2,3,4,5], 7) == 5
assert sol.search_insert([], 3) == 0
assert sol.search_insert([1], 1) == 0
