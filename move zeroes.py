class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[j] == 0:
                nums.append(0)
                nums.pop(j)
            else:
                j += 1
            i += 1
                
        
        