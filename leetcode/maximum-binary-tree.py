# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def r(arr):
            if len(arr) == 0:
                return 
            k = arr.index(max(arr))
            root = TreeNode(max(arr)) 
            prefix = arr[:k]
            suffix = arr[k+1:]
            root.left = r(prefix)
            root.right = r(suffix)
            return root
        return r(nums)

