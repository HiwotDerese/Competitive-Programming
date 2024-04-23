class Solution:
    def isPowerOfFour(self, n: int) -> bool:
#         if n == 1:
#             return True
#         if n == 0:
#             return False
        
#         if n % 4 == 4:
#             return self.isPowerOfFour(n // 4)


        if n < 1:
            return False
        elif n == 1:
            return True
        else:
            return self.isPowerOfFour(n/4)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if n == 1:
        #     return True
        # elif n == 0:
        #     return False
        # else:
        #     if n % 4 == 0:
        #         return self.isPowerOfFour(n / 4)
        #     else:
        #         return False