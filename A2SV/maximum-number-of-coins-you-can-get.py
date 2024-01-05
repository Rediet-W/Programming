class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        mine = 0
        i = 2
        c = 0
        while c< len(piles)/3:
            mine += piles[-i]
            c+=1
            i+=2
        return mine

            