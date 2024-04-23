class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        ans = []
        
        for i in range(n-2):
            arr = []
            for j in range(n-2):
                _max = 0
                
                for k in range(i,i+3):
                    sliced = grid[k][j:j+3]
                    # print(sliced)
                    _max = max(_max, max(sliced))
                # print(_max)  
                arr.append(_max)
                
            ans.append(arr)
            
        return ans
                    
                    
        