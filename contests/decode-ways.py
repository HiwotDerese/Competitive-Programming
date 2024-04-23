class Solution:
    def numDecodings(self, s: str) -> int:
        if  s[0]=="0":
            return 0

        n = len(s)
        dp = [0] * n
        dp += [1, 1]

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue

            else:
                choice1 = dp[i + 1]

            if i + 1 == n or int(s[i: i+2]) > 26 or (i + 2 < n and int(s[i + 2]) == 0):
                choice2 = 0

            else:
                choice2 = dp[i + 2]

            dp[i] = choice1 + choice2

        return dp[0]