class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = 0
        left = 0
        right = 2**(n-1)

        for i in range(n-1):
            mid = (left + right)//2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                curr = 1-curr

        return curr