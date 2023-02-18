class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c**0.5)
        
        while left <= right:
            
            _sum = left ** 2 + right ** 2
            if _sum == c:
                return True
            
            elif _sum > c:
                right -= 1
                
            elif _sum < c:
                left += 1
            
        return False
        