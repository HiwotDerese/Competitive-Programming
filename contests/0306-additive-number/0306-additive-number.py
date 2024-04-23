# "112358"
class Solution:
    def additive(self, num, num1, num2, sum_, found):
        
        if not sum_ and found:
            return True
        
        num3 = str(num1 + num2)
        min_leng = min(len(num3), len(sum_))
        
        if sum_[0: min_leng] == num3:
            return self.additive(num, num2, int(num3), sum_[min_leng:], 1)
        
        return False
        
    def isAdditiveNumber(self, num: str) -> bool:

        for i in range(1, len(num) - 1):
            num1 = int(num[:i])

#               if there are a leading zeros
            if str(num1) != num[:i]:
                break
            
            for j in range(i + 1, len(num)):
                num2 = int(num[i: j])
                if str(num2) != num[i: j]:
                    break

                if self.additive(num, num1, num2, num[j :], 0):
                    return True
                
        # print('ww')
        return False
                
                
        

        
            
            
            
            
            
            
            
            
            
            

        
        
        
        
        