class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0
        while n > 1:
            if n %2 == 0:
                adv = mat = n//2
            else:
                mat = (n - 1)//2
                adv = mat + 1
            total_matches += mat
            n = adv
        return total_matches