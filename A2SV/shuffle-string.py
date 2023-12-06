class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = ''
        for i in range(len(s)):
            shuffled += s[indices.index(i)]
        
        return shuffled
