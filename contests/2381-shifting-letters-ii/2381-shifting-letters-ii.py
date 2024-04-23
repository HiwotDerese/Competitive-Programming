class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        leng, ans = len(shifts), ""
        alphabet = string.ascii_lowercase
        dic = {}
        for i in range(len(alphabet)):
            dic[alphabet[i]] = i
            
        # print(dic)
        res = [0] * (len(s) + 1)
        # print(res)
        for i in range(leng):
            start = shifts[i][0]
            end = shifts[i][1]
            if shifts[i][2] == 1:
                res[start] += 1
                res[end + 1] -= 1
                
            else:
                res[start] -= 1
                res[end + 1] += 1
            # print(res)
                
                
        pre_sum = 0
        for i in range(len(s)):
            res[i] += pre_sum
            pre_sum = res[i]
            ans += alphabet[(dic[s[i]] + res[i]) % 26]

        return ans
            
            
        
            
            
        
                
            
        