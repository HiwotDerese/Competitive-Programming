class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0 for i in range(n+1)] for i in range(n+1)]        
        m = len(queries)
        
        for i in range(m):
            row1 = queries[i][0]
            col1 = queries[i][1]
            row2 = queries[i][2]
            col2 = queries[i][3]
            
            for i in range(row2 - row1 + 1):
                matrix[i + row1][col1] += 1
                matrix[i + row1][col2 + 1] -= 1
        
            # print(matrix)
            
        
        for i in range(n + 1):
            pre = 0
            for j in range(n + 1):
                matrix[i][j] += pre
                pre = matrix[i][j]
            matrix[i].pop()
            
        matrix.pop() 
        return matrix
                
                
        
        
                
            
            
            
            