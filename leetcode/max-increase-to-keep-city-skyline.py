class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        swapped = [[0 for _ in range(n)]  for _ in range(n)] 
        
        for i in range(n):
            for j in range(n):
                swapped[i][j] = grid[j][i]
        ans = 0
        
        for i in range(n):
            for j in range(n):
                r = min(max(grid[i]), max(swapped[j]))
                ans += r- grid[i][j]

        return ans