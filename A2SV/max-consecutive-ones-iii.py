class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        flips = k
        while i< len(nums):
            if nums[i] == 0:
                flips -= 1
            if flips <0:
                if nums[j] == 0:
                    flips +=1
                j +=1
            i+=1
        return i-j
        