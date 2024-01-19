class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for i in range(k): # to initialize the window
            if s[i] in vowels:
                count+=1
        maxvowel = count
        curr = count

        for j in range(k, len(s)):
            if s[j] in vowels:
                curr +=1
            if s[j-k] in vowels:
                curr -=1
            maxvowel = max(maxvowel, curr)

        return maxvowel