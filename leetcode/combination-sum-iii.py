class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [n for n in range(1,10)]
        curr = []
        ans = []
        def backtrack(i):
            if len(curr) == k:
                if sum(curr) == n:
                    ans.append(curr[:])
                return 
            if i >= len(nums) or sum(curr) > n:
                return
            
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()

            backtrack(i+1)
        backtrack(0)
        return ans