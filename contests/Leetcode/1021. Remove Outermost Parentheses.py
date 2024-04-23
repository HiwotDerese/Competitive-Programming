class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        openPar = 0
        closePar = 0
        start = 1
        for i in range(len(s)):
            if s[i] == "(":
                openPar += 1
            elif s[i] == ")":
                closePar += 1
            if openPar == closePar:
                ans += s[start:i]
                start = i + 2
                openPar = 0
                closePar = 0
        return ans

            
        # stack = []
        # for par in s:
        #     if par == "(":
        #         stack.append(par)
        #     else:
        #         stack.pop()
        #         if len(stack) != 0:
        #             ans = ans + "()"
        # return ans
