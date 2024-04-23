class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        max_, choice1, choice2 = [0] * n, 0, 0

        for idx in range(n):
            temp = choice1
            choice1 = max(nums[idx] + choice2, choice1)
            choice2 = temp
            max_[idx] = choice1

        return max_[-1]