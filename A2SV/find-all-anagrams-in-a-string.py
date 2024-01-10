class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = dict.fromkeys(string.ascii_lowercase, 0)
        for i in p:
            target[i] += 1

        anagram = []
        word = dict.fromkeys(string.ascii_lowercase, 0)
        if sum(target.values()) <= len(s):
            for i in range(len(p)):
                word[s[i]] += 1
            if word == target:
                anagram.append(0)
            for right in range(len(p), len(s)):
                word[s[right]] += 1
                word[s[right-len(p)]] -=1
                if word == target:
                    anagram.append(right-len(p)+1)

            return anagram
            
