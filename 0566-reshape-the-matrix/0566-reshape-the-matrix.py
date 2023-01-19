class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row_len = len(mat)
        col_len = len(mat[0])
        ans = []
        
        if r == row_len or c == col_len:
            return mat
        if r*c != row_len * col_len:
            return mat
        else:
            oneD = []
            for i in range(row_len):
                for j in range(col_len):
                    oneD.append(mat[i][j])
            
            if c == len(oneD) and r == 1:
                ans.append(oneD)
                return ans
            start = 0
            end = c
            arr = []
            for i in range(r):
                ans.append(oneD[start:end])
                # arr.append(oneD[start:end])
                start += c
                end += c
                # ans.append(oneD[start:end])
                
            return ans
                