class Solution:
    def getMaximum(self, n, memo):
        if n in memo:
            return memo[n]

        if n%2 == 0:
            ans = self.getMaximum(n // 2, memo)
            memo[n] = ans
            self.getMaximum((n - 1), memo)
            return ans

        else:
            ans = self.getMaximum(n - 1, memo) + self.getMaximum((n//2) + 1, memo)
            memo[n] = ans
            return ans

    def getMaximumGenerated(self, n: int) -> int:
        memo = {0: 0, 1: 1}
        if n == 0:
            return 0

        self.getMaximum(n, memo)
        return max(memo.values())