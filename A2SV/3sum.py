class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) -1
            needed = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] > needed:
                    r-=1
                elif nums[l] + nums[r] < needed:
                    l+=1
                else:
                    ans.add((nums[i],nums[l],nums[r]))
                    r-=1
                    l+=1
        return list(ans)
            
