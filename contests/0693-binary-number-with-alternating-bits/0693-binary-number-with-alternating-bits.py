class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        compare = 1 & n
        n = n >> 1
        while n != 0:
            
            if compare == (1 & n):
                return False
            compare = 1 & n
            n = n >> 1
            
        return True
            
        