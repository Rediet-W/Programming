class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dictt = {}
        for i in arr:
            dictt[i] = dictt.get(i,0) + 1
        vals = dictt.values()
        s = max(vals)
        for i,c in dictt.items():
            if c == s:
                return i
        
        