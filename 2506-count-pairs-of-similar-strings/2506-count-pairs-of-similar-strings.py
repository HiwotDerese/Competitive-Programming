class Solution:
    def similarPairs(self, word: List[str]) -> int:
        count = 0
        
        for i in range(len(word)):
            
            for j in range(i):
                
                if set(word[i]) == set(word[j]):
                    count += 1
                    
            print(count)
            
        return count