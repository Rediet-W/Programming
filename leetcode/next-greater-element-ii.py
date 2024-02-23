class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nextgreater = [-1] * len(nums)
        n = len(nums)
        stack = []
        
        for i in range(2*n):
            curr = nums[i%n]
            while stack and nums[stack[-1]] < curr:
                popped = stack.pop()
                if popped <n:
                    nextgreater[popped] = nums[i %n]
            stack.append(i%n)

        return nextgreater

