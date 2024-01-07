class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        num = 0
        while num < len(nums):
            if nums[num] != 0:
                nums[zero] , nums[num] = nums[num] , nums[zero]
                zero += 1
            num +=1
        


                