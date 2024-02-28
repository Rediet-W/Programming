# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        def divide_conquer(arr):
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            mid = len(arr)//2
            curr = TreeNode(arr[mid])
            curr.left = divide_conquer(arr[:mid])
            curr.right = divide_conquer(arr[mid+1:])
            return curr
        return divide_conquer(nums)

