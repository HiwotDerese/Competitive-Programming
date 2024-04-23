class Solution:
    def countBits(self, n: int) -> List[int]:
    
        ans = []
        for i in range(n + 1):
            count, idx = 0, i
            
            while idx != 0:
                if idx % 2 != 0:
                    count += 1
                    
                idx = idx >> 1
                
            ans.append(count)
            
        return ans
                
            
            
            
        
        