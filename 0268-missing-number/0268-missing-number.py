class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(nums[-1] - 1):
            if nums[i + 1] - nums[i] != 1:
                return nums[i] + 1
        
        if nums[0] != 0:
            return nums[0] - 1
        return nums[-1] + 1
        