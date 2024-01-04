class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = []
        ans = 0
        for x,y in points:
            xs.append(x)
        xs.sort()
        for i in range(len(xs)-1):
            ans= max(ans, xs[i+1]-xs[i])
        return ans