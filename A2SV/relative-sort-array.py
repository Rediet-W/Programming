class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sortedby = {num: index for index, num in enumerate(arr2)}

        sorting = lambda x: (0, sortedby[x]) if x in sortedby else (1,x)
        arr1.sort(key=sorting)
        return arr1
