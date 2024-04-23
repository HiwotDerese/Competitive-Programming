class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_ = min(nums) + k
        max_ = max(nums) - k

        ans = max_ - min_
        
        return ans if ans >= 0 else 0