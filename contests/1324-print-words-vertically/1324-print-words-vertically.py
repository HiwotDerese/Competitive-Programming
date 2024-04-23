class Solution:
    def printVertically(self, s: str) -> List[str]:
        splittedS = s.split()
        leng_str = len(max(splittedS, key=len))
        len_s = len(splittedS)
        
        vertical = []
        
        # print(long_str)
        for i in range(leng_str):
            
            ver_word = ""
            for j in range(len_s):
                word = splittedS[j]
                
                if len(word) > i:
                    ver_word += word[i]
                else:
                    ver_word += " "
            ver_word = ver_word.rstrip()
            vertical.append(ver_word)
            
        return vertical
                    
                
        