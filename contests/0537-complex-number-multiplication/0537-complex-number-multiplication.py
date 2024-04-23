class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        number1 = num1.split("+")
        number2 = num2.split("+")
        
        real1 = int(number1[0])
        real2 = int(number2[0])
        
        leng1 = len(number1[1])
        leng2 = len(number2[1])
        
        imag1 = int(number1[1][:leng1-1])
        imag2 = int(number2[1][:leng2-1])
        
        real = (real1 * real2) - (imag1*imag2)
        imag = (real2*imag1) + (real1*imag2)
        
        ans = str(real) + "+" + str(imag) + "i"
        
        
        return ans       
            
        