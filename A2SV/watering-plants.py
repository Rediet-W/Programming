class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        steps = 0
        river = -1
        curr_capacity = capacity
        i = 0
        while i < n:
            if plants[river+1] > capacity:
                steps +=2*river + 3
                capacity = curr_capacity
                capacity -= plants[i]
            else:
                steps += 1
                capacity -= plants[river + 1]
            i += 1
            river +=1
        return steps