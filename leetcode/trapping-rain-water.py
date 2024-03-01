class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1 
        trapped = 0
        lm = height[0]
        rm = height[-1]
        while l< r:
            if height[l] < height[r]:
                l+=1 
                lm = max(lm, height[l])
                trapped += lm - height[l]
            else:
                r -= 1
                rm = max(rm, height[r])
                trapped += rm - height[r]
        return trapped
