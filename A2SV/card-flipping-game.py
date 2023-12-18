class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cardset= set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                cardset.add(fronts[i])
        res = float(inf)
        for number in (fronts + backs):
            if number not in cardset:
                res = min(res, number)

        if res != float(inf):
            return res
        else:
            return 0