# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = deque([root] if root else [])
        bfs = []
        while d:
            level= []
            for i in range(len(d)):
                curr = d.popleft()
                level.append(curr.val)
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
            level = reversed(level) if len(bfs) %2 else level
            bfs.append(level)
        return bfs
