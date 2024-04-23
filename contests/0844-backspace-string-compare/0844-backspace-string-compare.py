class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        
        for i in range(len(s)):
            if stackS and s[i] == "#":
                stackS.pop()
                
            elif s[i].isalpha():
                stackS.append(s[i])
                
        for i in range(len(t)):
            if stackT and t[i] == "#":
                stackT.pop()
            elif t[i].isalpha():
                stackT.append(t[i])
        
        print(stackS, stackT)
        if stackS == stackT:
            return True
        
        return False
                
                
            
        