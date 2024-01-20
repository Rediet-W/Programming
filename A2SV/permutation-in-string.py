class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicts1 = dict.fromkeys(string.ascii_lowercase, 0)
        n = len(s1)
        for i in range(n):
            dicts1[s1[i]] +=1
        if len(s1) <=len(s2):
            dicts2 = dict.fromkeys(string.ascii_lowercase, 0)
            for i in range(n):
                dicts2[s2[i]] +=1
            if dicts2 == dicts1:
                return True

            for r in range(n, len(s2)):
                dicts2[s2[r]] +=1
                dicts2[s2[r-n]] -=1
                if dicts2 == dicts1:
                    return True 
            return False

        else: 
            return False
            