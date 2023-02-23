class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # added = 0
        # for i in range(len(nums)):
        #     nums[i] = nums[i] + added
        #     added = nums[i]
        # return nums
        return list(accumulate(nums))