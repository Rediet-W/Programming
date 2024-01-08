class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = 0
        nums.sort()

        
        for i in range(len(nums)):
            l, r= i, len(nums)-1
            while l<r:
                if nums[l] + nums[r] >= target:
                    r-=1
                else:
                    pairs += r-l
                    break

        return pairs

        