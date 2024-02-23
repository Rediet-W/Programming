class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D = deque()
        R = deque()
        for i in range(len(senate)):
            if senate[i] == "D":
                D.append(i)
            else:
                R.append(i)
        while len(R) > 0 and len(D) > 0:
            d = D.popleft()
            r = R.popleft()
            if d < r:
                D.append(d+len(senate))
            else:
                R.append(r + len(senate))
        if len(D) == 0:
            return "Radiant"
        elif len(R) == 0:
            return "Dire"
           



        
