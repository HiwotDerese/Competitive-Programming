class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for i in s:
            if(len(stk) == 0):
                stk.append(i)

            elif(stk[-1] == i):
                stk.pop()

            else:
                stk.append(i)

        return "".join(stk)
        