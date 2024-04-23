class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        hash1 = {}
        hash2 = {}
        ans = []
        
        for i in range(len(p)):
            hash1[p[i]] = 1 + hash1.get(p[i], 0)
            hash2[s[i]] = 1 + hash2.get(s[i], 0)
        i = 0
        j = len(p)
        
        while j < len(s):
            if hash1 == hash2:
                ans.append(i)
                
            hash2[s[i]] -= 1
            hash2[s[j]] = 1 + hash2.get(s[j], 0)
            if hash2[s[i]] == 0:
                hash2.pop(s[i]) 
            
            i += 1
            j += 1
            
            
        if hash1 == hash2:
            ans.append(i)
            
        return ans
            
       

    
    
        
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         if len(s) < len(p):
#             return []
        
#         hash1 = dict((i,0) for i in ascii_lowercase)
#         hash2 = dict((i,0) for i in ascii_lowercase)
#         ans = []
        
#         for i in range(len(p)):
#             hash1[p[i]] += 1
#             hash2[s[i]] += 1
            
#         i = 0
#         j = len(p)
        
#         while j < len(s):
#             if hash1 == hash2:
#                 ans.append(i)
#             hash2[s[i]] -= 1
#             hash2[s[j]] += 1
#             i += 1
#             j += 1
            
#         if hash1 == hash2:
#             ans.append(i)
            
#         return ans
            


        
        