import math

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


class Solution:
    def searchMatrix(self, matrix, target):
        # Perform a binary search using the first element of each row
        high = len(matrix)-1
        low = 0

        while low <= high:
            center = math.floor(low + ((high - low)/2))

            if matrix[center][0] < target:
                low = center
            else:
                high = center

        # Search row where element should be within (this row should have a start less than the target)
        searchRow = matrix[low] if target < matrix[high][0] else matrix[high]

        for element in searchRow:
            if element == target:
                return True

        return False

    def searchMatrix2(self, matrix, target):
        m = len(matrix)

        if m == 0:
            return False

        n = len(matrix[0])

        # binary search
        left = 0
        right = m * n - 1

        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]

                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1

        return False
