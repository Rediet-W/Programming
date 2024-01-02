class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        ans = []
        up = True
        curr_row,curr_col = 0,0
        while len(ans) != cols * rows:
  
            if up:
                while curr_row >= 0 and curr_col < cols:
                    ans.append(mat[curr_row][curr_col])        
                    curr_row -=1
                    curr_col +=1
                if curr_col == cols:
                    curr_col -=1
                    curr_row +=2
                else:
                    curr_row +=1
                up = False
            else:
                while curr_col >= 0 and curr_row < rows:
                    ans.append(mat[curr_row][curr_col])
                    curr_row +=1
                    curr_col -= 1
                if curr_row == rows:
                    curr_row -=1
                    curr_col +=2
                else:
                    curr_col +=1
                up = True

        return ans
