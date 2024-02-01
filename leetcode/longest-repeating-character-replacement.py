class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        ans = 0
        l = 0
        
        for r in range(len(s)):
            char[s[r]] = char.get(s[r], 0) + 1

            while r-l+1 - max(char.values()) > k:
                char[s[l]] -=1
                l+=1
            
            ans = max(ans, r-l+1)
        
        return ans