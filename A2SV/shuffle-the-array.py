class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = len(nums)//2
        shuffled = []
        while i < j and j < len(nums):
            shuffled.append(nums[i])
            shuffled.append(nums[j])
            i+=1
            j+=1
        return shuffled 