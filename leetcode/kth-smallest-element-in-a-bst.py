# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inordertraversal(root):
            if not root:
                return 
            inordertraversal(root.left)
            arr.append(root.val)
            inordertraversal(root.right)
            return arr
        nums = inordertraversal(root)
        if len(nums) != 0:
            return nums[k-1]
