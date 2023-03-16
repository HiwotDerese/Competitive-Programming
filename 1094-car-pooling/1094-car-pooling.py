class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        _min, _max, leng = float('inf'), -float('inf'), len(trips)
        
        for i in range(leng):
            _min = min(_min, trips[i][1])
            _max = max(_max, trips[i][2])

        arr = [0] * (_max - _min + 3)
        # print(_min, _max, arr)
        for i in range(leng):
            arr[trips[i][1] - _min] += trips[i][0]
            # print(trips[i][2] - _min)
            arr[trips[i][2] - _min] -= trips[i][0]
            
        pre = 0
        for i in range(len(arr)):
            arr[i] += pre
            pre = arr[i]
            
        if max(arr) > capacity:
            return False
        return True
        
            
        
        