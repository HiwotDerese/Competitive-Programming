class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        leng = len(s)
        dic = {}
        
        for i in s:
            dic[i] = 0
            
        left, ans = 0, 0
        
        for right in range(leng):
            dic[s[right]] += 1
            _max = max(dic.values())
            
            while (right - left + 1) - (max(dic.values())) > k:
                dic[s[left]] -= 1
                left += 1
                
            ans = max(ans, right - left + 1)
            
            
        return ans
            
            
            
            
            
                
            
            
            
            