# Given a binary tree representation of an arithmetic expression. In this
# tree, each leaf is an integer value, and a non-leaf node is one of the four
# operations: '+', '-', '*', or '/'. Write a function that evaluates this tree.

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate( root ):

  if not root.left and not root.right:
    return root.val

  if root.left:
    left = evaluate( root.left )

  if root.right:
    right = evaluate( root.right )

  return eval( str(left) + ' ' + root.val + ' ' + str(right) )

tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print( evaluate(tree) )
