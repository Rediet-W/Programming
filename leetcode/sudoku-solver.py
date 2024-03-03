class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isvalid(r, c, grid, k):
            for i in range(9):
                if grid[r][i] == k or grid[i][c] == k or grid[3*(r//3) + i//3][3*(c//3) + i%3] == k:
                    return False
            return True
        
        def solve(grid):
            for r in range(9):
                for c in range(9):
                    if grid[r][c] == '.':
                        for k in map(str, range(1, 10)):
                            if isvalid(r, c, grid, k):
                                grid[r][c] = k
                                if solve(grid):
                                    return True
                                grid[r][c] = '.'
                        return False
            return True
        
        solve(board)
            