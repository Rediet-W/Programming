class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def possible(k):
            hour = 0
            for i in piles:
                hour += ceil(i/k)
            return hour <= h
        ans = r
        while l<= r:
            m = l + (r-l)//2
            if possible(m):
                ans = min(ans, m)
                r = m-1
            else:
                l = m+1
        return ans
