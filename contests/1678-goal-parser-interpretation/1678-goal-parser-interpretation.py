class Solution:
    def interpret(self, command: str) -> str:
        
        ans = ""
        leng = len(command)
        
        for i in range(leng):
            if command[i] == "G":
                ans += command[i]
        
            elif command[i] == "(" and command[i + 1] == ")":
                ans += "o"
            
            elif command[i] == "(" and command[i + 1] == "a":
                ans += "al"
                
        return ans
        