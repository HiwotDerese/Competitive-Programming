class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 5:
            return 0

        nums.sort()
        left, right, ans = 0, n - 4, inf

        while right < n:
            ans = min(ans, nums[right] - nums[left])
            left += 1
            right += 1

        return ans