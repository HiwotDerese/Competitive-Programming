class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in matrix:
            
            if target <= i[-1]:
                
                return target in i
            
        return False

            
        
                    
                
                                                               
        