class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        t_dict = Counter(t)
        l = 0
        
        curr = {}
        possibles = float('inf')
        
        have, need = 0, len(t_dict)

        for r in range(len(s)):
            curr[s[r]] = curr.get(s[r],0) + 1
            if s[r] in t_dict and curr[s[r]] == t_dict[s[r]]:
                have +=1 
            
            while have == need:
                if r-l+1 < possibles:
                    possibles = r-l+1
                    ranges = (l,r)

                curr[s[l]] -= 1 
                if s[l] in t_dict and curr[s[l]] < t_dict[s[l]]:
                    have -= 1
                l+=1

        if possibles != float('inf'):
            l,r = ranges
            return s[l:r+1]
        else:
            return ""
                

        
        
