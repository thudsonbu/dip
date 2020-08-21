 # You are given the root of a binary tree, along with two nodes, A and B. Find and
 #  return the lowest common ancestor of A and B. For this problem, you can assume 
 # that each node also has a pointer to its parent, along with its left and right 
 # child.

class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


def lowestCommonAncestor(root, a, b):
    depth_a = 0
    parent = a.parent
    while(parent):
        depth_a +=1
        parent = parent.parent
    depth_b = 0
    parent = b.parent
    while(parent):
        depth_b +=1
        parent = parent.parent
    if depth_a > depth_b:
        a_pos = a
        for i in range(depth_a-depth_b):
            a_pos = a_pos.parent
        b_pos = b
    else:
        b_pos = b
        for i in range(depth_b-depth_a):
            b_pos = b_pos.parent
        a_pos = a
    while(True):
        if b_pos.val == a_pos.val:
            return b_pos
        else:
            b_pos = b_pos.parent
            a_pos = a_pos.parent

#   a
#  / \
# b   c
#    / \
#   d*  e*
root = TreeNode('a')
root.left = TreeNode('b')
root.left.parent = root
root.right = TreeNode('c')
root.right.parent = root
a = root.right.left = TreeNode('d')
root.right.left.parent = root.right
b = root.right.right = TreeNode('e')
root.right.right.parent = root.right

print(lowestCommonAncestor(root, a, b).val)