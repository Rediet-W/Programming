class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = {}
        score, ans = 0,0
        l = 0

        for i,n in enumerate(nums):
            if n in seen:
                while l<seen[n]+1:
                    score -= nums[l]
                    l+=1
            seen[n] = i
            score +=n
            ans = max(ans, score)

        return ans