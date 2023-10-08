class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []

        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])

            elif stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

        print(stack)
        ans = ""

        for idx in range(len(stack)):

            for i in range(stack[idx][1]):
                ans += stack[idx][0]

        return ans