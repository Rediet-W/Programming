class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        perimeter = []
        nums.sort()
        for i in range(len(nums) - 2):
            sliced = nums[i:i+3]
            if nums[i] + nums[i+1] > nums[i+2]:
                perimeter.append(sum(sliced))
        if len(perimeter) == 0:
            return 0
        else:
            return max(perimeter)