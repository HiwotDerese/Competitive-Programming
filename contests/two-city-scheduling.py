class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        for i in range(n):
            diff = costs[i][1] - costs[i][0]
            costs[i] = [diff] + costs[i]

        costs.sort()
        ans = 0
        for i in range(n):
            if i < n // 2:
                ans += costs[i][2]

            else:
                ans += costs[i][1]

        return ans