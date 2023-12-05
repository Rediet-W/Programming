class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len_str= min(strs, key=len)
        for i, char in enumerate(min_len_str):
            for left in strs:
                if left[i] != char:
                    return min_len_str[:i]
        return min_len_str