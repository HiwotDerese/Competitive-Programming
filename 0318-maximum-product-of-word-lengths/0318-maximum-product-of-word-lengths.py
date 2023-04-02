class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = dict(zip(string.ascii_lowercase, range(0, 26)))
        ans, leng = 0, len(words)
        bit = []
        
        for i in range(leng):
            curr = [str(0)]*27
            for j in range(len(words[i])):
                curr[dic[words[i][j]]] = str(1)
                
            bit.append(int("".join(curr), 2))
            
        
        for i in range(leng):
            for j in range(i + 1, leng):
                
                if bit[i] & bit[j] == 0:
                    ans = max(ans, (len(words[i]) * len(words[j])))
                    
                    
        return ans
        