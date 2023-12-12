class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word for word in s.split(" ")]
        reversed_word = words[::-1]
        r = []
        for i in reversed_word:
            if i:
                r.append(i)
        reverse = ""
        for i in r:
            reverse += i
            reverse += " "
        return reverse.strip()