class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        print(m)
        print(n)
        row_sum = [0]*m
        col_sum = [0]*n
        
        diff = []
        
        for i in range(m):
            for j in range(n):
                row_sum[i] += grid[i][j]
                col_sum[j] += grid[i][j]      
        
        for i in range(m):
            arr = []
            for j in range(n):
                ans = row_sum[i] - (m - row_sum[i]) + col_sum[j] - (n - col_sum[j])
                arr.append(ans)
            diff.append(arr)
            
        return diff 
                
                
            
        