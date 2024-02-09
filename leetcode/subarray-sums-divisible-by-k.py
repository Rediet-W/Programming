class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_mod =[]
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            prefix_mod.append(prefix%k)

        remainder = defaultdict(int)
        remainder[0] = 1
        cnt = 0
        for i in prefix_mod:
            if i in remainder:
                cnt += remainder[i]
            remainder[i] += 1

        return cnt


        