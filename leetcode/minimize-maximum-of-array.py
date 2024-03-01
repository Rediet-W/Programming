class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n= len(nums)
        ans = 0
        summ = 0
        for i in range(n):
            summ += nums[i]
            ans = max((summ+i)//(i+1), ans)

        return ans