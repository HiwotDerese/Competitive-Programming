class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        index, leng = 0, len(nums)
        
        while index < leng:
            
            if nums[nums[index] - 1] == nums[index] and nums[index] != index + 1:
                return nums[index]
            
            elif nums[index] == index + 1:
                index += 1
                
            else:
                nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1] 
                
                
        
        