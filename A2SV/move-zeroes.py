class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = 0
        for i in range(0, len(nums)):
            if nums[i]!= 0:
                temp = nums[prev]
                nums[prev]=nums[i]
                nums[i]= temp
                prev+=1

        