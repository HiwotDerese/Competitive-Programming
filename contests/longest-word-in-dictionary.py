class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()                  
        dic_, res = {""} , ""
        
        for word in words:
            n = len(word)

            if word[:n-1] in dic_:     
                dic_.add(word)   

                if len(word) > len(res): 
                    res = word  
        
        return res