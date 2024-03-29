# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dictt = defaultdict(int)
        def traverse(root):
            if not root:
                return
            dictt[root.val] += 1
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        freq = max(list(dictt.values()))
        ans = []
        for i,n in dictt.items():
            if n == freq:
                ans.append(i)
        
        return ans
