class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixdictt = defaultdict(int)
        prefixdictt[0] = 1
        res = 0
        prefix = 0
        for i in nums:
            prefix += i
            diff = prefix - k
            res += prefixdictt[diff]  
            prefixdictt[prefix] +=1
        return res

