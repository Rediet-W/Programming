class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        op = float('inf')
        i,j = 0,0

        while j < k:
            if blocks[j] == 'W':
                white+=1
            j+=1

        while j < len(blocks):
            op = min(op, white)
            if blocks[j] == 'W':
                white +=1
            if blocks[j-k] == 'W':
                white -=1
            j+=1
        op = min(op,white)
        return op