class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        outPut = []

        for i in range(1,n + 1):
            if ((i % 3 == 0) and (i % 5 == 0)):
                outPut.appened ("FizzBuzz")
            elif i % 3 == 0:
                outPut.append("Fizz")
            elif i % 5 == 0:
                
                outPut.append("Buzz")
            else:
                outPut.append(str(i))
        return outPut