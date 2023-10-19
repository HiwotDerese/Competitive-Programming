class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for row in range(n)] for col in range(m)]

        for row in range(m):
            for col in range(n):
                if col == 0 and row == 0:
                    dp[row][col] = 1

                else:
                    dp[row][col] = dp[row][col - 1]  + dp[row - 1][col]

        return dp[m - 1][n - 1]