class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        leng = len(s)-1
        ans = ""
        i = leng
        
        # print(s[4:2])
        
        while i >= 0:
            if s[i] ==  "#":
                num = s[i-2:i]
                # print(num)
                char = chr(int(num) + ord('a') - 1)
                ans += char
                i -= 3
            else:
                num = s[i]
                char = chr(int(num) + ord('a') - 1)
                ans += char
                i -= 1
        return ''.join(reversed(ans))
            
                
        