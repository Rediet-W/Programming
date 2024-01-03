class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ= 0

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                num = mat[r][c]
                if r==c or r+c == len(mat) - 1:
                    summ+=num
        return summ

        