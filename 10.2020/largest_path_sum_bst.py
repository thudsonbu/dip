# Hi, here's your problem today. This problem was recently asked by Google:

# Given a binary tree, find and return the largest path from root to leaf.

# Here's an example and some starter code:

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def largest_path_sum(tree):
    if tree.right:
        right_sum, right_arr = largest_path_sum(tree.right)
    else:
        right_sum, right_arr = 0, []
    if tree.left:
        left_sum, left_arr = largest_path_sum(tree.left)
    else:
        left_sum, left_arr = 0, []
        
    if right_sum > left_sum:
        return right_sum + tree.value, right_arr + [tree.value]
    else:
        return left_sum + tree.value, left_arr + [tree.value]
    

tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.left.right = Node(5)
#    1
#  /   \
# 3     2
#  \   /
#   5 4
found_sum, arr = largest_path_sum(tree)
print("Found sum: " + str(found_sum))
print("Found arr: " + str(arr))
