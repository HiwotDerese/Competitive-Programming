class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # if all(map(lambda n:n==1,nums)):
        #     return sum(nums) - 1
        left = 0
        right = 0
        start = []
        maxm = 0
        while right < len(nums):
            if nums[right] == 0 and not start:
                start.append(right)
            elif nums[right] == 0:
                size = sum(nums[left:right])
                maxm = max(maxm, size)
                left= start[-1]
                start.append(right)
            right += 1
        size = sum(nums[left:right])
        maxm = max(maxm, size)
        if len(start) == 0:
            return sum(nums) - 1
        return maxm