class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        dictt = {}
        for i in range(26):
            dictt[i] = chr(97+i)
        letters = []
        for char in s:
            letters.append(char)
        
        prefix = [0] * len(letters)
        for [l,r,d] in shifts:
            if d == 0:
                prefix[l] -=1
                if r < len(s) -1 :
                    prefix[r+1] +=1
            else:
                prefix[l] += 1
                if r < len(s)-1:
                    prefix[r+1] -=1
        
        curr = 0
        prefixletters = []
        for i in range(len(letters)):
            curr+= prefix[i]
            prefixletters.append(curr)
       
        for j in range(len(letters)):
            z = ord(letters[j]) + prefixletters[j] -97
            z %= 26
            letters[j] = dictt[z]

        s = "".join(letters)
        return s