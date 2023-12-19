class Solution:
    def minimizedStringLength(self, s: str) -> int:
        dic_s = {}
        for i in s:
            dic_s[i] = dic_s.get(i,0) + 1
        return len(dic_s.keys())