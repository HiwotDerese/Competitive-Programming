class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sums = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == k:
                    sums += 1
        return sums