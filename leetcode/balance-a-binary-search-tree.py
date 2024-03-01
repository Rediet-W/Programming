# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inordertraversal(root):
            if not root:
                return 
            inordertraversal(root.left)
            arr.append(root.val)
            inordertraversal(root.right)
            return arr
        nums = inordertraversal(root)
        def dfs(arr):
            if len(arr) == 0:
                return 
            mid = len(arr)//2
            r = TreeNode(arr[mid])
            r.left = dfs(arr[:mid])
            r.right = dfs(arr[mid+1:])
            return r
        return dfs(nums)
