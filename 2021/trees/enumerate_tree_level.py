# Given a binary tree, return all values given a certain height h.

class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, target_height, current_height ):
  if current_height == target_height:
    return [root.value]

  else:
    out = []

    if root.left:
      out = out + valuesAtHeight(root.left, target_height, current_height + 1)

    if root.right:
      out = out + valuesAtHeight(root.right, target_height, current_height + 1)

    return out



#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print( valuesAtHeight(a, 3, 1) )
# [4, 5, 7]
