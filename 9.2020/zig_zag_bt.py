# Hi, here's your problem today. This problem was recently asked by Apple:

# Given a binary tree, return the list of node values in zigzag order traversal. 
# Here's an example

# # Input:
# #         1
# #       /   \
# #      2     3
# #     / \   / \
# #    4   5 6   7
# #
# # Output: [1, 3, 2, 4, 5, 6, 7]

# Here's some starter code

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_order(tree):
    pre_arr = get_tree_array(tree)
    zig_arr = [pre_arr.pop(0)]
    traverse_backward = True
    skip = int(len(pre_arr)/2)
    while skip >= 1:
        arr_to_append = []
        pos = len(pre_arr) - skip
        while pos >= 0:
            arr_to_append.append(pre_arr.pop(pos))
            pos -= skip
        if traverse_backward:
            zig_arr += arr_to_append
        else:
            zig_arr += reversed(arr_to_append)
        traverse_backward = False if traverse_backward else True
        skip = int((skip - 1)/2)
    return zig_arr

        

    return 

def get_tree_array(tree):
    arr = [tree.value]
    if tree.left:
        arr += get_tree_array(tree.left)
    if tree.right:
        arr += get_tree_array(tree.right)
    return arr

n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))
print(get_tree_array(n1))
# [1, 3, 2, 4, 5, 6, 7]