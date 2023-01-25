class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        iterating = True
        i = 1
        
        while iterating:
            if i < len(nums):
                if nums[i-1] == nums[i]:
                    nums.pop(i-1)
                else:
                    i += 1
            else:
                iterating = False
                
        return len(nums)