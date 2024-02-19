class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        i = target
        while i > 2:
            if maxDoubles == 0:
                break
            if i % 2 == 0:
                ans += 1
                maxDoubles -= 1
                i = i //2
            else:
                ans += 2
                maxDoubles -= 1
                i = i // 2
            
        
        if i != 1:
            ans += (i - 1)
        return ans