class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for i in tokens:
            if i == "+":
                ans = stack.pop() + stack.pop()
                stack.append(int(ans))
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                ans = b - a
                stack.append(int(ans))
            elif i == "*":
                ans = stack .pop() * stack.pop()
                stack.append(int(ans))
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                ans = b / a
                stack.append(int(ans))
            else:
                stack.append(int(i))
        return stack[0]