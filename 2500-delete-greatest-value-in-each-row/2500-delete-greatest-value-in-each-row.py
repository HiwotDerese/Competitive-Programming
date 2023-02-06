class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        ans = 0
        
        for i in range(col):
            _max = 0
            for j in range(row):
                
                num = max(grid[j])
                _max = max(_max, num)
                
                grid[j].remove(num)
                
            ans += _max
            
        return ans
               
        
        