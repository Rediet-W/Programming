class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr= []
        ans = []
        def backtrack(i):
            if sum(curr) == target:
                ans.append(curr[:])
                return
            if i >= len(candidates) or sum(curr) > target:
                return
            curr.append(candidates[i])
            backtrack(i)
            curr.pop()

            backtrack(i+1)
        backtrack(0)
        return ans
                