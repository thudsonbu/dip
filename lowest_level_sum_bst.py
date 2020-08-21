
# You are given the root of a binary tree. Find the level for the binary tree with the minimum sum, 
# and return that value.

class Node: 
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def miniumum_level_sum(root):
    min_sum = root.val
    children = [root]
    while(len(children) > 0):
        current_level_sum = 0
        for node in children:
            current_level_sum += node.val
        min_sum = min(current_level_sum, min_sum)
        new_children = []
        for node in children:
            if node.left:
                new_children.append(node.left)
            if node.right:
                new_children.append(node.right)
        children = new_children
    return min_sum

node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print(miniumum_level_sum(node))