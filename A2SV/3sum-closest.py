class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = sum(nums[:3])
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l<r:
                curr = nums[l] + nums[r] + nums[i]
                if abs(curr-target) < abs(target-closest):
                    closest = curr
                if curr > target:
                    r-=1
                else:
                    l+=1
        return closest
          
    