class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        x_m = abs(target[0])
        y_m = abs(target[1])
        me_to_target = x_m + y_m
        g_sum = []
        for i in range(len(ghosts)):
            x_g = abs(ghosts[i][0] - target[0])
            y_g = abs(ghosts[i][1] - target[1])
            g= x_g + y_g
            g_sum.append(g)
        if me_to_target < min(g_sum):
            return True
        else:
            return False
        