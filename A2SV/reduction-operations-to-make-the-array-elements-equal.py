class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        dict_nums = defaultdict(int)
        ope = 0
        for i in nums:
            dict_nums[i] +=1
        unique = list(dict_nums.keys())
        unique.sort()
        for i in range(1,len(unique)):
            ope += i*dict_nums[unique[i]]

        return ope

