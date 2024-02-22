class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lstoc = {}
        for i in range(len(s)):
            lstoc[s[i]] = i
        ans = []
        end = 0
        size = 0
        for i,c in enumerate(s):
            size +=1
            end = max(end, lstoc[c])
            if i == end:
                ans.append(size)
                size =0
        return ans


        return lstoc       