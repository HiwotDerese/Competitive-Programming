class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        leng = len(matrix)
        
        for i in range(leng):
            for j in range(i,leng):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print(matrix[i])
            matrix[i].reverse()
            
        return matrix
        