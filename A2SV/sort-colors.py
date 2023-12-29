class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)

        
        for i in range(zero):
            nums[i]  = 0
        for j in range(one):
            nums[zero + j] = 1
        for k in range(two):
            nums[zero + one + k] = 2

        return nums
