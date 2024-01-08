class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0
        i = 0
        g.sort()
        s.sort()
        while i< len(s):
            for j in range(len(g)):
                if s[i]>= g[j]:
                    content+=1
                    g.pop(j)
                    break
            i+=1
        return content