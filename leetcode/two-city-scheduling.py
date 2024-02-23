class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[1] - x[0])
        min_cost = 0
        for i in range(len(costs)//2):
            min_cost += costs[i][1]
            min_cost += costs[len(costs)-1-i][0]
        return min_cost

