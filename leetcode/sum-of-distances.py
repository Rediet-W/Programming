class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        idx = defaultdict(int)
        freq = defaultdict(int)
        n = len(nums)
        
        ans = [0] * n
        for i in range(n):
            if freq[nums[i]] > 0:
                ans[i] = i*freq[nums[i]] - idx[nums[i]]
            freq[nums[i]] +=1
            idx[nums[i]] +=i
        
        idx = defaultdict(int)
        freq = defaultdict(int)

        for i in range(n-1, -1, -1):
            if freq[nums[i]] > 0:
                ans[i] += idx[nums[i]] - i*freq[nums[i]] 
            freq[nums[i]] +=1
            idx[nums[i]] +=i

        return ans
        