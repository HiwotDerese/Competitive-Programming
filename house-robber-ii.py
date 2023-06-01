class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 3:
            return max(nums)
            
        dp1, rob1, rob2 = [0] * (n - 1), 0, 0

        for idx in range(n - 1):
            temp = rob1
            rob1 = max(nums[idx] + rob2, rob1)
            rob2 = temp
            dp1[idx] = rob1


        dp2, robb1, robb2 = [0] * (n - 1), 0, 0

        for idx in range(1, n):
            temp = robb1
            robb1 = max(nums[idx] + robb2, robb1)
            robb2 = temp
            dp2[idx - 1] = robb1

        return max(dp1[-1], dp2[-1])