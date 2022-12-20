class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        r = 0
        l = 0
        count = 0
        prod = 1
        while r < len(nums):
            prod *= nums[r]
            while prod >= k and l < r:
                prod /= nums[l]
                l += 1
            if prod < k:
                count += (r - l + 1)
            r += 1
        return count
