class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        mx_sub = nums[0]
        for i in range(len(nums)):
            curr = max(nums[i], curr + nums[i])
            mx_sub = max(curr, mx_sub)

        return mx_sub