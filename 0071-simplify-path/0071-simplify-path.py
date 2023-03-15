class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, curr, idx, leng = [], "", 0, len(path)
        
        while idx < leng:
            if path[idx] == '/':
                if not stack:
                    # print(stack)
                    stack.append(path[idx])
                    # print(stack)
                elif curr:
                    if curr == ".." and len(stack) > 1:
                        # print(stack)
                        stack.pop()

                    elif curr != ".." and curr != ".":
                        # print(stack)
                        if stack[-1] == '/':
                            stack.append(curr)
                        else:
                            # print(curr)
                            stack.append('/' + curr)
            
                curr = ""    
            else:
                curr += path[idx]
            
            # print(stack)
            idx += 1
        
        # print(curr)
        if curr:
            # print(curr)
            if curr == ".." and len(stack) > 1:
                stack.pop()
            elif curr != ".." and curr != ".":
                if stack[-1] == '/':
                    stack.append(curr)
                else:
                    # print(curr)
                    stack.append('/' + curr)

        return "".join(stack)
    
    
    
    