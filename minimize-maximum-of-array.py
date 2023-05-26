class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans, n = nums[0], len(nums)

        for idx in range(1, n):
            sum_ = nums[idx - 1] + nums[idx]
            ans = max(ans, ceil(sum_ / (idx + 1)))
            nums[idx] = sum_

        return ans