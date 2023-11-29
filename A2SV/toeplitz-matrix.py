class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def diagonalcheck(row,col):
            val = matrix[row][col]
            while row<len(matrix) and col<len(matrix[0]):
                if matrix[row][col] != val:
                    return False
                row+=1
                col+=1
            return True
        for col in range(len(matrix[0])):
            if not diagonalcheck(0,col):
                return False
        for row in range(len(matrix)):
            if not diagonalcheck(row, 0):
                return False
        return True