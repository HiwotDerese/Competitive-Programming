class Solution:
    def dfs(self, idx, sum_, nums, k):

        if (idx, sum_) in self.memo:
            return self.memo[(idx, sum_)]

        if idx == len(nums):
            return sum_ == k

        self.memo[(idx + 1, sum_ + nums[idx])] = self.dfs(idx + 1, sum_ + nums[idx], nums, k)
        
        self.memo[(idx + 1, sum_ - nums[idx])] = self.dfs(idx + 1, sum_ - nums[idx], nums, k)

        self.memo[(idx, sum_)] = self.memo[(idx + 1, sum_ + nums[idx])]  + self.memo[(idx + 1, sum_ - nums[idx])]

        return self.memo[(idx, sum_)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}

        return self.dfs(0, 0, nums, target)