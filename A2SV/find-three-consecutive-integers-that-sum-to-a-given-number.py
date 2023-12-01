class Solution:
    def sumOfThree(self, num: int) -> List[int]:
            i = num//3
            if num == 3*i:
                return [i-1, i, i+1]
            return [] 
