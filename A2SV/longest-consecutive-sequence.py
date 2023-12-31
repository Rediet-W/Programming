class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in nums_s:
                length = 0
                while n + length in nums_s:
                    length +=1
                longest = max(length, longest)
        return longest
            