# Hi, here's your problem today. This problem was recently asked by Google:

# Given a sorted list, create a height balanced binary search tree, meaning the height differences of each node can only differ by at most 1.

# Here's some code to start with:

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        answer = str(self.value)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer


def create_height_balanced_bst(nums):
    print("----------------")
    split_location = (int(len(nums)/2))
    lower_half = nums[0:split_location]
    print("Node left values: " + str(lower_half))
    upper_half = nums[split_location+1::]
    print("Node right values: " + str(upper_half))
    center_node_val = nums[split_location]
    print("Node: " + str(center_node_val))
    if len(upper_half) > 0:
        right_node = create_height_balanced_bst(upper_half)
    else:
        right_node = None
    if len(lower_half) > 0:
        left_node = create_height_balanced_bst(lower_half)
    else: 
        left_node = None
    center_node = Node(center_node_val,left_node,right_node)
    return center_node


tree = create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
tree2 = create_height_balanced_bst([1,2,3,4,5,6,7,8,9])
# 53214768
#  (pre-order traversal)
#       5
#      / \
#     3    7
#    / \  / \
#   2   4 6  8
#  /
# 1
