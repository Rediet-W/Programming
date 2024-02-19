class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        odds = []
        for i in c.values():
            if i % 2==0:
                ans += i
            else:
                odds.append(i)
        if len(odds) != 0:
            ans += sum(odds) - (len(odds) - 1)
        
        return ans 

        