class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i,n in c.items():
            if n > len(nums)//2:
                return i