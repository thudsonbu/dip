# Given a tree, the leaves form a certain order from left to right. Two trees 
# are considered "leaf-similar" if their leaf ordering are the same. Deterimine
# if the two provided trees are leaf similar

class Node(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
  
class Solution(object):
    def leafSimilar(self, root1, root2):
        root1_leaves = self.findLeaves(root1)
        root2_leaves = self.findLeaves(root2)
    
        return root1_leaves == root2_leaves

    def findLeaves(self, root):
        left = []
        right = []
        
        if root.left:
          left = self.findLeaves(root.left)

        if root.right:
          right = self.findLeaves(root.right)

        if not left and not right:
          return [ root.val ]
        else:
          return left + right
          
  #    3
#   / \ 
#  5   1
#   \
#    2 

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

print(Solution().leafSimilar(t1, t2))
# True
