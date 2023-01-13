class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_leng = len(matrix)
        col_leng = len(matrix[0])
        
        ans = []
        
        for col in range(col_leng):
            
            new = []
            for row in range(row_leng):
                new.append(matrix[row][col])
            ans.append(new)
            
        return ans
                
                
        