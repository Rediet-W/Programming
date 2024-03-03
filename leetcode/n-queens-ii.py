class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pdiag = set()
        ndiag = set()

        board = [["."] * n for i in range(n)]
        res = 0

        def bt(r):
            nonlocal res
            if r == n:
                res += 1
                return 
            
            for c in range(n):
                if c in cols or r+c in pdiag or r-c in ndiag:
                    continue
                
                board[r][c] = 'Q'
                cols.add(c)
                pdiag.add(r+c)
                ndiag.add(r-c)

                bt(r+1)

                board[r][c] = '.'
                cols.remove(c)
                pdiag.remove(r+c)
                ndiag.remove(r-c)

        bt(0)
        return res
