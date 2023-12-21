class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ls=[]
        ans = []
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                ls.append(matrix[j][i])
            ans.append(ls)
            ls= []
        return ans