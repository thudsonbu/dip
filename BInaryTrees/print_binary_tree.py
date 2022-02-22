# Hi, here's your problem today. This problem was recently asked by Apple:

# You are given a tree, and your job is to print it level-by-level with linebreaks.

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g

# The output should be
# a
# bc
# defg
# Here's a starting point:

from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        bst_map = {}
        depth = 0
        new_map, max_depth = self.get_all(self,bst_map,depth)
        out = ''
        for i in range(max_depth+1):
            out += (new_map.get(i))
            out += '\n'
        return out
    

    def get_all(self, node, bst_map, depth):
        try:
            current = bst_map[depth]
            current += str(node.val)
        except:
            current = str(node.val)
        bst_map[depth] = current
        if node.left:
            store, max_depth_right = self.get_all(node.left, bst_map, depth + 1)
        if node.right:
            store, max_depth_left = self.get_all(node.right, bst_map, depth + 1)
        if node.left or node.right:
            max_depth = max(max_depth_left,max_depth_right)
        else:
            max_depth = depth
        return bst_map, max_depth
        

tree = Node('a')
tree.left = Node('b')
tree.right = Node('c')
tree.left.left = Node('d')
tree.left.right = Node('e')
tree.right.left = Node('f')
tree.right.right = Node('g')

print(tree)