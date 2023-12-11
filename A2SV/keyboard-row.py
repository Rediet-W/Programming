class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        same_line= []
        for word in words:
            for row in rows:
                if all(letter in row for letter in word.lower()):
                    same_line.append(word)
                    break
        return same_line