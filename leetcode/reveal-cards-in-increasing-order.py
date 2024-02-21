class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        ans = [0] * n
        index = collections.deque(range(n))
        s_deck = sorted(deck)
        for c in s_deck:
            ans[index.popleft()] = c
            if index:
                index.append(index.popleft())
        return ans