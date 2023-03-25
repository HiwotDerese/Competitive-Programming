class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans, leng = [], len(nums)
        
        index = 0
        while index < leng:
            # print(nums, index)
            if nums[index] == 0:
                index += 1
            
            elif nums[nums[index] - 1] == 0:
                index += 1
                
            else:
                val = nums[index]
                nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]
                nums[val - 1] = 0
                
                
        for i in range(leng):
            if nums[i] > 0:
                ans.append(i + 1)
                
        return ans
        
        
        
    
    
    
    
    
        
        
        
        
        
        