class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        visited = {}
        best = 10** 20

        for i,c in enumerate(cards):
            if c in visited:
                best = min(best, i-visited[c] +1)
            visited[c] = i
        
        if best == 10 ** 20:
            return -1
        return best