class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        p = 0
        i = 0
        while p < n:
            if i < len(nums) and nums[i] <= p+1:
                p += nums[i]
                i+=1
            else:
                patches += 1
                p+= p+1

        return patches