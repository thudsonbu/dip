# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only
# constant extra space.

# Return the duplicate number.

# Intuition
# If there are duplicates in the array, there should be a cycle when navigating
# by jumping to the index at nums[n].

# Solution
# Use Floyd's tortoise and hare algorithm to find the cycle.

class Solution:
    def findDuplicate(self, nums):
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
