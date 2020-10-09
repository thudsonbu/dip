# Hi, here's your problem today. This problem was recently asked by Google:

# Given a node in a binary search tree (may not be the root), find the next largest node in the binary search tree (also known as an inorder successor). The nodes in this binary search tree will also have a parent field to traverse up the tree.

# Here's an example and some starter code:

class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"(Value: {self.val}, Left: {self.left}, Right: {self.right})"

def inorder_successor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    else:
        search_val = node.val
        node = node.parent
        while node.val < search_val:
            node = node.parent
        return node

tree = Node(3)
tree.left = Node(2)
tree.right = Node(4)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(5)
tree.right.right.parent = tree.right
#     3
#    / \
#   2   4
#  /     \
# 1       5
print(inorder_successor(tree.left))
# 3
print(inorder_successor(tree.right))
# 5