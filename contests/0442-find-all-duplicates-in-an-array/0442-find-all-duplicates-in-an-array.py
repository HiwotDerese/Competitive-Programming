class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans, leng = [], len(nums)
        
        index = 0
        while index < leng:
            if nums[index] == index + 1:
                index += 1
            
            elif nums[nums[index] - 1] == nums[index]:
                ans.append(nums[index])
                index += 1
                
            else:
                nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]
                
                
        return set(ans)
        
        
        
        
        
        
        
        
        