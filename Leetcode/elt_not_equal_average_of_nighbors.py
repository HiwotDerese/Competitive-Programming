class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        for i in range(1,len(nums)-1, 1):
            if i == len(nums):
                break
            if (nums[i-1] + nums[i+1]) / 2 == nums[i]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            for i in range(i, 1, -1):
                if (nums[i] + nums[i -2]) / 2 == nums[i -1]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                else: 
                    break
        return nums
