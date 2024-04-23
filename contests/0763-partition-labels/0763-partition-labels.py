class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        leng = len(s)
        last_index = {}
        
        for i in range(leng):
            last_index[s[i]] = i
                    
        cnt = 0
        max_last_index = 0
        
        for i in range(leng):
            max_last_index = max(max_last_index, last_index[s[i]])
            cnt += 1
            
            if i == max_last_index:
                ans.append(cnt)
                cnt = 0
                
        return ans