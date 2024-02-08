class Solution:
    def maxScore(self, s: str) -> int:
        list_s = []
        for i in s:
            list_s.append(int(i))

        zero = 0
        ones = sum(list_s)
        score = 0
        for i in range(len(s)-1):
            if list_s[i] == 0:
                zero += 1
            else:
                ones -= 1
            if len(list_s[:i+1]) != 0 or len(list_s[i+1:]) != 0:
                score = max(score, zero + ones)
        return score
        