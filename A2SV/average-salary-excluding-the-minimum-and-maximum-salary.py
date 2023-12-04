class Solution:
    def average(self, salary: List[int]) -> float:
        n = sum(salary) - max(salary) - min(salary)
        average = n/(len(salary) - 2)
        return average