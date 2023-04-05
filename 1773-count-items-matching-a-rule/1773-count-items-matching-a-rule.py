class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        if ruleKey == "type":
            var = 0
        elif ruleKey == "color":
            var = 1
        elif ruleKey == "name":
            var = 2
            
        ans = 0
        for i in range(len(items)):
            if items[i][var] == ruleValue:
                ans += 1
                
                
        return ans
            
        