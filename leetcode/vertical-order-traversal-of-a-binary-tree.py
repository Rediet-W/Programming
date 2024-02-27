# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dictt = defaultdict(list)
        def traverse(root, col=0, row = 0):
            if not root:
                return None
            dictt[col].append((root.val, row))
            traverse(root.left, col-1, row+1)
            traverse(root.right, col+ 1, row+1)
            return 
        traverse(root)
        ans = list(dictt.items())
        ans.sort()
        final = []
        
        for i, n in ans:
            n.sort(key= lambda x : (x[1], x[0]))
            curr =[]
            for i in range(len(n)):
                curr.append(n[i][0])
            final.append(curr)
        return final 
       