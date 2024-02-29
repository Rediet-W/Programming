# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def is_valid_bst(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return (is_valid_bst(node.left, min_val, node.val) and
                    is_valid_bst(node.right, node.val, max_val))
        
        def sum_bst(node):
            nonlocal max_sum
            if not node:
                return 0
            if is_valid_bst(node, float('-inf'), float('inf')):
                subtree_sum = node.val + sum_bst(node.left) + sum_bst(node.right)
                max_sum = max(max_sum, subtree_sum)
                return subtree_sum
            else:
                return 0

        max_sum = 0
        sum_bst(root)
        return max(max_sum, 0)
        

        def sum_bst(node):
            if not node:
                return 0
            if is_valid_bst(node, float('-inf'), float('inf')):
                return node.val + sum_bst(node.left) + sum_bst(node.right)
            else:
                return max(sum_bst(node.left), sum_bst(node.right))

            return sum_bst(root)
        #print(is_valid_bst(root, float('-inf'), float('inf')))
        return max(sum_bst(root), 0)
        #time O(n) - nodes
        space O(h)'''
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