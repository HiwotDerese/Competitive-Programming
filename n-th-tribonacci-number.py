class Solution:
    def tribonacci(self, n: int, memo = {0:0, 1: 1, 2:1}) -> int:

        if n in memo:
            return memo[n]

        ans = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        memo[n] = ans
        return ans