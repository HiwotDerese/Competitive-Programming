class Solution:
    def balancedString(self, s: str) -> int:
        dic, balanced, left, leng, ans = Counter(s), len(s) // 4, 0, len(s), len(s)
                
        if max(dic.values()) == balanced:
            return 0
        
        for right in range(len(s)):
            
            dic[s[right]] -= 1

            while max(dic.values()) <= balanced:
                ans = min(ans, right - left + 1)
                
                dic[s[left]] += 1
                left += 1    
            
        return ans
                
            
                
            
                
            
        
        
        
        
        
        
        