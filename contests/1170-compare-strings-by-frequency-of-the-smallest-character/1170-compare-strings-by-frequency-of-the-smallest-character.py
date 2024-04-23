class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        dic, leng1, leng2, ans = {}, len(queries), len(words), []
        
        def freq(s):
            st = sorted(s)
            i, count = 0, 0
            
            while i < len(s) and st[i] == st[0]:
                count += 1
                i += 1
                
            return count

        
        for i in range(leng2):
            dic[i] = freq(words[i])
                        
        for i in range(leng1):
            count = 0
            
            for j in range(leng2):
                le = freq(queries[i])
                
                if le < dic[j]:
                    count += 1
                    
            ans.append(count)
            
            
        return ans
                    
            
                
            
        