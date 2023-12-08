class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        for i in range(len(nums)):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        rearranged = []
        i = 0
        while i < len(nums)//2:
            rearranged.append(positive[i])
            rearranged.append(negative[i])
            i+=1
        return rearranged
