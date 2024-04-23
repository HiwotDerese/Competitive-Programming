class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ans = ""
        minm = min(len(word1), len(word2))
        
        for i in range(minm):
            ans += word1[i]
            ans += word2[i]
            
        if len(word1) > len(word2):
            ans += word1[i+1:]
            
        elif len(word1) < len(word2):
            ans += word2[i+1:]
            
        return ans
        
        