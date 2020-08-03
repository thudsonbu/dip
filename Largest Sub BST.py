class TreeNode:
    def __init__(self, key):
        self.left = None # left node
        self.right = None # right node
        self.key = key # node value
    
    def __str__(self):
        answer = str(self.key)
        if self.left:
            answer += str(self.key)
        if self.right:
            answer += str(self.right)
        return answer

class Solution:

    # Solution constructor
    def __init__(self):
        self.max_root = None
        self.max_size = 0

    def largest_bst_subtree(self, root):
        self.max_size = 0
        self.max_root = None

        def helper(root): # checks if root is the top of a valid tree
            # check if we have a node (if right or left node is blank)
            if root is None:
                return(0, float('inf'), float('-inf'))
            left = helper(root.left) # recursively call tree check
            right = helper(root.right) # recursively call tree check
            # check if max key from left size is less then root and if min key from left is greater then root (valid tree)
            if root.key > left[2] and root.key < right[1]:
                # add sizes of left and right trees to get total size
                size = left[0] + right[0] + 1
                # reset max size if larger (max size of solution class)
                if size > self.max_size:
                    self.max_size = size
                    self.max_root = root
                return (size, min(root.key, left[1]), max(root.key, right[2]))
            # the tree is not valid so return a size of 0
            else:
                return(0, float('-inf'), float('inf'))
        
        # run helper on input object
        helper(root)
        return self.max_size

node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)

potato = Solution()
print(potato.largest_bst_subtree(node))