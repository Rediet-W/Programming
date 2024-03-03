class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pdiag = set()
        ndiag = set()

        res = []
        board = [["."] *n for i in range(n)]

        def bt(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return 

            for c in range(n):
                if c in cols or r+c in pdiag or r-c in ndiag:
                    continue
                cols.add(c)
                pdiag.add(r+c)
                ndiag.add(r-c)
                board[r][c] = 'Q'

                bt(r+1)

                board[r][c] = '.'
                cols.remove(c)
                pdiag.remove(r+c)
                ndiag.remove(r-c)
        bt(0)
        return res