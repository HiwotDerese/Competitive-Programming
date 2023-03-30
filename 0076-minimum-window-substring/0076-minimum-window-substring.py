class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dic = Counter(t) 
        s_dic = Counter() 
        ans, _min, left = "", float('inf'), 0

        for right in range(len(s)):
            s_dic[s[right]] = 1 + s_dic.get(s[right], 0)
            # print(s_dic)
            while s_dic >= t_dic: 
                # print(s_dic)
                if (right - left + 1) < _min:
                    ans = s[left:right+1]
                    _min = right - left + 1
                    
                s_dic[s[left]] -= 1
                left += 1

        return ans 
                
                
        
        
        
        
        
        