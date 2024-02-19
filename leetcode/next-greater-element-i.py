class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextgreater = [-1] * len(nums2)
        # monotonic decreasing stack
        stack = [] 
        for i in range(len(nums2)):
            while len(stack) != 0 and nums2[stack[-1]] < nums2[i]:
                top = stack.pop()
                nextgreater[top] = i
            stack.append(i) 
        
        ans = []
        for i in nums1:
            n = nextgreater[nums2.index(i)]
            if n == -1:
                ans.append(n)
            else:
                ans.append(nums2[n])

        return ans

