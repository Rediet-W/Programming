class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        curr =[]
        def backtrack(i):
            if sum(curr) == target:
                ans.append(curr[:])
                return 
            if i >= len(candidates) or sum(curr) > target :
                return 
            curr.append(candidates[i])
            backtrack(i+1)
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i +=1
            curr.pop()

            backtrack(i+1)

        backtrack(0)
        return ans
                