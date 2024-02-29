class Solution:
    def numberOfWays(self, s: str) -> int:
        #start from 1st index
        #including
        # to find the 1s  [0 0 1 2 2 3] after [3 3 3 2 1 1] at each 0 a[i]*b[] 
        # to 0s [1 2 2 2 3 3] after [3 2 1 1 1 0] at each 1 
        bfr_ones = []
        bfr_zeros = []
        after_ones= [0] * len(s)
        after_zeros = [0] * len(s)
        curz = 0
        curo = 0
        for i in s:
            if i == "1":
                curo += 1
            else:
                curz += 1
            bfr_ones.append(curo)
            bfr_zeros.append(curz)
        cz = 0
        co = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "1":
                co += 1
            else:
                cz += 1
            after_zeros[i] = cz
            after_ones[i] = co
        
        ans = 0
        for i in range(len(s)):
            if s[i] == "0":
                ans += after_ones[i] * bfr_ones[i]
            else:
                ans += after_zeros[i] * bfr_zeros[i]
        return ans