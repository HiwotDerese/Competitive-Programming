class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = Counter(s)
        ans = ""
        
        for i in order:
            ans += dic.pop(i, 0) * i
            
        for val, idx in dic.items():
            ans += (val * idx)
            
        return ans
        
    # def customSortString(self, order: str, T: str) -> str:
    #     cnt = Counter(T)  
    #     ans = []
    #     # ans = [cnt.pop(c, 0) * c for c in order] 
    #     for c in order:
    #         ans.append(cnt.pop(c, 0) * c )
    #     for c, v in cnt.items():
    #         ans.append(c * v)                      
    #     return ''.join(ans)