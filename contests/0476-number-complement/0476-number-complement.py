class Solution:
    def findComplement(self, num: int) -> int:
        ans = ""
        while num != 0:

            if (1 & num) == 1:
                ans = str(0) + ans
                
            else:
                ans = str(1) + ans 
            num = num >> 1
            
        return int("0b" + ans, 2)
            
        