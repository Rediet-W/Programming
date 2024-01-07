class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k% len(nums)
        l,r = 0,len(nums)-1
        while l<r:
            nums[l] , nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        # so once the array is reversed We only need to reverse two parts till k and the remaining
        l, r = 0, k-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        
        l, r = k, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
