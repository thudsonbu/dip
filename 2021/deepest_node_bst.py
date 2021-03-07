# you are given the root of a binary tree, return the deepest node (furthest
# from the root)

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
        left_depth = deepest(node.left) or 0
    else:
        left_depth = 0

    if node.right:
        right_depth = deepest(node.right)
    else:
        right_depth = 0

    return max(left_depth, right_depth) + 1


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
