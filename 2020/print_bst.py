# Given the root of a binary tree, print its level-order traversal. For example:

class Node: 
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root):
    tree_print = []
    if root.left:
        tree_print.append(root.val)
        tree_print += print_tree(root.left)
        tree_print += print_tree(root.right)
    else:
        tree_print.append(root.val)
    return tree_print

root = Node(1, Node(2), Node(3, Node(4), Node(5)))

print(print_tree(root))