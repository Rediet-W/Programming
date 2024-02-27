class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subsets = []
        def subset(i):
            #base case
            if i >= len(nums):
                ans.append(subsets[:])
                return 

            #add the curr
            subsets.append(nums[i])
            subset(i+1)
            subsets.pop()

            #not
            subset(i+1)
        subset(0)
        return ans

        