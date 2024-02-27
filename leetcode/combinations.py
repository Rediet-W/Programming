class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def combinations(start, possible):
            if len(possible) == k:
                ans.append(possible.copy())
                return 

            for i in range(start, n+1):
                possible.append(i)
                combinations(i+1, possible)
                possible.pop()
                

        combinations(1, [])
        return ans
        #time complexity
        # 2**n + nCk* k
        # if optimized nCk* k