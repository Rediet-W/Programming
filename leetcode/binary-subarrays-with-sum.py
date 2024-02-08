class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        curr = 0
        dictt = defaultdict(int)

        dictt[0] = 1

        for i in range(len(nums)):
            curr += nums[i]
            diff = curr - goal
            res += dictt[diff]
            dictt[curr] +=1

        return res
