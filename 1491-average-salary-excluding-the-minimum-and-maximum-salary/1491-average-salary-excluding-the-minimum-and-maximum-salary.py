class Solution:
    def average(self, salary: List[int]) -> float:
        minm = min(salary)
        salary.remove(minm)
        maxm = max(salary)
        salary.remove(maxm)
        average = sum(salary) / len(salary)
        return average
        