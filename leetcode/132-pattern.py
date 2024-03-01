class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = [] # montonically decreasing stack (num, prev_min)
        currMin = nums[0] 
        if n < 3:
            return False
        for k in range(1, n):
            while stack and stack[-1][0] <= nums[k]:
                stack.pop()
        
            if stack and nums[k] > stack[-1][1]:
                return True

            stack.append((nums[k], currMin))
            currMin = min(currMin, nums[k])
            
        return False

