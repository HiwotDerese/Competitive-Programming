class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            if len(stack) == 0:
                stack.append([temperatures[i], i])
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    val, idx = stack.pop()
                    ans[idx] = i - idx
                stack.append([temperatures[i], i])
                
                
            # while stack and temperatures[i] > stack[-1][0]:
            #     val, idx = stack.pop()
            #     ans[idx] = i - idx
            # stack.append([temperatures[i], i])
        return ans

                    
        