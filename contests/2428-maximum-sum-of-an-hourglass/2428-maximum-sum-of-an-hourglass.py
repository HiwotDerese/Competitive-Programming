class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row_leng = len(grid)
        col_leng = len(grid[0])
        pre_sum = []
        
        for row in range(row_leng):
            mtrix = []
            for col in range(col_leng):
                if col == 0:
                    mtrix.append(grid[row][col])
                else:
                    num = mtrix[col - 1] + grid[row][col]
                    mtrix.append(num)
                    
            pre_sum.append(mtrix)
            
        
        _max = 0
        
        for row in range(1,row_leng-1):
            
            for col in range(1, col_leng-1):
                
                if col == 1:
                    pre_sum1 = pre_sum[row - 1][col + 1]
                    pre_sum2 = pre_sum[row + 1][col + 1]
                    num = grid[row][col]
                    _sum = pre_sum1 + pre_sum2 + num
                    print(_sum)
                    _max = max(_max, _sum)
                    
                else:
                    pre_sum1 = pre_sum[row - 1][col + 1] - pre_sum[row - 1][col + 1 - 3]
                    pre_sum2 = pre_sum[row + 1][col + 1] - pre_sum[row + 1][col + 1 - 3]
                    num = grid[row][col] 
                    _sum = pre_sum1 + pre_sum2 + num
                    print(_sum)
                    
                    _max = max(_max, _sum)
                    
                
        return _max
            
            
                
        
        
        