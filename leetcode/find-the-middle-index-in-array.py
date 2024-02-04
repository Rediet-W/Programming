class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = [0] * len(nums)
        right = [0] * len(nums)

        left[0] = nums[0]
        for i in range(1,len(nums)):
            left[i] = left[i-1] + nums[i]
        
        right[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] + nums[i]
        
        if len(nums) == 0:
            return 0
        else:
            for i in range(len(nums)):
                if right[i] == left[i]:
                    return i
            return -1

