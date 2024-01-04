class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        s = 0
        for i in range(k):
            s+=nums[i]
        curr_sum = s
        for right in range(k,len(nums)):
            curr_sum += nums[right]
            curr_sum -= nums[right-k]
            s= max(s, curr_sum)
        ave = s/k
        return ave
