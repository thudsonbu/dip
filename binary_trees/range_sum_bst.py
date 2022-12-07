# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range
# [low, high].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0

        node_sum = 0

        if root.val >= low and root.val <= high:
            node_sum += root.val

        if root.left and root.val > low:
            node_sum += self.rangeSumBST(root.left, low, high)

        if root.right and root.val < high:
            node_sum += self.rangeSumBST(root.right, low, high)

        return node_sum
