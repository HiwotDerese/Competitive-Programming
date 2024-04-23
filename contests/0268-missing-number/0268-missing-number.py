class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        idx = len(nums)
        nums.append(-1)
        
        index = 0
        while index < len(nums):
            if nums[index] == index or nums[index] == -1:
                index += 1
                
            else:
                nums[nums[index]], nums[index] = nums[index], nums[nums[index]]
                if nums[index] == -1:
                    idx = index
                elif nums[nums[index]] == -1:
                    idx = index
                    
        return idx
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         nums.sort()
        
#         if nums[0] != 0:
#             return nums[0] - 1
        
#         for i in range(nums[-1] - 1):
#             if nums[i + 1] - nums[i] != 1:
#                 return nums[i] + 1
        
        
#         return nums[-1] + 1
        