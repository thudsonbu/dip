class Solution:
    def isMonotonic(self, nums):
        direction = nums[-1] > nums[0] and 1 or -1

        for i in range(len(nums) - 1):
            if not direction * (nums[i + 1] - nums[i]) >= 0:
                return False

        return True


mySolution = Solution()

assert mySolution.isMonotonic([1, 2, 2, 3]) == True
assert mySolution.isMonotonic([6, 5, 4, 4]) == True
assert mySolution.isMonotonic([1, 3, 2]) == False
assert mySolution.isMonotonic([1, 2, 4, 5]) == True
assert mySolution.isMonotonic([1, 1, 1]) == True
assert mySolution.isMonotonic([3, 1, 1]) == True
