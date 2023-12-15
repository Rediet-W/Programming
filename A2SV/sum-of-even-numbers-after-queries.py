class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_of_even = sum(n for n in nums if n%2 ==0)
        answer = []
        for val, index in queries:
            if nums[index] % 2 == 0:
                sum_of_even-=nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                sum_of_even+=nums[index]
            answer.append(sum_of_even)
        return answer

        