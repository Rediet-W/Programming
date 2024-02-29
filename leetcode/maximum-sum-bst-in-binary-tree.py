# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Pair:
    def __init__(self, s, b=False, lmax=float('-inf'), rmin=float('inf')):
        self.sum = s
        self.bst = b
        self.max = lmax
        self.min = rmin

class Solution:
    def maxSumBST(self, n):
        self.max = 0
        self.ans(n)
        return self.max

    def ans(self, n):
        if not n:
            return Pair(0, True)
        
        if not n.left and not n.right:
            if self.max < n.val:
                self.max = n.val
            return Pair(n.val, True, n.val, n.val)
        
        lp = self.ans(n.left)
        rp = self.ans(n.right)
        
        np = Pair(lp.sum + rp.sum + n.val)
        if n.val > lp.max and n.val < rp.min and lp.bst and rp.bst:
            np.bst = True
            if self.max < np.sum:
                self.max = np.sum
        else:
            np.bst = False
        
        np.min = min(n.val, lp.min)
        np.max = max(n.val, rp.max)
        
        return np