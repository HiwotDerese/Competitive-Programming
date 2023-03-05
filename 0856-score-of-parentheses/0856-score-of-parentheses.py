class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if not s:
            return 0

        ans = 0
        stack = []
        trun = 0
        for i in range(len(s)):
            if s[i] == "(":
                turn = 1
                stack.append("(")
                
            if s[i] == ")":
                if turn == 1:
                    ans += 2**(len(stack)-1)
                    turn = 0    
                    
                stack.pop()
                
        return ans
    
    
    

    

    
    
    
    
    
    
    
    
    