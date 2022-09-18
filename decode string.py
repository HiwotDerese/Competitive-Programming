class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ""
        rep = 0
        for i in s:
            if i == "[":
                stack.append(ans)
                stack.append(rep)
                rep = 0
                ans = ''
            elif i == "]":
                num = stack.pop()
                st = stack.pop()
                ans = st + num * ans
            elif i.isdigit():
                rep = rep*10 + int(i)
            else:
                ans += i
        return ans
            
        