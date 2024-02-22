class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums) - 1 
        curr = nums[n]
        for i in range(n-1, -1, -1):
            if nums[i] > curr:
                spaces = math.ceil(nums[i] / curr)
                ans += spaces -1
                curr = nums[i]//spaces
            else:
                curr = nums[i] 

        return ans