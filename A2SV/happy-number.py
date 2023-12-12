class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            sqsum= 0
            while n>0:
                sqsum += (n%10)*(n%10)
                n= floor(n/10)
            if sqsum == 1:
                return True
            n= sqsum
        return 