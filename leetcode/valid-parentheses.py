class Solution:
    def isValid(self, s: str) -> bool:
        dictt = {')':'(' , "}" :"{" , "]":"["}
        stack = []
        for i in s:
            if i in dictt:
                if stack and stack[-1] == dictt[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
