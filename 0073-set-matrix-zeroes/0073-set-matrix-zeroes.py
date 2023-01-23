class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = []
        row = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    col.append(j)
                    row.append(i)
        
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for i in range(len(matrix)):
            for j in col:
                matrix[i][j]=0 
        