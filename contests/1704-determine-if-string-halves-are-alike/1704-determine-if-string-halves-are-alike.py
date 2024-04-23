class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels, leng = "aeiou", len(s)
        
        str1 = s[:leng // 2]
        str2 = s[leng//2:]
        
        count1 = 0
        for i in str1:
            if i.lower() in vowels:
                count1 += 1
                
        
        count2 = 0
        for i in str2:
            if i.lower() in vowels:
                count2 += 1
                
        if count1 == count2:
            return True
        
        return False
    
    
    1