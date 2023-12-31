class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <3:
            return False

        left, mid = float("inf"), float("inf")
        for i in range(len(nums)):
            if nums[i] > mid:
                return True
            if nums[i] < left:
                left = nums[i]
            elif nums[i] > left and nums[i] < mid:
                mid = nums[i]
            
        return False

        