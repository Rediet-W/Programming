class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = floor(c**0.5)
        found = False
        while left <= right:
            if left **2 + right**2 > c:
                right-=1
            elif left **2 + right**2 < c:
                left +=1
            else:
                found = True
                break
        return found
        