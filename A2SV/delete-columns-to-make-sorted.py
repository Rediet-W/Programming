class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            j= 0
            while j< len(strs)-1:
                if ord(strs[j][i]) <= ord(strs[j+1][i]):
                    j +=1
                else:
                    count+=1
                    break
        return count


