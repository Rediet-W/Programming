class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = []
        counted = []
        appear = len(nums)//3
        for i in range(len(nums)):
            if nums[i] not in counted:
                count = nums.count(nums[i])
                if count > appear:
                    majority.append(nums[i])
            else:
                continue
            counted.append(nums[i])
        return majority