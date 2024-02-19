class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        brackets = {')':'('}
        stack = []
        moves = 0
        for i in s:
            if i in brackets:
                if len(stack) != 0:
                    stack.pop()
                else:
                    moves += 1
            else:
                stack.append(i)
        return moves + len(stack)
