class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = 1
        for k in range(1, len(nums)):
            if nums[k] != nums[k-1]:
                nums[dup] = nums[k]
                dup+=1
        return dup
