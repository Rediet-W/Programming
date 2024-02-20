class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]   
        above = self.getRow(rowIndex-1)   
        arr = [1] * (rowIndex+1)
        for i in range(1, rowIndex):
            arr[i] = above[i] + above[i-1]
        return arr 