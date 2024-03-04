class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        score = 0
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(score)
                score = 0
            else:
                score = stack[-1] + max(2*score, 1)
                stack.pop()

        return score
