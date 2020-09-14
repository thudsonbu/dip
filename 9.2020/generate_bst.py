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
        left_nums = [n for n in nums if n < num]
        right_nums = [n for n in nums if n > num]
        if len(left_nums) == 0 and len(right_nums) == 0:
            trees.append(Node(num,None,None))
            return trees
        elif len(left_nums) == 0:
            right_trees = generate_bst(right_nums)
            for right_tree in right_trees:
                trees.append(Node(num,None,right_tree))
            continue
        elif len(right_nums) == 0:
            left_trees = generate_bst(left_nums)
            for left_tree in left_trees:
                trees.append(Node(num,left_tree,None))
            continue
        elif len(right_nums) != 0 and len(left_nums) != 0:
            all_left_trees = generate_bst(left_nums)
            all_right_trees = generate_bst(right_nums)
            for left_tree in all_left_trees:
                for right_tree in all_right_trees:
                    trees.append(Node(num,left_tree,right_tree))
        else:
            print("Something is broken")
    return trees

def generate_bst_main(n):
    trees = generate_bst(range(1,n+1))
    return trees

for tree in generate_bst_main(3):
    print(tree)

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