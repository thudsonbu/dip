# Hi, here's your problem today. This problem was recently asked by Microsoft:

# Given a tree, the leaves form a certain order from left to right. Two trees are considered "leaf-similar" if their leaf orderings are the same.

# For instance, the following two trees are considered leaf-similar because their leaves are [2, 1]:
#     3
#    / \ 
#   5   1
#    \
#     2 
#     7
#    / \ 
#   2   1
#    \
#     2 
# Our job is to determine, given two trees, whether they are "leaf similar."

class Node(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
  
class Solution(object):

    def leaf_similar(self, root1, root2):
        
        t1_leaves = self.leaves(root1)
        t2_leaves = self.leaves(root2)

        return t1_leaves == t2_leaves

    def leaves(self, root):
        left_leaves = []
        right_leaves = []

        if root.left:
            left_leaves = self.leaves(root.left)
        if root.right:
            right_leaves = self.leaves(root.right)
        if not root.right and not root.left:
            return [root.val]
        else:
            return left_leaves + right_leaves
        

t1 = Node(3)
t1.left = Node(5)
t1.right = Node(1)
t1.left.left = Node(6)
t1.left.right = Node(2)

#    7
#   / \ 
#  2   1
#   \
#    2 
t2 = Node(7)
t2.left = Node(2)
t2.right = Node(1)
t2.left.left = Node(6)
t2.left.right = Node(2)

print(Solution().leaf_similar(t1, t2))
# True
