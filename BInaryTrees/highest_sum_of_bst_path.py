# You are given the root of a binary tree. Find the path between 2 nodes that 
# maximizes the sum of all the nodes in the path, and return the sum. The path does
#  not necessarily need to go through the root.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.highest_path = 0


    def max_path_sum(self, root):
        if not root.left and not root.right:
            return root.val
        if root.left:
            left_sum = self.max_path_sum(root.left)
        else:
            left_sum = 0
        if root.right:
            right_sum = self.max_path_sum(root.right)
        else:
            right_sum = 0
        self.highest_path = max(self.highest_path, left_sum + root.val + right_sum)
        if left_sum > right_sum:
            return left_sum + root.val
        else:
            return right_sum + root.val
        


root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
 
Solver = Solution()

Solver.max_path_sum(root)

print(Solver.highest_path)