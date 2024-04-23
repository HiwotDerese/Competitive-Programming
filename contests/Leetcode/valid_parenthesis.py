class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"{":"}", "[":"]", "(":")"}
        for i in s:
            if i in pairs.keys():
                stack.append(i)
            elif i in pairs.values():
                if len(stack) == 0:
                    return False
                else:
                    x = stack.pop()
                    if pairs[x] != i:
                        return False
        if len(stack) == 0:
            return True
                    