class Node(object):

      def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def visualize_bst(preorder, inorder):
    # find the root
    root = Node(preorder[0])
    if len(preorder) >= 3:
        sub_preorder = preorder
        sub_preorder.remove(root.val)
        sub_inorder = inorder
        sub_inorder.remove(root.val)
        middle = int(len(sub_preorder)/2)
        left_preorder = sub_preorder[0:middle]
        right_preorder = sub_preorder[middle::]
        left_inorder = sub_inorder[0:middle]
        right_inorder = sub_inorder[middle::]
        root.left = visualize_bst(left_preorder, left_inorder)
        root.right = visualize_bst(right_preorder, right_inorder)
    return root
    


root = visualize_bst([2,1,3],[1,2,3])

print(root.val)
print(root.left.val)
print(root.right.val)
