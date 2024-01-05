class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        buy = 0
        c= 0
        costs.sort()
        for i in costs:
            buy+=i
            if buy <= coins:
                c+=1
            else:
                break
        return c

        