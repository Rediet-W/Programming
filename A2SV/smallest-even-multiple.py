class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n== 1:
            return 2
        if n % 2 == 0:
            return n 
        else:
            for i in range(1,n):
                if (n*i) % 2 == 0:
                    return n*i
