class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # if len(nums) == 1 and nums[0] == k:
        #     return k
        i = 0
        minm = len(nums) + 1
        while i < len(nums):
            j = i
            sums = 0
            while j < len(nums):
                sums += nums[j]
                if sums >= k:
                    minm = min(minm, j - i + 1)
                    break
                j += 1
            i += 1
        return minm if minm <= len(nums) else -1