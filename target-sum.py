class Solution:
    def dfs(self, idx, sum_, n, nums, k):

        if (idx, sum_) in self.memo:
            if self.memo[(idx, sum_)]:
                self.ans += self.memo[(idx, sum_)]

            return self.memo[(idx, sum_)]

        if idx == n:
            if sum_ == k:
                self.ans += 1
                return 1

            return 0

        self.memo[(idx + 1, sum_ + nums[idx])] = self.dfs(idx + 1, sum_ + nums[idx], n, nums, k)
        
        self.memo[(idx + 1, sum_ - nums[idx])] = self.dfs(idx + 1, sum_ - nums[idx], n, nums, k)

        self.memo[(idx, sum_)] = self.memo[(idx + 1, sum_ + nums[idx])]  + self.memo[(idx + 1, sum_ - nums[idx])]

        return self.memo[(idx, sum_)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ans, self.memo = 0, {}

        self.dfs(0, 0, len(nums), nums, target)
        
        return self.ans