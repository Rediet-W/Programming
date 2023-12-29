class Solution:
    def sortSentence(self, s: str) -> str:
        dictt = {}
        words = list(map(str, s.split()))
        for i in words:

            dictt[i[-1]] = i[:-1]
        
        ans = ""
        for n in range(len(words)):
            l = n+1
            w = dictt[str(l)]
            ans += w
            ans+=" "

        ans = ans.strip()
        return ans
