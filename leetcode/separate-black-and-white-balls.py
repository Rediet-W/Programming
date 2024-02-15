class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        ones = 0
        swaps = 0
        # for each zero need to make swaps equal to the numbers ones encountered
        for i in range(n):
            if s[i] == '1':
                ones += 1
            else:
                swaps += ones

        return swaps
