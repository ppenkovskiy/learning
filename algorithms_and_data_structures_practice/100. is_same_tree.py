class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if (p == None and q != None) or (q == None and p != None):
            return False
        elif p == None and q == None:
            return True
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and True
        else:
            return False
