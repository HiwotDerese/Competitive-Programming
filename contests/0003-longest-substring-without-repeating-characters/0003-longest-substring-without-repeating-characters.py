class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leng = len(s)
        last_seen = {}
        left = 0
        _max = 0
        
        for right in range(leng):
            if s[right] in last_seen:
                if last_seen[s[right]] < left:
                    _max = max(_max, right - left + 1) 
                else:
                    left = last_seen[s[right]] + 1
                
            else:  
                _max = max(_max, right - left + 1) 
            
            last_seen[s[right]] = right
            
        return _max
                
    
    
    
    
    
    
    
    

    
    
    
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         seen = {}
#         left = 0
#         ans = 0
#         for right in range(n):
#             if s[right] not in seen:
#                 ans = max(ans, right - left + 1)
#             else:
#                 if seen[s[right]] < left:
#                     ans = max(ans,right - left + 1)
#                 else:
#                     left = seen[s[right]] + 1
#             seen[s[right]] = right
#         return ans
    
            

        
        
        
        
        
        
        