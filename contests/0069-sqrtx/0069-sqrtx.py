class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
            
        low, high = 0, x
        best = -1
        
        while low <= high:
            mid = (high - low) // 2 + low

            if mid**2 < x:
                low = mid + 1
                best = mid
            elif mid**2 > x:
                high = mid - 1
            else:
                return mid
            
        return best
                
            
        