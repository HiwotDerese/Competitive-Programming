class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        leng = len(words)
        checker = list(words[0])
        
        for i in range(1, leng):
            new_checker = []
            for char in words[i]:
                if char in checker:
                    new_checker.append(char)
                    checker.remove(char)
            checker = new_checker
            
        return checker
                
        
                
                
            
