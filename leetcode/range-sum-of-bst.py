# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        def inordertraversal(root):
            if not root:
                return None
            inordertraversal(root.left)
            res.append(root.val)
            inordertraversal(root.right)
            return res
        inordertraversal(root)
        summ = 0
        for i in res:
            if i >= low and i <= high:
                summ+= i

        return summ

            