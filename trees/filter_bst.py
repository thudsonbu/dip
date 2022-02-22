# Given a binary tree and an integer k, filter the binary tree such that its
# leaves don't contain the value k. Here are the rules:

# - If a leaf node has a value of k, remove it.
# - If a parent node has a value of k, and all of its children are removed, remove it.


class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"value: {self.value}, left: ({self.left.__repr__()}), right: ({self.right.__repr__()})"

def filter(tree, k):
  
  if tree.right:
    cutRight = filter(tree.right, k)
  else:
    cutRight = True

  if tree.left:
    cutLeft = filter(tree.left, k)
  else:
    cutLeft = True

  if cutRight and cutLeft and (tree.value == k):
    return True

  if cutRight:
    tree.right = None
  
  if cutLeft:
    tree.left = None
  

#     1
#    / \
#   1   1
#  /   /
# 2   1
n5 = Node(2)
n4 = Node(1)
n3 = Node(1, n4)
n2 = Node(1, n5)
n1 = Node(1, n2, n3)



filter(n1, 1)

print(n1)
#     1
#    /
#   1
#  /
# 2
# value: 1, left: (value: 1, left: (value: 2, left: (None), right: (None)), right: (None)), right: (None)
