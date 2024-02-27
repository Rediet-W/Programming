# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = 0
        total = 0
      
        def summ(root, s):
            nonlocal total
            
            if not root:
                return None
            s = s*10 + root.val 
            if root.left == None and root.right == None:
                total += s
                return 
            
            summ(root.left, s) 
            summ(root.right, s)
        summ(root, s)  
        return total