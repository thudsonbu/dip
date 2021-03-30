# Given an integer k and a binary search tree find the floor and ceiling for k
# meaning the number nearest below k and the number nearest above
# k.

class Node:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val

def findCeilingFloor(root, k, floor=None, ceil=None):
  # if node is equal return floor = k, ceil = k
  if root.val == k:
    return [ k, k ]

  if root.val > k:
    if root.left:
      return findCeilingFloor(root.left, k, floor, root.val)
    else:
      return [ floor, root.val ]

  else:
    if root.right:
      return findCeilingFloor(root.right, k, root.val, ceil)
    else:
      return [ root.val , ceil ]

root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root, 5))
# (4, 6)
