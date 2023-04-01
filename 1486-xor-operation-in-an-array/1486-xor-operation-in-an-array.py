class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start + 2 * 0
        
        for i in range(1, n):
            ans = ans ^ (start + 2 * i)
            
            
        return ans
        