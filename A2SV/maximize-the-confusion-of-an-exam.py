class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        TorF = {'T':0, 'F':0}
        maxfreq = 0
        i= 0
        for j in range(len(answerKey)):
            TorF[answerKey[j]] += 1
            leng = j-i+1
            maxfreq = max(maxfreq, TorF[answerKey[j]])
            if leng > maxfreq + k:
                TorF[answerKey[i]] -= 1
                i += 1
        
        return len(answerKey) - i
            
