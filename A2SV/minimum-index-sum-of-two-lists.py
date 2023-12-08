class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = []
        for i in range(len(list1)):
            if list1[i] in list2:
                common.append([i, i + list2.index(list1[i])])

        common.sort(key=lambda x: x[1])
        sum_min_index = common[0][1]
        common_string= []
        for i in range(len(common)):
            if common[i][1] == sum_min_index:
                common_string.append(list1[common[i][0]])
        
        return common_string
        
        