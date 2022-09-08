class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        n = len(stack)
        for i in num:
            while k > 0 and stack and stack[-1] > i:
                k -=1
                stack.pop()
            stack.append(i)
        stack = stack[:len(stack)-k]
        ans = "".join(stack)
        return str(int(ans)) if ans else "0"
#         splited = [int(x) for x in str(num)]
#         n = len(splited)
#         count = 0
#         if k == 0:
#             stack = [str(''.join([str(i) for i in stack]))]
#             return stack[0]
#         elif k == 1 and len(num) == 1:
#             return """0"""
#         for i in range(n):
#             if stack[-1] > splited[i] :
#                 stack.pop()
#                 count += 1
#                 if count == k: 
#                     for i in range(i+1,n,1):
#                         stack.append(splited[i])
#                     break
#             else:
#                 count +=1
#                 if count == k: 
#                     for i in range(i+1,n,1):
#                         stack.append(splited[i])
#                     break
#                 else:
#                     continue
        
#         if len(stack) == 1:
#             return str(stack[0])
#         else:
#             if stack[0] == 0:
#                 stack = stack[1:]
#             stack = [str(''.join([str(i) for i in stack]))]
#             return str(int(stack[0]))
            
                
        









# # from typing_extensions import Self


# class Solution:
#     def removeKdigits(num: str, k: int) -> str:
#         stack = []
#         splited = [int(x) for x in str(num)]
#         n = len(splited)
#         count = 0
#         for i in range(n):
#             if len(stack) == 0:
#                 stack.append(splited[i])
#             elif stack[-1] > splited[i]:
#                 stack.pop()
#                 count += 1
#                 if count == k: 
#                     for i in range(i+1,n,1):
#                         stack.append(splited[i])
#                     break
#                 stack.append(splited[i])
#             else:
#                 count +=1
#                 if count == k: 
#                     for i in range(i+1,n,1):
#                         stack.append(splited[i])
#                     break
#                 else:
#                     continue
#         if len(stack) == 1:
#             return str(stack[-1])
#         else:
#             stack = [str(''.join([str(i) for i in stack]))]
#             return stack[0]
#     print(removeKdigits("1432219", 3))   
#     # removeKdigits("1432219", 3)           
    