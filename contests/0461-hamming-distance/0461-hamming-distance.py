class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x > 0 or y > 0:
            num1 = 1 & x
            num2 = 1 & y
            
            if num1 != num2:
                ans += 1
                
            x = x >> 1
            y = y >> 1
            
            # print(bin(x), bin(y))
            
            
        return ans
                
        