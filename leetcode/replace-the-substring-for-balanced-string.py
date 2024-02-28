class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        need = n//4
        char = Counter(s)
        l = 0
        r = 0
        res = float('inf')

        for r in range(len(s)):
            char[s[r]] -= 1
            #once we have found lets try to minimize it
            while l< len(s) and char['Q'] <= need and char['R'] <= need and char['E'] <= need and char['W'] <= need:
                char[s[l]] += 1
                res = min(res, r-l+1)
                l+=1
        return res