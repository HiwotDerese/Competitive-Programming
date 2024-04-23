class Solution:
    def reverseWords(self, s: str) -> str:
        s_arr = list(s.split(" "))
        ans = ""
        for i in s_arr:
            s_reverse = i[::-1]
            ans += s_reverse + " "
        
        
        return ans.strip()