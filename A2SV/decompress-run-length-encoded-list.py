class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        encoded = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            j = 0
            while j<freq:
                encoded.append(val)
                j+=1
        return encoded