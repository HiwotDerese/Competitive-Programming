class Solution:
    def longestSubarray(self, nums, limit):
        increase = deque()
        decrease = deque()
        ans = 0
        l = 0
        
        for r in range(len(nums)):
            while increase and nums[increase[-1]] < nums[r]:
                increase.pop()
                
            increase.append(r)
            
            
            while decrease and nums[decrease[-1]] > nums[r]:
                decrease.pop()
                
            decrease.append(r)
            
            
            while nums[increase[0]] - nums[decrease[0]] > limit:
                if l == increase[0]:
                    increase.popleft()
                    
                if l == decrease[0]:
                    decrease.popleft()
                    
                    
                l += 1
                
            
            ans = max(ans, r - l + 1 )
            
            
        return ans
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         minm  = []
#         maxm = []
#         ans = 0
#         i = 0
#         for j in range(len(nums)):
#             while maxm and maxm[-1] < nums[j]:
#                 maxm.pop()
#             while minm and minm[-1] > nums[j]:
#                 minm.pop()
#             minm.append(nums[j])
#             maxm.append(nums[j])
#             if maxm[0] - minm[0] <= limit:
#                 ans = max(ans, j-i+1)
#             else:
#                 if maxm[0] == nums[i]:
#                     maxm.pop(0)
#                 if minm[0] == nums[i]:
#                     minm.pop(0)
#                 i= i+ 1
#         return ans
    
                    
                    
        