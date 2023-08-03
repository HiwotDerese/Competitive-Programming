class Solution:
    def numTrees(self, n: int) -> int:
        dp = {0:1, 1:1}

        for i in range(2, n + 1):

            sum_ = 0
            for j in range(i):
                left, right = j, i - j - 1

                sum_ += dp[left] * dp[right]

            dp[i] = sum_


        return dp[n]