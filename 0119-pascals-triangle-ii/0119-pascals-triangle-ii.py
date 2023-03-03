class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]
        
        arr = self.getRow(rowIndex - 1)
        
        new = [1] * (len(arr) + 1)
        
        for i in range(1, len(arr)):
            new[i] = arr[i - 1] + arr[i]
            
        return new
        