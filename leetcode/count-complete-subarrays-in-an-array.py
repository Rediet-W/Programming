class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dictt = Counter(nums)
        target = len(dictt.keys())
        l = 0
        
        complete = 0
        for i in range(len(nums)):
            d = defaultdict(int)
            r = i
            while r < len(nums):
                d[nums[r]] += 1
                if len(d.keys()) == target:
                    complete += 1
                r += 1
            print(complete)
        return complete
                
            
        