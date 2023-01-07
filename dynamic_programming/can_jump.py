# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum jump
# length at that position.

# Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, n: list[int]) -> bool:
        if 0 not in n[:-1] or len(n) == 1:
            return True

        pt = n.index(0)

        for i in range(len(n)):
            if i <= pt and i + n[i] > pt:
                pt = i + n[i]

            if i == pt and not n[i]:
                return False

            if pt >= len(n)-1:
                return True

        return True
