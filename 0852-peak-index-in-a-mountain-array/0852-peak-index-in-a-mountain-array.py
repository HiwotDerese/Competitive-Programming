class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        
        while low != high:
            
            mid = (low + high) // 2
            # print(low, high, mid)
            if arr[low] < arr[mid]:
                low += 1
            elif arr[low] == arr[mid] and arr[high] > arr[mid]:
                low += 1
            if arr[high] < arr[mid]:
                high -= 1
            # print(low, high, mid)
            
                
        return low
    
    
    
    
    
    
    
        
