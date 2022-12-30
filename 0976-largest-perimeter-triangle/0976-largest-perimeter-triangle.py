class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        leng = len(nums)
        nums = sorted(nums, reverse=True)
        print(nums)
        
        
        for i in range(leng - 2):
            
            if nums[i] < (nums[i + 1] + nums[i + 2]):
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0
        