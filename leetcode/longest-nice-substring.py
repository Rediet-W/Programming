class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def divide(s): 
            if len(s) < 2 :
                return ""
            set_s = set(s)
            for i in range(len(s)):
                if s[i].swapcase() not in set_s:
                    left = divide(s[:i])
                    right = divide(s[i+1:])
                    return right if len(right) > len(left) else left
            return s
        return divide(s)