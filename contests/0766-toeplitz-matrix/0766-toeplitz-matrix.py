class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for i in range(row_len-1):
            
            for j in range(col_len-1):
                
                if matrix[i][j] != matrix[i+1][j+1]:
                    
                    return False
                
        return True
        
        