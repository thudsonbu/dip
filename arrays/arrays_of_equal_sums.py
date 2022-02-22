# Given an array of numbers, determine whether it can be partitioned into 3
# arrays of equal sums.

class Solution(object):
    def canThreePartsEqualSumBruteForce(self, A):
      n = len(A)
      for i in range(0, n):
        for j in range(i, n):
          subset1 = sum(A[0:i])
          subset2 = sum(A[i:j])
          subset3 = sum(A[j:])
          if subset1 == subset2 and subset2 == subset3:
            return True
      return False

    def canThreePartsEqualSum(self, A):
      n = len(A)
      target = sum(A) / 3
      current = 0
      count = 0
      for n in A:
        current = current + n
        if current == target:
          current = 0J
          count = count + 1
      return current == 0 and count == 3


print(Solution().canThreePartsEqualSumBruteForce(
    [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
# True
print(Solution().canThreePartsEqualSumBruteForce(
    [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1, 3]))
# False

print(Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
# True
