class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            number = nums[i]
            count = 0
            for i in range(len(nums)):
                if nums[i] != number and nums[i] < number:
                    count +=1

            ans.append(count)

        return ans