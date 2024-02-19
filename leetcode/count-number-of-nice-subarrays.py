class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        prefixsum=0
        prefix_freq =defaultdict(int)
        prefix_freq[0]=1
        nice = 0
        for i in nums:
            if i == 1:
                prefixsum+=1
            nice += prefix_freq[prefixsum-k]
            prefix_freq[prefixsum]+=1
        return nice
    