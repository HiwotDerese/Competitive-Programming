class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = len(s)
        num = 0
        operator = "+"
        curr = 0
        nums = set(str(x) for x in range(10))
        for i in range(n):
            if s[i] in nums:
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == n-1:
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    stack.append(int(stack.pop()) * int(num))
                elif operator == "/":
                    stack.append(int(int(stack.pop()) / int(num)))
                num = 0
                operator  = s[i]
        return sum(stack)
        