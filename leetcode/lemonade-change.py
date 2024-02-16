class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                five += 1
                pass
            elif bill == 10:
                five -=1
                tens += 1
            elif tens > 0:
                tens -= 1
                five -=1 
            else:
                five -= 3
            if five < 0:
                return False
        return True
