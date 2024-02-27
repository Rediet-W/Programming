class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subsets = []
        nums.sort()
        def subset(i):
            if i >= len(nums):
                ans.append(subsets[:])
                return 
                
            
            # to add it 
            subsets.append(nums[i])
            subset(i+1)
            subsets.pop()

            #not to add
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
          
            subset(i+1)
        subset(0)
        return ans
        