class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        leng = len(strs)
        word_leng = len(strs[0])
        del_col = 0
        
        for i in range(word_leng):
            for j in range(leng - 1):
                if strs[j][i] > strs[j + 1][i]:
                    del_col += 1
                    break
                    
        return del_col
                    
                
        