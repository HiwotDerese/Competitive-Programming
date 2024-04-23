class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, curr, idx, leng = [], "", 0, len(path)
        
        while idx < leng:
            if path[idx] == '/':
                if not stack:
                    stack.append(path[idx])
                    
                elif curr:
                    if curr == ".." and len(stack) > 1:
                        stack.pop()

                    elif curr != ".." and curr != ".":
                        if stack[-1] == '/':
                            stack.append(curr)
                            
                        else:
                            stack.append('/' + curr)
            
                curr = "" 
                
            else:
                curr += path[idx]
            
            idx += 1
        
        if curr:
            if curr == ".." and len(stack) > 1:
                stack.pop()
                
            elif curr != ".." and curr != ".":
                if stack[-1] == '/':
                    stack.append(curr)
                    
                else:
                    stack.append('/' + curr)

        return "".join(stack)
    
    
    
    