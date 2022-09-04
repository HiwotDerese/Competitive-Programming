class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        queue = []
        n = len(s)
        for i in s:
            if i == ")":
                while stack and stack[-1] != "(":
                    queue.append(stack.pop())
                stack.pop()
                for j in queue:
                    stack.append(j)
                queue = []
            else:
                stack.append(i)
        return "".join(stack)