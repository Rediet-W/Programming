class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l,r = 0, len(cardPoints)-k
        summ = sum(cardPoints[r:])
        op = summ
        while r < len(cardPoints):
            summ += (cardPoints[l] - cardPoints[r])
            op = max(op, summ)
            l+=1
            r+=1
        return op
