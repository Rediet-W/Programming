class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet_equivalent = ""
        i = 0
        integer_to_alphabet = {str(i): chr(ord('a') + i - 1) for i in range(1, 27)}
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                alphabet_equivalent += integer_to_alphabet[s[i:i+2]]
                i+=3
            else:
                alphabet_equivalent += integer_to_alphabet[s[i]]
                i+=1
        return alphabet_equivalent
                