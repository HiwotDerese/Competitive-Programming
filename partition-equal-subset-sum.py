class Solution:
    def canPartition(self, nums: List[int]) -> bool:


        target, n = sum(nums) / 2, len(nums)

        dp = defaultdict(bool)

        if sum(nums) % 2 != 0:
            return False

        def dfs(idx, sum_):
            if idx >= n or sum_ > target:
                return False

            if sum_ == target:
                return True

            if (idx, sum_) in dp:
                return dp[(idx, sum_)]

            # curr = False
            dp[(idx, sum_)] = dfs(idx + 1, sum_ + nums[idx]) or dfs(idx + 1, sum_)
            return dp[(idx, sum_)]

        return dfs(0, 0)