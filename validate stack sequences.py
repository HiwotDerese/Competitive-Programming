class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        count = 0
        while popped:
            if count < len(pushed):
                stack.append(pushed[i])
                i += 1
            elif stack[-1] != popped[0]:
                return False
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
            
            count += 1
        return True
