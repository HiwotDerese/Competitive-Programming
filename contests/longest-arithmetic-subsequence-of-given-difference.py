class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n, ans, dp = len(arr), 0, {}

        for idx in range(n-1, -1, -1):
            if arr[idx] + difference not in dp:
                dp[arr[idx]] = 1

            else:
                dp[arr[idx]] = 1 + dp[arr[idx] + difference]

            ans = max(ans, dp[arr[idx]])

        return ans