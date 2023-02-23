leng, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
_min = float("inf")

left = _sum = 0
for right in range(leng):
    _sum += arr[right]

    
    
    _min = min(_min, right - left + 1)


print(_min)

