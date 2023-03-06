class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        leng1, leng2 = len(s1), len(s2)
        if leng2 < leng1:
            return False
        
        dic1, dic2 = {}, {}

        for i in range(leng1):
            dic1[s1[i]] = 1 + dic1.get(s1[i], 0)
            dic2[s1[i]] = 0
            
            
        for i in range(leng1):
            if s2[i] in s1:
                dic2[s2[i]] += 1
                
        left = 0
        for right in range(leng1-1, leng2):

            if dic1 == dic2:
                return True
            
            if s2[left] in s1:
                dic2[s2[left]] -= 1
                
            left += 1
            right += 1
            if right < leng2:
                if s2[right] in s1:
                    dic2[s2[right]] = 1 + dic2.get(s2[right], 0) 
                    
        return False
            
        
            
        
            
        