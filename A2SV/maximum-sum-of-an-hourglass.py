class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        mx = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[i])-1):
                d = grid[i][j]
                s = 0
                for k in range(3):
                    s+=grid[i-1][j-1+k]
                s+=d
                for k in range(3):
                    s+= grid[i+1][j-1+k]
                mx=max(mx,s)
        return mx
            



        