class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count= 0
        count = 0
        for n in nums:
            if n == 1:
                count+=1
                max_count= max(count, max_count)
            else:
                count = 0
        return max_count
        
