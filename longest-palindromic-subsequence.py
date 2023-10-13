class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = defaultdict(str)

        def longest(st):
            if st in dp:
                return dp[st]

            n = len(st)
            if n <= 1:
                return n

            if st[0] == st[n - 1]:
                dp[st] = 2 + longest(st[1:n - 1])

            else:
                ans = max(longest(st[0 : n - 1]), longest(st[1 : n])) 
                dp[st] = ans

            return dp[st]
            
        return longest(s)






 









# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         text1 = s
#         text2 = "".join(list(reversed(list(s))))
#         dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1) ]
#         for i in range(1,len(dp)):
#             for j in range(1,len(dp[0])):
#                 if text1[i - 1] == text2[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1] + 1
#                 else:
#                     dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])
#         return dp[-1][-1]