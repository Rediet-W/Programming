class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_1 = ""
        word_2 = ""
        equal = False
        for i in range(len(word1)):
            word_1 += word1[i]
        for i in range(len(word2)):
            word_2 += word2[i]
        if word_1 == word_2:
            equal = True
        return equal

        