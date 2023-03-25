class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        index, leng, var = 0, len(nums), float('inf')
        
        while index < leng:
            
            if nums[index] == index + 1:
                index += 1
                
            else:
                if nums[index] - 1 == var:
                    var = index
                    nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]
                    index += 1
                # print(index, nums) 
                
                elif nums[index] == nums[nums[index] - 1]:
                    var = index
                    index += 1
                    
                    
                else:
                    nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1] 
                    
                    
        return [nums[var], var + 1]
                    
                    
                    
                
