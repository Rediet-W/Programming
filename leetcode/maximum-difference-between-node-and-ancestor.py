# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(root, currmax, currmin):
            if not root:
                return currmax - currmin
            currmax = max(currmax, root.val)
            currmin = min(currmin, root.val)

            
            return max(dfs(root.left, currmax, currmin), dfs(root.right, currmax, currmin) )
        return dfs(root, root.val , root.val)

