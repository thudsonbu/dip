# Hi, here's your problem today. This problem was recently asked by 
# Amazon:

# Given a number n, generate all binary search trees that can be 
# constructed with nodes 1 to n.

# Here's some code to start with:

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    result = str(self.value)
    if self.left:
      result = result + str(self.left)
    if self.right:
      result = result + str(self.right)
    return result

def generate_bst(nums):
    trees = []
    for num in nums:
        nums_left = range(num)
        print(nums_left)
        nums_right = range(num+2,nums[-1])
        print(nums_right)
        left_trees = generate_bst(nums_left)
        right_trees = generate_bst(nums_right)
        for tree_left in left_trees:
            for tree_right in right_trees:
                new_node = Node(num,tree_left,tree_right)
                trees.append(new_node)
        if len(left_trees) == 0:
            for tree_right in right_trees:
                new_node = Node(num,None,tree_right)
                trees.append(new_node)
        if len(right_trees) == 0:
            for tree_left in left_trees:
                new_node = Node(num,tree_left,None)
                trees.append(new_node)
    return trees

def generate_bst_main(n):
    trees = generate_bst(range(n+1))
    return trees

    


for tree in generate_bst_main(3):
    print(tree)
    print("bacon")

# Pre-order traversals of binary trees from 1 to n.
# 123
# 132
# 213
# 312
# 321

#   1      1      2      3      3
#    \      \    / \    /      /
#     2      3  1   3  1      2
#      \    /           \    /
#       3  2             2  1