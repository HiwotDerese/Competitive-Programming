class Solution:
    def countDigits(self, num: int) -> int:
        n = str(num)
        ans = 0
        
        for i in range(len(n)):
            if num % int(n[i]) == 0:
                ans += 1
                
        return ans
        