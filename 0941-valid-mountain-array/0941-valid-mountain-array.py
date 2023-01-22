class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        leng = len(arr)
        _max = max(arr)
        idx = arr.index(_max)
        if leng < 3 or idx == 0 or idx == leng-1:
            return False
        # if idx == 0 or idx == leng-1:
        #     return False
        for i in range(idx):
            if arr[i] >= arr[i+1]:
                return False
        for i in range(idx,leng-1):
            if arr[i] <= arr[i + 1]:
                return False
            
        return True
#         uniqueL = len(set(arr))
        
#         if leng < 3 or leng != uniqueL:
#             return False
#         for i in range(1,leng-1):
#             if arr[i-1] < arr[i] > arr[i+1]:
#                 f = arr[:i+1]
#                 fs = sorted(f)
#                 s = arr[i:]
#                 ss = sorted(s, reverse=True)
#                 if f == fs and s == ss:
#                     return True
#         return False
        
        