class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        R = defaultdict(lambda: 1)
        
        for x,y in guards:
            R[x,y] = "G"
        for x,y in walls:
            R[x,y] = "W"

        for r in range(m):
            #right 
            g = 0
            for c in range(n):
                if R[r,c] == 'G':
                    g = 1
                elif R[r,c] == "W":
                    g = 0
                if g and R[r,c] != "G":
                    R[r,c] = 0

            #left 
            g = 0
            for c in range(n-1,-1,-1):
                if R[r,c] == 'G':
                    g = 1
                elif R[r,c] == "W":
                    g = 0
                if g and R[r,c] != "G":
                    R[r,c] = 0
        for c in range(n):
            #down 
            g = 0
            for r in range(m):
                if R[r,c] == 'G':
                    g = 1
                elif R[r,c] == "W":
                    g = 0
                if g and R[r,c] != "G":
                    R[r,c] = 0
                    
            #up 
            g = 0
            for r in range(m-1,-1,-1):
                if R[r,c] == 'G':
                    g = 1
                elif R[r,c] == "W":
                    g = 0
                if g and R[r,c] != "G":
                    R[r,c] = 0

            
        return sum(int(R[x,y] == 1) for x in range(m) for y in range(n))

