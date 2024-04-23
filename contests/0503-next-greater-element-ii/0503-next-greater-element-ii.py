class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans, stack, leng = [], [], len(nums)
        
        for i in range(leng):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
                
              # if no greater found it will remain -1
            ans.append(-1)
            stack.append(i)
            
            
#         for the circular part
        for i in range(leng):
            if stack:
                while stack and nums[stack[-1]] < nums[i]:
                    ans[stack.pop()] = nums[i]
            else:
                break
                    
        return ans
            
        
        
            
        
        
        