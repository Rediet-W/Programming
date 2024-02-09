class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        remainder = 0
        prefix_sum = 0
        min_len = n

        # find the total remainder
        for num in nums:
            remainder = (remainder + num) % p
        
        # if the sum is already divisible we return 0
        if remainder == 0:
            return 0

        # dict that holds the prefix_sum to sum of last idx of subarrays that sum to the prefixsum
        prefix_idx = {}
        prefix_idx[0] = -1

        for i in range(n):
            prefix_sum = (prefix_sum + nums[i]) % p
            key = (prefix_sum - remainder + p) % p
            if key in prefix_idx:
                min_len = min(min_len, i- prefix_idx[key])

            prefix_idx[prefix_sum] = i
        
        if min_len == n:
            return -1
        else:
            return min_len