# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high, bad = 1, n, n
        
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                bad = min(bad, mid)
                high = mid - 1
            else:
                low = mid + 1
                
                
        return bad
                
            
                
            
        
        
        
        