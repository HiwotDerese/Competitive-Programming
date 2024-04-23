class Solution:
    def minCost(self, cost, idx, n, memo):
        if idx == n - 1 or idx == n - 2:
            return 0

        if idx in memo:
            return memo[idx]

        memo[idx] = min((cost[idx + 1]+ self.minCost(cost, idx + 1, n, memo)), (cost[idx + 2] + self.minCost(cost, idx + 2, n, memo)))

        return memo[idx]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n, memo = len(cost), {}
        return min((cost[0]+ self.minCost(cost, 0, n, memo)), (cost[1] + self.minCost(cost, 1, n, memo)))