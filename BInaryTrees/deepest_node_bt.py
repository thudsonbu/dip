# Given a binary tree, find the node which is farthest from the root

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val


def deepest(node):
  if node.left:
    left = deepest(node.left)
  else:
    left = 0
  
  if node.right:
    right = deepest(node.right)
  else:
    right = 0

  return max( left, right ) + 1


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')
root.left.left.left = Node('e')

print(deepest(root))
# (d, 3)
