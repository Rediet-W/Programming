class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nextgreater = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack)!= 0 and temperatures[stack[-1]] < temperatures[i]:
                popped = stack.pop()
                nextgreater[popped] = i
            stack.append(i)
            
        ans = []
        for i in range(len(temperatures)):
            if nextgreater[i]!= 0:
                ans.append(nextgreater[i] - i)
            else:
                ans.append(0)
        return ans
