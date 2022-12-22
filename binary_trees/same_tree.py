class Solution:
    def isSameTree(self, p, q):
        if not q and not p:
            return True

        if not q and p:
            return False

        if not p and q:
            return False

        if p.val != q.val:
            return False

        left_match = self.isSameTree(p.left, q.left)
        right_match = self.isSameTree(p.right, q.right)

        return left_match and right_match
