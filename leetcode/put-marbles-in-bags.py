class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pair = []
        for i in range(len(weights)-1):
            pair.append(weights[i] + weights[i+1])
        
        pair.sort()
        
        mn = sum(pair[:k-1])
        mx = sum(pair[len(pair) - k + 1:])
        return mx-mn
