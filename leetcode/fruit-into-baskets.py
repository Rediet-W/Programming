class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dictt = {}
        max_fruits = -float('inf')
        l = 0

        for r in range(len(fruits)):
            dictt[fruits[r]] = dictt.get(fruits[r], 0) +1
            while len(dictt.keys()) > 2:
                dictt[fruits[l]] -=1
                if dictt[fruits[l]] == 0:
                    del dictt[fruits[l]]
                l+=1
            max_fruits = max(max_fruits, r-l+1)

        return max_fruits