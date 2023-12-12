class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [0]*51
        for i in range(len(ranges)):
            start = ranges[i][0]
            end = ranges[i][1]
            for j in range(start,end + 1):
                arr[j] +=1
        for i in range(left, right+1):
            if arr[i] == 0:
                return False
        return True