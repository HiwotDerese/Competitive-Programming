class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        min_, max_= [inf], [-inf]*n

        for idx in range(1, n):
            min_.append(min(min_[-1], nums[idx - 1]))
            max_[-(idx + 1)] = max(max_[-idx], nums[-idx])

        for idx in range(n):
            if min_[idx] < nums[idx] < max_[idx]:
                return True