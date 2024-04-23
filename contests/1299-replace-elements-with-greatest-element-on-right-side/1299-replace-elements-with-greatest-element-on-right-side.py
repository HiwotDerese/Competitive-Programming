class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        leng = len(arr)
        
        _max = -1
        
        for i in range(leng-1,-1,-1):
            greatest = arr[i]
            arr[i] = _max
            if greatest > _max:
                _max = greatest
                
        return arr
            
            
            
        