class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(heights)):
            max_idx = i
            max_val = heights[i]
            for j in range(i + 1,len(heights)):
                if max_val < heights[j]:
                    max_val = heights[j]
                    max_idx = j
            heights[i], heights[max_idx] = heights[max_idx], heights[i]
            names[i], names[max_idx] = names[max_idx] , names[i]

        return names
            

