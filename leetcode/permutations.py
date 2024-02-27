class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            num = nums.pop(0)
            res = self.permute(nums)
            print(res)
            for r in res:
                r.append(num)
            ans.extend(res)
            nums.append(num)

       
        return ans
                