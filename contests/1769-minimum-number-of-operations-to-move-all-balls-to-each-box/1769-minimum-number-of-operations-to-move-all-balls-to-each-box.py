class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        arr = list(map(lambda a: int(a), boxes))
        print(arr)
        leng = len(boxes)
        ans = []
        
        for i in range(leng):
            operation = 0
            
            for j in range(leng):
                if arr[j] == 1:
                    op = abs(j - i)
                    operation += op
                    
            ans.append(operation)
            
        return ans
                
        