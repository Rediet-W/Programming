class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = 0
        points.sort(key = lambda x:x[1])
        curr = points[0][0] -1
        for i,j in points:
            if i <= curr <= j:
                continue
            else:
                arrows +=1 
                curr = j

        return arrows
            