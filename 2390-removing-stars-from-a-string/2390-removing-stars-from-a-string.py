class Solution:
    def removeStars(self, s: str) -> str:
        leng = len(s)
        stack = []
        for i in range(leng):
            if s[i] == "*":
                stack.pop()
                
            else:
                stack.append(s[i])
                
        ans = "".join(stack)
        
        return ans
            
        
        
        
        
        
        
#         count = 0
#         ans = ""
        
#         while stack:
#             if stack[-1] == "*":
#                 count += 1
#                 stack.pop()
#             else:
#                 if count > 0:
#                     # print(count,stack)
#                     for i in range(count):
#                         stack.pop()
#                         count -= 1
#                 else:
#                     ans += stack.pop()
                    
#         a = list(ans)
#         a.reverse()
#         return "".join(a)
            

        
        