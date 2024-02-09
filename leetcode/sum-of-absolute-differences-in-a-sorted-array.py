class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * (n+1)
        suffix = [0] * n

        # build the prefix arr
        curr = 0
        for i in range(n):
            prefix[i] = curr
            curr += nums[i]
        prefix[n] = prefix[n-1] + nums[-1]

        # build the suffix arr
        curr = 0
        for i in range(n-1, -1, -1):
            curr += nums[i]
            suffix[i] = curr

        # create the res arr
        res = [0] * n
        for i in range(n):
            bfr = i* nums[i] - prefix[i]
            after =  suffix[i] - nums[i]*(n-i)
            res[i] = bfr + after

        return res
