class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        leng = len(grid)
        equal_pairs = 0
        
        rows = []
        cols = []
        for i in range(leng):
            rows.append(grid[i])
            curr_col = []
            for j in range(leng):
                curr_col.append(grid[j][i])
                
            cols.append(curr_col)
        
        for row in rows:
            for col in cols:
                if row == col:
                    equal_pairs += 1
        
        
        return equal_pairs
                    
        