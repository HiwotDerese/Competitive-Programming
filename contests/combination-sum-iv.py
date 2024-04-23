class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(len(dp)):
            for j in range(n):
                
                curr = i + nums[j]
                if curr <= target:
                    dp[curr] += dp[i]

        return dp[target]