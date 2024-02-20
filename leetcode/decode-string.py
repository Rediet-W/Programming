class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                curr = ''
                while len(stack) > 0 and stack[-1] != "[":
                    j = stack.pop()
                    curr = j + curr
                print(curr)
                stack.pop()
                times = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    times = stack.pop() + times
                ans = curr*int(times)
                for i in range(len(ans)):
                    stack.append(ans[i])

        return "".join(stack)         
