# Hi, here's your problem today. This problem was recently asked by Microsoft:

# Given a binary tree, find the level in the tree where the sum of all nodes on that level is the greatest.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"

def tree_level_max_sum(root):
    root_val, sums_arr = tree_level_max_sum_helper(root)

    max_sum = root_val

    for level_sum in sums_arr:
        max_sum = max(max_sum, level_sum)
    
    return max_sum

def tree_level_max_sum_helper(root):
    arr = []

    if root.left:
        left_val, left_arr = tree_level_max_sum_helper(root.left)
    else:
        left_val, left_arr = 0, []

    if root.right:
        right_val, right_arr = tree_level_max_sum_helper(root.right)
    else:
        right_val, right_arr = 0, []

    # while there are items in both arrays sum them and add them to the new array (this is the sum of a level)
    while right_arr and left_arr:
        arr.insert(0, right_arr.pop(0) + left_arr.pop(0))
    
    # if there are some left over in the right append them (if the left arr did not go as deep)
    while right_arr:
        arr.insert(0, right_arr.pop(0))

    # if there are some left over in the left arr append them
    while left_arr:
        arr.insert(0, left_arr.pop(0))

    # finally insert the sums of the two new values from each branch
    arr.insert(0, left_val + right_val)

    return root.value, arr

n3 = Node(4, Node(3), Node(2))
n2 = Node(5, Node(4), Node(-1))
n1 = Node(1, n2, n3)

"""
    1          Level 0 - Sum: 1
   / \
  4   5        Level 1 - Sum: 9 
 / \ / \
3  2 4 -1      Level 2 - Sum: 8

"""

assert tree_level_max_sum(n1) == 9, "Highest level sum should be 9"
# Should print 1 as level 1 has the highest level sum
