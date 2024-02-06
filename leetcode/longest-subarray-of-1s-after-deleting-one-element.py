class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0 
        start = 0
        zero_count = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count +=1
            while zero_count > 1:
                if nums[start] ==0:
                    zero_count -=1
                start +=1
            max_len = max(max_len, r - start)

        return max_len
        