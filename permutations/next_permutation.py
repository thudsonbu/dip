class Solution:
    def nextPermutation(self, nums):
        if len(nums) < 2:
            return nums

        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1

        if i < 0:
            nums.reverse()
            return nums

        j = len(nums) - 1
        while nums[i] >= nums[j]:
            j -= 1

        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

        self.reverse(i, nums)

    def reverse(self, i, nums):
        l, r = i + 1, len(nums) - 1

        while l < r:
            tmp = nums[r]
            nums[r] = nums[l]
            nums[l] = tmp

            l += 1
            r -= 1
