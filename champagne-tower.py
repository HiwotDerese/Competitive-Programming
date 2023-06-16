class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for _ in range(x)] for x in range(1, query_row + 3)]

        dp[0][0] = poured

        for row in range(query_row + 1):
            for col in range(len(dp[row])):
                curr = dp[row][col]

                if dp[row][col] > 1:
                    dp[row][col] = 1
                    dp[row + 1][col] += (curr - 1) / 2
                    dp[row + 1][col + 1] += (curr - 1) / 2

        return dp[query_row][query_glass]