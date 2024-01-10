class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operation = 0
        l, r = 0, len(nums)-1
        nums.sort()
        while l<r and r > 0:
            if nums[l] + nums[r] > k:
                r -=1
            elif nums[l] + nums[r] < k:
                l +=1
            else: 
                operation +=1
                nums.pop(r)
                nums.pop(l)

                r-=2
        
        return operation