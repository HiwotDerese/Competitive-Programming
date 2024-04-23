class Solution:
    def calculate(self, s: str) -> int:
        stack, n, num, pre_operator = [], len(s), 0, "+"

        nums = [str(x) for x in range(10)]

        for i in range(n):
            if s[i] in nums:
                num = num * 10 + int(s[i])
                
            if s[i] in "+-*/" or i == n-1:
                if pre_operator == "+":
                    stack.append(num)

                elif pre_operator == "-":
                    stack.append(-num)

                elif pre_operator == "*":
                    a = int(stack.pop())
                    b = int(num)
                    stack.append(a * b )

                elif pre_operator == "/":
                    stack.append(int(int(stack.pop()) / int(num)))
                num = 0
                pre_operator  = s[i]

        return sum(stack)