class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume = 0
        left, right = 0, len(height)-1
        while left < right:
            curr_vol = min(height[left], height[right]) * (right-left)
            volume = max(volume, curr_vol)
            if height[left] < height[right]:
                left +=1
            else:
                right-=1
        return volume