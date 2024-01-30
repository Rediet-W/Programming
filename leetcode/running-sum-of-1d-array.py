class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        curr = 0
        for r in nums:
            curr += r
            ans.append(curr)
        return ans